import plotly.express as px

def show_violin_plot(df):
    fig = px.violin(df, y="Spending Score (1-100)", x="Gender",
                    color="Gender", box=True, points="all",
                    title="Spending Score Distribution by Gender")
    return fig
