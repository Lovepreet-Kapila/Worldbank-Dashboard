World Bank Multi‑Country Development Dashboard
An interactive Streamlit dashboard that visualizes key development indicators — GDP per capita, CO₂/GHG emissions, and New Firm Density — using the World Bank API.
The dashboard allows users to compare trends across multiple countries and explore relationships between economic, environmental, and entrepreneurial indicators.

🔗 Live App:
https://worldbank-dashboard-myuxqqhpjqwpgcks3makri.streamlit.app/

🔗 GitHub Repository:
https://github.com/Lovepreet-Kapila/worldbank-dashboard


## 1. Introduction
This project analyzes long‑term development patterns using publicly available data from the World Bank.
The dashboard enables users to:
- Compare indicators across countries
- Explore correlations between variables
- Visualize global patterns
- Download processed datasets
The primary analytical focus is a comparison between Germany and India, representing a developed and a developing economy.
Additional countries are included for broader exploration.

## 2. Data Source
All data is retrieved from the World Bank Open Data API, including:
- GDP per capita (NY.GDP.PCAP.CD)
- GHG emissions (EN.GHG.ALL.LU.MT.CE.AR5)
- New Firm Density (IC.BUS.NDNS.ZS)

Data is processed using Python, Pandas, and Plotly, and displayed through a Streamlit interface.

## 3. Dashboard Visualizations
Below is a detailed explanation of each graph included in the dashboard, similar to the YouTube example you shared.

3.1 Trend Over Time (Line Chart)
Purpose:
Shows how a selected indicator changes over time for multiple countries.
What it reveals:
- Long‑term economic or environmental trends
- Differences in growth rates
- Divergence between developed and developing countries
Example Insight:
Germany’s GDP per capita rises steadily, while India’s grows more slowly, highlighting the economic gap.

3.2 Multi‑Indicator Comparison (Scatter Matrix)
Purpose:
Displays pairwise relationships between selected indicators.
What it reveals:
- Whether indicators move together
- Whether countries cluster based on development level
- Outliers or unusual patterns
Example Insight:
Countries with higher GDP per capita tend to have higher New Firm Density, showing a link between income and entrepreneurship.

3.3 Normalized Multi‑Indicator Trends (0–1 Scale)
Purpose:
Allows comparison of indicators with different units by scaling them between 0 and 1.
What it reveals:
- Whether indicators rise or fall together
- Relative growth patterns
- Structural differences between countries
Example Insight:
India’s normalized CO₂ emissions rise faster than its GDP, showing carbon‑intensive growth.

3.4 Correlation Heatmap
Purpose:
Shows the strength and direction of relationships between indicators.
What it reveals:
- Positive or negative correlations
- Whether indicators influence each other
- Which variables move together
Example Insight:
GDP per capita and New Firm Density show a positive correlation, suggesting economic prosperity supports entrepreneurship.

3.5 Bubble Chart (GDP → GHG → New Firm Density)
Purpose:
Visualizes three indicators at once.
- X‑axis: GDP per capita
- Y‑axis: GHG emissions
- Bubble size: New Firm Density
What it reveals:
- How economic development relates to environmental impact
- Whether entrepreneurial activity aligns with income levels
- Country clusters based on development stage
Example Insight:
Germany appears as a high‑GDP, lower‑emissions, high‑entrepreneurship country.
India appears as a lower‑GDP, rising‑emissions, lower‑entrepreneurship country.

3.6 Summary Statistics Table
Purpose:
Provides descriptive statistics (mean, min, max) for each indicator.
What it reveals:
- Average performance
- Extremes in the dataset
- Cross‑country comparisons
Example Insight:
Germany’s average GDP per capita is significantly higher than India’s.

3.7 World Map (Choropleth)
Purpose:
Displays the latest available value of a selected indicator on a global map.
What it reveals:
- Geographic distribution of development indicators
- Regional patterns
- Global inequalities
Example Insight:
GHG emissions are highest in rapidly industrializing countries like China and India.

## 4. Research Focus: Germany vs. India
The accompanying PDF report answers three research questions:
RQ1: How does GDP per capita differ between Germany and India?
Germany maintains a much higher GDP per capita, reflecting its status as a high‑income economy.
RQ2: How have CO₂ emissions changed over time?
Germany’s emissions decline; India’s rise — showing different stages of environmental transition.
RQ3: How does New Firm Density compare?
Germany has a stronger entrepreneurial ecosystem; India’s values are lower and more volatile.

## 5. Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- World Bank API

## 6. Installation (Optional)

pip install -r requirements.txt

streamlit run app.py

## 8. License
   
This project is for academic purposes.
