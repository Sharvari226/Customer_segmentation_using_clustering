import seaborn as sns
import matplotlib.pyplot as plt

def show_correlation_plot(df):
    numeric = df.select_dtypes("number")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(numeric.corr(), annot=True, cmap="viridis", ax=ax)
    ax.set_title("Correlation Plot")
    return fig
