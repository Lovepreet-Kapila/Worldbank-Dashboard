import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(
    page_title="World Bank Dashboard",
    layout="wide"
)

st.title("🌍 World Bank Multi-Country Development Dashboard")
st.write("Compare GDP per capita, GHG emissions, and New Firm Density across countries.")

# -----------------------------
# INDICATORS & COUNTRIES
# -----------------------------
INDICATORS = {
    "GDP per capita": "NY.GDP.PCAP.CD",
    "GHG emissions": "EN.GHG.ALL.LU.MT.CE.AR5",
    "New firm density": "IC.BUS.NDNS.ZS"
}

COUNTRIES = {
    "India": "IND",
    "Germany": "DEU",
    "United States": "USA",
    "China": "CHN",
    "Brazil": "BRA",
    "South Africa": "ZAF",
    "France": "FRA",
    "Japan": "JPN",
    "United Kingdom": "GBR",
    "Canada": "CAN"
}

# -----------------------------
# FETCH FUNCTIONS
# -----------------------------
@st.cache_data
def fetch_indicator(country_code, indicator_code):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=2000"
    response = requests.get(url).json()

    if not isinstance(response, list) or len(response) < 2 or response[1] is None:
        return pd.DataFrame(columns=["date", "value"])

    df = pd.DataFrame(response[1])
    df = df[["date", "value"]]
    df["date"] = pd.to_numeric(df["date"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna().sort_values("date")
    return df


@st.cache_data
def load_all_data():
    data = {}
    for country, code in COUNTRIES.items():
        data[country] = {}
        for ind_name, ind_code in INDICATORS.items():
            df = fetch_indicator(code, ind_code)
            df["country"] = country
            df["indicator"] = ind_name
            data[country][ind_name] = df
    return data


raw_data = load_all_data()

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------
st.sidebar.header("Controls")

indicators = st.sidebar.multiselect(
    "Select Indicators",
    list(INDICATORS.keys()),
    default=["GDP per capita", "GHG emissions", "New firm density"]
)

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    list(COUNTRIES.keys()),
    default=["India", "Germany", "United States"]
)

# Determine year range
all_years = []
for c in selected_countries:
    all_years.extend(raw_data[c]["GDP per capita"]["date"].tolist())

min_year = int(min(all_years))
max_year = int(max(all_years))

year_range = st.sidebar.slider(
    "Select Year Range",
    min_year, max_year,
    (min_year, max_year)
)

# -----------------------------
# BUILD COMBINED DATASET
# -----------------------------
combined = pd.DataFrame()

for c in selected_countries:
    df = pd.DataFrame({"date": raw_data[c]["GDP per capita"]["date"]})
    df["country"] = c

    for ind in indicators:
        df = df.merge(
            raw_data[c][ind][["date", "value"]].rename(columns={"value": ind}),
            on="date",
            how="left"
        )

    combined = pd.concat([combined, df], ignore_index=True)

combined = combined[
    (combined["date"] >= year_range[0]) &
    (combined["date"] <= year_range[1])
]

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Trends", "📊 Correlation", "📋 Summary Stats", "🌍 World Map", "⬇️ Download Data"]
)

# -----------------------------
# UNIVERSAL FIGURE STYLING
# -----------------------------
def style_fig(fig):
    fig.update_layout(
        width=1200,
        height=700,
        title_font=dict(color='black'),
        xaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black')),
        yaxis=dict(title_font=dict(color='black'), tickfont=dict(color='black'))
    )
    fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
    return fig

# -----------------------------
# TAB 1 — TRENDS
# -----------------------------
with tab1:
    st.subheader("Trend Over Time")

    if len(indicators) == 0:
        st.warning("Select at least one indicator.")
    else:
        first_indicator = indicators[0]

        plot_df = pd.concat(
            [raw_data[c][first_indicator] for c in selected_countries],
            ignore_index=True
        )

        plot_df = plot_df[
            (plot_df["date"] >= year_range[0]) &
            (plot_df["date"] <= year_range[1])
        ]

        fig = px.line(
            plot_df,
            x="date",
            y="value",
            color="country",
            title=f"{first_indicator} ({year_range[0]}–{year_range[1]})"
        )
        fig = style_fig(fig)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("Multi‑Indicator Comparison")

    if len(indicators) < 2:
        st.info("Select at least two indicators to compare.")
    else:
        fig_compare = px.scatter_matrix(
            combined,
            dimensions=indicators,
            color="country",
            title="Indicator Comparison Matrix"
        )
        fig_compare = style_fig(fig_compare)
        st.plotly_chart(fig_compare, use_container_width=True)

        st.markdown("---")

    st.subheader("Normalized Multi‑Indicator Trends")

    if len(indicators) < 2:
        st.info("Select at least two indicators to view normalized trends.")
    else:
        norm_df = combined.copy()

        for ind in indicators:
            norm_df[ind] = (norm_df[ind] - norm_df[ind].min()) / (norm_df[ind].max() - norm_df[ind].min())

        fig_norm = px.line(
            norm_df,
            x="date",
            y=indicators,
            color="country",
            title="Normalized Indicator Trends (0–1 Scale)"
        )
        fig_norm = style_fig(fig_norm)
        st.plotly_chart(fig_norm, use_container_width=True)

# -----------------------------
# TAB 2 — CORRELATION
# -----------------------------
with tab2:
    st.subheader("Correlation Analysis")

    if len(indicators) < 2:
        st.info("Select at least two indicators.")
    else:
        corr_df = combined[indicators].dropna()

        if corr_df.empty:
            st.warning("Not enough data for correlation.")
        else:
            corr = corr_df.corr().round(2)
            fig_corr = px.imshow(
                corr,
                text_auto=True,
                color_continuous_scale="RdBu_r",
                title="Correlation Heatmap"
            )
            fig_corr = style_fig(fig_corr)
            st.plotly_chart(fig_corr, use_container_width=True)

        st.markdown("---")

    st.subheader("GDP → GHG → New Firm Density Relationship")

    required = ["GDP per capita", "GHG emissions", "New firm density"]

    if not all(ind in indicators for ind in required):
        st.info("Select GDP per capita, GHG emissions, and New firm density to view this relationship.")
    else:
        bubble_df = combined.dropna(subset=required)

        fig_bubble = px.scatter(
            bubble_df,
            x="GDP per capita",
            y="GHG emissions",
            size="New firm density",
            color="country",
            hover_name="country",
            title="How GDP Relates to GHG Emissions and New Firm Density",
            size_max=40
        )
        fig_bubble = style_fig(fig_bubble)
        st.plotly_chart(fig_bubble, use_container_width=True)

# -----------------------------
# TAB 3 — SUMMARY STATS
# -----------------------------
with tab3:
    st.subheader("Summary Statistics")

    if combined.empty:
        st.warning("No data available.")
    else:
        st.dataframe(combined.groupby("country")[indicators].agg(["mean", "min", "max"]).round(2))

# -----------------------------
# TAB 4 — WORLD MAP
# -----------------------------
with tab4:
    st.subheader("World Map View")

    if len(indicators) == 0:
        st.info("Select at least one indicator.")
    else:
        first_indicator = indicators[0]
        latest_year = combined["date"].max()

        map_df = combined[combined["date"] == latest_year]

        fig_map = px.choropleth(
            map_df,
            locations="country",
            locationmode="country names",
            color=first_indicator,
            hover_name="country",
            color_continuous_scale="Viridis",
            title=f"{first_indicator} in {latest_year}"
        )
        fig_map = style_fig(fig_map)
        st.plotly_chart(fig_map, use_container_width=True)

# -----------------------------
# TAB 5 — DOWNLOAD
# -----------------------------
with tab5:
    st.subheader("Download Data")

    csv = combined.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="worldbank_data.csv",
        mime="text/csv"
    )