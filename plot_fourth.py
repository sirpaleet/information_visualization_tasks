# -*- coding: utf-8 -*-
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import cmasher as cmr
import csv
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.manifold import MDS, TSNE

# To have less repetition a part of the following functions could be made into a helper.

# Reducing dimensionality with PCA:
def plot_data_one(file) -> None:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile)
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
        cmap_colors = cmr.take_cmap_colors('cmr.arctic', 2, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 2 colors in hex
        fig, (ax1, ax2) = plt.subplots(1, 2)
        plt.setp(ax2.get_yticklabels(), visible=False)
        ax1.set(xlabel='Year', ylabel='Gini index reduced (Finland)')
        ax2.set(xlabel='Year')

        # Get data:
        finland_disp = []
        finland_disp_se = []
        finland_mkt = []
        finland_mkt_se = []
        finland_yrs = []
        for row in spamreader:
            match row[0]:
                case "Finland":
                    finland_yrs.append(int(row[1]))
                    finland_disp.append(float(row[2]))
                    finland_disp_se.append(float(row[3]))
                    finland_mkt.append(float(row[4]))
                    finland_mkt_se.append(float(row[5]))

        # Non-standardized data zipped to be used:
        finland_non = list(zip(finland_disp, finland_disp_se, finland_mkt, finland_mkt_se))

        # Preprocessing here (standardization of data):
        # (https://scikit-learn.org/stable/modules/preprocessing.html)
        finland_scaled = preprocessing.StandardScaler().fit(finland_non).transform(finland_non)

        # Draw one-dimensional from non-standardized with PCA (Principal Component Analysis):
        # (https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
        pca_one = PCA(n_components=1)
        non_reduced_pca = pca_one.fit_transform(finland_non)
        ax1.plot(finland_yrs, non_reduced_pca, '.', color=cmap_colors[0], markeredgewidth=2)
        # ax1.legend()
        ax1.grid(linestyle='dashed', color='gainsboro')
        ax1.set_title('Non-Standardized data of Gini indices (Finland) reduced with PCA')
        ax1.axes.set_ylim(-10, 10)
        ax1.set_facecolor('whitesmoke')

        # Draw one-dimensional from standardized with PCA:
        pca_two = PCA(n_components=1)
        scaled_reduced_pca = pca_two.fit_transform(finland_scaled)
        ax2.plot(finland_yrs, non_reduced_pca, '.', color=cmap_colors[1], markeredgewidth=2)
        # ax2.legend()
        ax2.grid(linestyle='dashed', color='gainsboro')
        ax2.set_title('Standardized data of Gini indices (Finland) reduced with PCA')
        ax2.axes.set_ylim(-10, 10)
        ax2.set_facecolor('whitesmoke')

        plt.show()
        return

# Reducing dimensionality with MDS:
def plot_data_two(file) -> None:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile)
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
        cmap_colors = cmr.take_cmap_colors('cmr.arctic', 2, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 2 colors in hex
        fig, (ax1, ax2) = plt.subplots(1, 2)
        plt.setp(ax2.get_yticklabels(), visible=False)
        # plt.setp(ax2.get_xticklabels(), visible=True)
        ax1.set(xlabel='Year', ylabel='Gini index reduced (Finland)')
        ax2.set(xlabel='Year')
        finland_disp = []
        finland_disp_se = []
        finland_mkt = []
        finland_mkt_se = []
        finland_yrs = []
        for row in spamreader:
            match row[0]:
                case "Finland":
                    finland_yrs.append(int(row[1]))
                    finland_disp.append(float(row[2]))
                    finland_disp_se.append(float(row[3]))
                    finland_mkt.append(float(row[4]))
                    finland_mkt_se.append(float(row[5]))
        # Non-standardized data:
        finland_non = list(zip(finland_disp, finland_disp_se, finland_mkt, finland_mkt_se))
        # Preprocessing here (standardization of data):
        # (https://scikit-learn.org/stable/modules/preprocessing.html)
        finland_scaled = preprocessing.StandardScaler().fit(finland_non).transform(finland_non)
        # MDS (Multidimensional scaling) on the non-standardized data with two different random seeds:
        # (https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html)
        # Seed 1:

        # Seed 2:

        return

# Reducing dimensionality with
def plot_data_three(file) -> None:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile)
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
        cmap_colors = cmr.take_cmap_colors('cmr.arctic', 2, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 2 colors in hex
        fig, (ax1, ax2) = plt.subplots(1, 2)
        plt.setp(ax2.get_yticklabels(), visible=False)
        # plt.setp(ax2.get_xticklabels(), visible=True)
        ax1.set(xlabel='Year', ylabel='Gini index reduced (Finland)')
        ax2.set(xlabel='Year')
        finland_disp = []
        finland_disp_se = []
        finland_mkt = []
        finland_mkt_se = []
        finland_yrs = []
        for row in spamreader:
            match row[0]:
                case "Finland":
                    finland_yrs.append(int(row[1]))
                    finland_disp.append(float(row[2]))
                    finland_disp_se.append(float(row[3]))
                    finland_mkt.append(float(row[4]))
                    finland_mkt_se.append(float(row[5]))
        # Non-standardized data:
        finland_non = list(zip(finland_disp, finland_disp_se, finland_mkt, finland_mkt_se))
        # Preprocessing here (standardization of data):
        # (https://scikit-learn.org/stable/modules/preprocessing.html)
        finland_scaled = preprocessing.StandardScaler().fit(finland_non).transform(finland_non)
        # t-SNE (T-distributed Stochastic Neighbor Embedding) on the non-standardized data with two different random seeds for each of three different values of the
        # “perplexity” parameter
        # (https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)
        # Seed 1:

        # Seed 2:

        return

if __name__ == '__main__':
    plot_data_one('swiid9_91_summary.csv')
    # plot_data_two('swiid9_91_summary.csv')
    # plot_data_three('swiid9_91_summary.csv')
