import streamlit as st
import matplotlib.pyplot as plt

def show_pie_chart(df):
    st.subheader("Pie Chart")
    col = st.selectbox("Select column for Pie Chart", df.columns)
    counts = df[col].value_counts()
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

