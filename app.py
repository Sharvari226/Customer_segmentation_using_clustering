# app.py
import streamlit as st
import pandas as pd

# Import visualization functions
from visuals.radar_chart import show_radar_chart
from visuals.bar_chart import show_bar_chart
from visuals.pie_chart import show_pie_chart
from visuals.heatmap import show_heatmap
from visuals.scatter_plot import show_scatter_plot
from visuals.box_plot import show_box_plot
from visuals.histogram import show_histogram
from visuals.line_chart import show_line_chart
from visuals.area_chart import show_area_chart
from visuals.correlation_matrix import show_correlation_matrix

# --- Dashboard UI ---
st.set_page_config(page_title="IoT Data Visualizations Dashboard", layout="wide")

st.title("📊 IoT Data Visualization Dashboard")
st.markdown("Use the sidebar to explore various visualizations")

# Upload or load dataset
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Upload a dataset to continue.")
    st.stop()

st.sidebar.header("Choose Visualization")
options = [
    "Bar Chart", "Pie Chart", "Radar Chart", "Heatmap", "Scatter Plot",
    "Box Plot", "Histogram", "Line Chart", "Area Chart", "Correlation Matrix"
]
choice = st.sidebar.selectbox("Select a Visualization", options)

# --- Display the selected visualization ---
if choice == "Bar Chart":
    show_bar_chart(df)
elif choice == "Pie Chart":
    show_pie_chart(df)
elif choice == "Radar Chart":
    show_radar_chart(df)
elif choice == "Heatmap":
    show_heatmap(df)
elif choice == "Scatter Plot":
    show_scatter_plot(df)
elif choice == "Box Plot":
    show_box_plot(df)
elif choice == "Histogram":
    show_histogram(df)
elif choice == "Line Chart":
    show_line_chart(df)
elif choice == "Area Chart":
    show_area_chart(df)
elif choice == "Correlation Matrix":
    show_correlation_matrix(df)

