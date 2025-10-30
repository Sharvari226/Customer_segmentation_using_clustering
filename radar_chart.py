import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_radar_chart(df):
    st.subheader("Radar Chart")
    cols = st.multiselect("Select numeric columns", df.select_dtypes(include=np.number).columns)
    if len(cols) < 3:
        st.warning("Select at least 3 columns")
        return
    values = df[cols].mean().tolist()
    values += values[:1]
    angles = np.linspace(0, 2*np.pi, len(cols), endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), cols)
    st.pyplot(fig)


