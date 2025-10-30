import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_heatmap(df):
    st.subheader("Heatmap (Correlation Matrix)")

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    if numeric_df.empty:
        st.warning("⚠️ No numeric columns available for correlation heatmap.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

