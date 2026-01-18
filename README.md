World Bank Multi‑Country Development Dashboard
An interactive Streamlit dashboard that visualizes key development indicators — GDP per capita, CO₂/GHG emissions, and New Firm Density — across multiple countries using the World Bank API.
This project was created as part of the module:
1511‑501 Practical Introduction to Programming with Python (WS 2025–26)

🌍 Live Dashboard
👉 [Looks like the result wasn't safe to show. Let's switch things up and try something else!]
(Replace with your actual link after deployment)

📌 Project Overview
This dashboard allows users to:
- Compare GDP per capita, GHG emissions, and New Firm Density
- Analyze trends across multiple countries
- Explore correlations between indicators
- View global patterns using a world choropleth map
- Download the processed dataset for further analysis
The project includes a focused comparison between Germany and India, supported by a detailed PDF report.

📊 Features
1. Trend Analysis
Visualize long‑term trends for any selected indicator across multiple countries.
2. Multi‑Indicator Comparison
Scatter‑matrix and normalized trend charts to compare indicators side‑by‑side.
3. Correlation Heatmap
Understand relationships between economic, environmental, and entrepreneurial indicators.
4. Bubble Chart
Explore how GDP, GHG emissions, and New Firm Density interact.
5. World Map
View the latest indicator values on a global choropleth map.
6. Data Download
Export the processed dataset as a CSV file.

🧠 Research Focus (Germany vs. India)
The accompanying PDF report answers three research questions:
- How does GDP per capita differ between Germany and India?
- How have CO₂ emissions changed over time in both countries?
- How does New Firm Density compare between Germany and India?
A fourth combined‑indicator analysis is included as an optional extension.

🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- World Bank API

📦 Installation (Optional for local use)
pip install -r requirements.txt
streamlit run app.py



📁 Project Structure
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── README.md



👥 Authors
- Lovepreet Kapila
📄 License
This project is for academic purposes.
