import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_box_plot(df):
    st.subheader("Box Plot")
    col = st.selectbox("Select column", df.columns)
    fig, ax = plt.subplots()
    sns.boxplot(y=df[col], ax=ax)
    st.pyplot(fig)

