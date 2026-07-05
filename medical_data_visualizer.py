import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = np.where((df["weight"] / ((df["height"] / 100) ** 2) > 25), 1, 0)
df["overweight"]


# 3

df["choles_norm"] = np.where((df["cholesterol"] > 1), 1, 0)

df["gluc_norm"] = np.where((df["gluc"] > 1), 1, 0)


# 4
def draw_cat_plot():
    # 5

    pd.melt(
        df,
        id_vars=[
            ["choles_norm"],
            ["gluc_norm"],
            ["smoke"],
            ["alco"],
            ["active"],
            ["cardio"],
        ],
        value_vars=["B"],
    )

    # 6
    df_cat = None

    # 7

    # 8
    fig = None

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None

    # 14
    fig, ax = None

    # 15

    # 16
    fig.savefig("heatmap.png")
    return fig
