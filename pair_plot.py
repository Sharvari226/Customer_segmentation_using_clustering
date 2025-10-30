import seaborn as sns
import matplotlib.pyplot as plt

def show_pair_plot(df):
    numeric = df.select_dtypes("number")
    fig = sns.pairplot(numeric)
    return fig.fig
