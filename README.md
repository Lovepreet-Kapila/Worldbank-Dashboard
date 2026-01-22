## World Bank Multi‑Country Development Dashboard

An interactive Streamlit dashboard that visualizes key development indicators — GDP per capita, CO₂/GHG emissions, and New Firm Density — using the World Bank API.
The dashboard enables users to compare trends across countries, explore correlations, and understand global development patterns.

🔗 Live App:

https://worldbank-dashboard-myuxqqhpjqwpgcks3makri.streamlit.app/

🔗 GitHub Repository:

https://github.com/Lovepreet-Kapila/worldbank-dashboard

## 1. Introduction

This project analyzes long‑term development patterns using publicly available data from the World Bank.

The dashboard allows users to:
- Compare indicators across multiple countries
- Explore correlations between economic, environmental, and entrepreneurial metrics
- Visualize global patterns through interactive charts
- Download processed datasets for further analysis
A key focus of the project is a comparison between Germany and India, representing a developed and a developing economy. Additional countries are included for broader exploration.

## 2. Data Source

All data is retrieved programmatically from the World Bank Open Data API, including:
- GDP per capita — NY.GDP.PCAP.CD
- GHG emissions — EN.GHG.ALL.LU.MT.CE.AR5
- New Firm Density — IC.BUS.NDNS.ZS
Data is processed using Python, Pandas, and Plotly, and displayed through a Streamlit interface.

## 3. Dashboard Visualizations

Below is a detailed explanation of each graph included in the dashboard.
These descriptions mirror the analysis presented in the written report.

### 3.1 Trend Over Time (Line Chart)

<img width="1790" height="737" alt="image" src="https://github.com/user-attachments/assets/cf4548fb-f6f5-4545-ae24-e7e8bd8ba7db" />

The trend‑over‑time chart illustrates how a selected indicator evolves across countries, allowing clear comparison of long‑term development patterns. For example, when examining GDP per capita, Germany’s values rise steadily from an already high base, reflecting the stability of a high‑income economy. India’s trajectory, while upward, grows at a slower pace and from a much lower starting point. This contrast highlights the structural economic gap between the two countries and shows how development stages influence growth rates over time.

### 3.2 Multi‑Indicator Comparison (Scatter Matrix)

<img width="1802" height="690" alt="image" src="https://github.com/user-attachments/assets/560caacd-f49d-401c-967b-7ee3ff345c5f" />

The scatter‑matrix visualization provides a multidimensional view of how indicators relate to one another. By plotting each indicator against the others, it becomes possible to observe clusters, correlations, and outliers. Countries with higher GDP per capita often appear in regions of the matrix associated with higher New Firm Density, suggesting a link between economic prosperity and entrepreneurial activity. Meanwhile, developing countries tend to cluster in lower‑value regions, revealing how structural factors shape their development profiles.

### 3.3 Normalized Multi‑Indicator Trends (0–1 Scale)

Normalizing indicators to a 0–1 scale allows direct comparison of variables that otherwise differ in units and magnitude. This visualization highlights the relative pace of change rather than absolute values. For instance, India’s normalized CO₂ emissions rise more sharply than its normalized GDP, indicating that economic growth is accompanied by increasing environmental pressure. Germany, on the other hand, shows more balanced and stable normalized trends, reflecting a transition toward sustainability and efficiency.

### 3.4 Correlation Heatmap

<img width="1816" height="720" alt="image" src="https://github.com/user-attachments/assets/2a3b16cf-ace8-4468-b318-49fa10102d03" />

The correlation heatmap summarizes the strength and direction of relationships between indicators. Strong positive correlations, such as between GDP per capita and New Firm Density, suggest that higher‑income countries tend to support more entrepreneurial activity. Meanwhile, weaker or negative correlations reveal where indicators diverge, such as environmental metrics that do not necessarily move in tandem with economic growth. This visualization helps identify which development dimensions reinforce each other and which evolve independently.

### 3.5 Bubble Chart (GDP → GHG → New Firm Density)

<img width="1817" height="746" alt="image" src="https://github.com/user-attachments/assets/5e88e041-09ad-4e19-9391-f91c5bd1c5db" />

The bubble chart integrates three indicators into a single visualization, offering a holistic view of each country’s development profile. Germany appears as a high‑GDP country with declining emissions and strong entrepreneurial activity, represented by a large bubble positioned in the upper‑left region of the chart. India, by contrast, occupies a lower‑GDP region with rising emissions and smaller bubble sizes, reflecting lower New Firm Density. This combined perspective highlights the contrasting development paths of the two nations and shows how economic, environmental, and entrepreneurial factors interact.

### 3.6 Summary Statistics Table

<img width="1482" height="307" alt="image" src="https://github.com/user-attachments/assets/fac3802c-8b3b-4c68-980e-18636e60420e" />

The summary statistics table provides an overview of each country’s average, minimum, and maximum indicator values. These descriptive metrics help contextualize the visual trends by quantifying differences in economic performance, environmental impact, and entrepreneurial activity. For example, Germany’s significantly higher mean GDP per capita compared to India reinforces the visual findings from the trend charts and underscores the structural gap between the two economies.

### 3.7 World Map (Choropleth)

<img width="1427" height="592" alt="image" src="https://github.com/user-attachments/assets/20cf8169-6f2e-4f42-bb1d-3f7e07b55b21" />

The world map visualizes the latest available value of a selected indicator across countries, offering a global perspective on development patterns. High‑income countries typically appear in darker shades for GDP per capita, while rapidly industrializing nations stand out in emissions‑based maps. This geographic representation helps situate Germany and India within the broader global landscape, showing how their development trajectories compare to regional and global peers.

## 4. Research Focus: Germany vs. Indiia

The accompanying report answers three key research questions:
RQ1: How does GDP per capita differ between Germany and India?
Germany maintains a much higher GDP per capita, reflecting its status as a high‑income economy.
RQ2: How have CO₂ emissions changed over time?
Germany’s emissions decline due to environmental policies, while India’s rise with industrialization.
RQ3: How does New Firm Density compare?
Germany has a stronger entrepreneurial ecosystem; India’s values are lower and more volatile.

## 5. Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- World Bank API

## 6. License
   
This project is for academic purposes.
