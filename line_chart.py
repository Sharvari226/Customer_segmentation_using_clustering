import streamlit as st
import matplotlib.pyplot as plt

def show_line_chart(df):
    st.subheader("Line Chart")
    x_col = st.selectbox("Select X-axis", df.columns)
    y_col = st.selectbox("Select Y-axis", df.columns)
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker='o')
    st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt

def show_line_chart(df):
    st.subheader("Line Chart")
    x_col = st.selectbox("Select X-axis", df.columns)
    y_col = st.selectbox("Select Y-axis", df.columns)
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker='o')
    st.pyplot(fig)
