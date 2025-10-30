import streamlit as st
import pandas as pd

def show_area_chart(df):
    st.subheader("Area Chart")

    # Select numeric columns only
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if not numeric_cols:
        st.warning("No numeric columns available for area chart.")
        return

    # Let user choose which numeric columns to plot
    selected_cols = st.multiselect("Select numeric columns to display", numeric_cols, default=numeric_cols[:2])

    if not selected_cols:
        st.info(" Please select at least one numeric column to display.")
        return

    st.area_chart(df[selected_cols])
