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
        # plt.setp(ax2.get_yticklabels(), visible=False)
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
        ax2.plot(finland_yrs, scaled_reduced_pca, '.', color=cmap_colors[1], markeredgewidth=2)
        # ax2.legend()
        ax2.grid(linestyle='dashed', color='gainsboro')
        ax2.set_title('Standardized data of Gini indices (Finland) reduced with PCA')
        ax2.axes.set_ylim(-5, 5)
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

        # MDS (Multidimensional scaling) on the non-standardized data with two different random seeds:
        # (https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html)

        # Seed 1:
        embedding_one = MDS(n_components=1, n_init=1, init="random")
        non_reduced_mds_one = embedding_one.fit_transform(finland_non)
        print(non_reduced_mds_one)
        ax1.plot(finland_yrs, non_reduced_mds_one, '.', color=cmap_colors[0], markeredgewidth=2)
        ax1.grid(linestyle='dashed', color='gainsboro')
        ax1.set_title('Random seed one')
        ax1.axes.set_ylim(-10, 10)
        ax1.set_facecolor('whitesmoke')

        # Seed 2:
        embedding_two = MDS(n_components=1, n_init=1, init="random")
        non_reduced_mds_two = embedding_two.fit_transform(finland_non)
        print(non_reduced_mds_two)
        ax2.plot(finland_yrs, non_reduced_mds_two, '.', color=cmap_colors[1], markeredgewidth=2)
        ax2.grid(linestyle='dashed', color='gainsboro')
        ax2.set_title('Random seed two')
        ax2.axes.set_ylim(-10, 10)
        ax2.set_facecolor('whitesmoke')

        plt.suptitle("Non-Standardized data of Gini indices (Finland) reduced with MDS")
        plt.show()
        return

# Reducing dimensionality with t-SNE:
def plot_data_three(file) -> None:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile)
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
        cmap_colors_one = cmr.take_cmap_colors('cmr.arctic', 3, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 2 colors in hex
        cmap_colors_two = cmr.take_cmap_colors('cmr.flamingo', 3, cmap_range=(0.2, 0.8), return_fmt='hex')    #
        fig, axs = plt.subplots(3, 2)

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
        finland_non = np.array(list(zip(finland_disp, finland_disp_se, finland_mkt, finland_mkt_se)))

        # t-SNE (T-distributed Stochastic Neighbor Embedding) on the non-standardized data with two different random
        # seeds for each of three different values of the “perplexity” parameter
        # (https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

        # Seed 1:
        number_one = 1 # random_state has a defined int value for repeatability between function calls

        # perplexity parameter one:
        embedding_one = TSNE(n_components=1, learning_rate='auto', random_state=number_one, init='random', perplexity=1)
        non_reduced_tsne_one = embedding_one.fit_transform(finland_non)
        axs[0,0].plot(finland_yrs, non_reduced_tsne_one, '.', color=cmap_colors_one[0], markeredgewidth=2)
        axs[0,0].grid(linestyle='dashed', color='gainsboro')
        axs[0,0].set_title('Random seed one')
        axs[0,0].set_facecolor('whitesmoke')

        # perplexity parameter two:
        embedding_two = TSNE(n_components=1, learning_rate='auto', random_state=number_one, init='random', perplexity=2)
        non_reduced_tsne_two = embedding_two.fit_transform(finland_non)
        axs[1,0].plot(finland_yrs, non_reduced_tsne_two, '.', color=cmap_colors_one[1], markeredgewidth=2)
        axs[1,0].grid(linestyle='dashed', color='gainsboro')
        axs[1,0].set_facecolor('whitesmoke')

        # perplexity parameter three:
        embedding_three = TSNE(n_components=1, learning_rate='auto', random_state=number_one, init='random', perplexity=3)
        non_reduced_tsne_three = embedding_three.fit_transform(finland_non)
        axs[2,0].plot(finland_yrs, non_reduced_tsne_three, '.', color=cmap_colors_one[2], markeredgewidth=2)
        axs[2,0].grid(linestyle='dashed', color='gainsboro')
        axs[2,0].set_facecolor('whitesmoke')

        # Seed 2:
        number_two = 2

        # perplexity parameter one:
        embedding_four = TSNE(n_components=1, learning_rate='auto', random_state=number_two, init='random', perplexity=1)
        non_reduced_tsne_four = embedding_four.fit_transform(finland_non)
        axs[0,1].plot(finland_yrs, non_reduced_tsne_four, '.', color=cmap_colors_two[0], markeredgewidth=2)
        axs[0,1].grid(linestyle='dashed', color='gainsboro')
        axs[0,1].set_title('Random seed two')
        axs[0,1].set_facecolor('whitesmoke')

        # perplexity parameter two:
        embedding_five = TSNE(n_components=1, learning_rate='auto', random_state=number_two, init='random', perplexity=2)
        non_reduced_tsne_five = embedding_five.fit_transform(finland_non)
        axs[1,1].plot(finland_yrs, non_reduced_tsne_five, '.', color=cmap_colors_two[1], markeredgewidth=2)
        axs[1,1].grid(linestyle='dashed', color='gainsboro')
        axs[1,1].set_facecolor('whitesmoke')

        # perplexity parameter three:
        embedding_six = TSNE(n_components=1, learning_rate='auto', random_state=number_two, init='random', perplexity=3)
        non_reduced_tsne_six = embedding_six.fit_transform(finland_non)
        axs[2,1].plot(finland_yrs, non_reduced_tsne_six, '.', color=cmap_colors_two[2], markeredgewidth=2)
        axs[2,1].grid(linestyle='dashed', color='gainsboro')
        axs[2,1].set_facecolor('whitesmoke')

        plt.setp(axs[1, 0].get_xticklabels(), visible=False)
        plt.setp(axs[1, 1].get_xticklabels(), visible=False)
        plt.setp(axs[0, 0].get_xticklabels(), visible=False)
        plt.setp(axs[0, 1].get_xticklabels(), visible=False)
        axs[0, 0].set(ylabel='Gini perplex. 1')
        axs[1, 0].set(ylabel='Gini perplex. 2')
        axs[2, 0].set(xlabel='Year', ylabel='Gini perplex. 3')
        axs[2, 1].set(xlabel='Year')
        plt.suptitle("Non-Standardized data of Gini indices (Finland) reduced with t-SNE")
        plt.show()
        return

if __name__ == '__main__':
    # plot_data_one('swiid9_91_summary.csv')
    # plot_data_two('swiid9_91_summary.csv')
    plot_data_three('swiid9_91_summary.csv')
