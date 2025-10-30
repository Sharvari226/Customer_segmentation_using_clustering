import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_bar_chart(df):
    st.subheader("Bar Chart")
    x_col = st.selectbox("Select X-axis", df.columns)
    y_col = st.selectbox("Select Y-axis", df.columns)
    fig, ax = plt.subplots()
    sns.barplot(x=df[x_col], y=df[y_col], ax=ax)
    st.pyplot(fig)
