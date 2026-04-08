# -*- coding: utf-8 -*-
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
# from urllib.request import urlopen
# import json

def plot_data_one(file) -> None:
    df = pd.read_csv(file, sep=';',
                     dtype={"GeoAreaName": str})
    # For plot 1 use (sequential multi-hue): color_continuous_scale==px.colors.sequential.Turbo,
    # For plot 2 (diverging): color_continuous_scale=px.colors.diverging.balance
    fig = px.choropleth(df,
                        locationmode='country names',
                        locations="GeoAreaName",
                        color='Value',
                        color_continuous_scale=px.colors.diverging.balance,
                        labels={'Value': 'Number of refugees', 'GeoAreaName': 'Area Name'})
    # https://plotly.com/python/reference/layout/
    fig.update_layout(margin={"l":0, "r":0, "pad":0}, title={
        'text' : 'Number of refugees per 100,000 population, by country of origin (2025)',
        'font': {'weight': 1000, 'size': 20},
        'x': 0.5,
        'xanchor': 'center'},
        font={'size': 15},
        coloraxis_colorbar={
            'x':0.92,
            'y':0.5,
            'title': {'text': None},
        })
    fig.show()
    return

def plot_data_two(file) -> None:
    df = pd.read_csv(file, sep=';', usecols=["GeoAreaName", "TimePeriod", "Value"],
                     dtype={"GeoAreaName": str, "TimePeriod": str, "Value": np.float64})
    print(df.loc[list(range(0,11))]["TimePeriod"])
    fig = go.Figure(data=go.Heatmap(
        z=[df.loc[list(range(0,11))]["Value"], df.loc[list(range(11,22))]["Value"], df.loc[list(range(22,33))]["Value"],
           df.loc[list(range(33,44))]["Value"], df.loc[list(range(44,55))]["Value"], df.loc[list(range(55,66))]["Value"],
           df.loc[list(range(66,77))]["Value"], df.loc[list(range(77,88))]["Value"], df.loc[list(range(88,99))]["Value"],
           df.loc[list(range(99,110))]["Value"], df.loc[list(range(110,121))]["Value"], df.loc[list(range(121,132))]["Value"]],
        x=df.loc[list(range(0,11))]["TimePeriod"],
        y=df.loc[[0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]]["GeoAreaName"],
        hoverongaps = False,
        colorscale=px.colors.diverging.balance))
    fig.update_layout(title={
        'text' : 'Number of refugees per 100,000 population, by country of origin (2015-2025, South America)',
        'font': {'weight': 1000, 'size': 20},
        'x': 0.5,
        'xanchor': 'center'},
        font={'size': 17})
    fig.show()
    return

def plot_data_three(file) -> None:
    df = pd.read_csv(file, sep=';', usecols=["GeoAreaName", "TimePeriod", "Value"],
                     dtype={"GeoAreaName": str, "TimePeriod": np.int16, "Value": np.float64})
    df_clustermap = df.pivot(index="GeoAreaName", columns="TimePeriod", values="Value")
    sb.clustermap(data=df_clustermap, col_cluster=False, linewidths=0, figsize=(11, 12), cmap="icefire").fig.suptitle(t='Number of refugees per 100,000 population, by country of origin (2015-2025, South America)', y=0.99, weight=1000)
    plt.show()
    return

if __name__ == '__main__':
    plot_data_three('refugees_2015-2025_South_America.csv')
    # plot_data_two('refugees_2015-2025_South_America.csv')
    # plot_data_one('refugees_2025_csv.csv')
