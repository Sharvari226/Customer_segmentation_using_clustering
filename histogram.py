import streamlit as st
import matplotlib.pyplot as plt

def show_histogram(df):
    st.subheader("Histogram")
    col = st.selectbox("Select column for Histogram", df.columns)
    bins = st.slider("Number of bins", 5, 50, 10)
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=bins, color='skyblue', edgecolor='black')
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
