import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_correlation_matrix(df):
    st.subheader("Correlation Matrix")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), cmap="viridis", annot=True)
    st.pyplot(fig)
