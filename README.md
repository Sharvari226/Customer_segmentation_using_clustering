 Interactive Data Visualization Dashboard (ML Exploratory Analysis)
 A Streamlit-powered dashboard for deep data understanding, visual insights, and pre-model analysis.


Overview

This project focuses on Exploratory Data Analysis (EDA) and Data Visualization for better understanding of machine learning datasets.
It provides an interactive Streamlit dashboard to explore datasets through multiple types of visualizations — enabling users to uncover trends, correlations, and insights before applying ML models.

The dashboard is modular — each visualization (bar chart, scatter plot, pie chart, etc.) is handled by a separate Python file under the visuals/ directory.

Objectives

Perform data exploration and identify key insights visually
Understand feature relationships and distributions
Build an interactive dashboard using Streamlit
Demonstrate data-driven storytelling with charts and plots
Prepare data understanding reports before ML modeling

Project Structure
ML_Visualization_Dashboard/
│
├── app.py                         # Main Streamlit application
│
├── data/
│   └── dataset.csv                
│
├── visuals/
│   ├── bar_chart.py
│   ├── line_chart.py
│   ├── pie_chart.py
│   ├── scatter_plot.py
│   ├── histogram.py
│   ├── box_plot.py
│   ├── radar_chart.py
│   ├── heatmap.py
│   ├── area_chart.py
│   └── correlation_chart.py
│
├── requirements.txt               
│
└── README.md                      


Installations:

Install dependencies
pip install -r requirements.txt

Run the Streamlit app
streamlit run app.py

Technologies used

| Component                | Technology                  |
| ------------------------ | --------------------------- |
| Language                 | Python 3.x                  |
| Dashboard Framework      | Streamlit                   |
| Data Handling            | Pandas, NumPy               |
| Visualization Libraries  | Matplotlib, Seaborn, Plotly |
| Machine Learning Context | EDA, Feature Analysis       |

Visualisations included:

| Visualization         | Description                                      |
| --------------------- | ------------------------------------------------ |
| **Bar Chart**         | Compare categorical values                       |
| **Line Chart**        | Visualize trends across time or sequence         |
| **Pie Chart**         | Show percentage distributions                    |
| **Scatter Plot**      | Explore relationships between numerical features |
| **Histogram**         | Understand feature distributions                 |
| **Box Plot**          | Detect outliers and visualize spread             |
| **Heatmap**           | Show correlation between multiple variables      |
| **Radar Chart**       | Multi-variable comparison across categories      |
| **Area Chart**        | Show cumulative data over a period               |
| **Correlation Chart** | Visualize pairwise feature relationships         |

