# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
import cmasher as cmr
## Notes:
# import matplotlib.colors as mcolors
# Python with matplotlib and seaborn (and altair, plotnine, plotly, HoloViz, ...).Comes with all the pros and cons of Python in general.See MyCourses/General/Companion Code Base for an example how to set upPython for visualization.
# Prefer perceptually uniform colormaps – see colorcet and cmasher in Python
# Python/color-science

def plot_data_one(file) -> None:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(csvfile)
        next(csvfile)
        next(csvfile)
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
        cmap_colors = cmr.take_cmap_colors('cmr.arctic', 8, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 5 colors in hex
        _, ax = plt.subplots()
        ax.set_axisbelow(True)

        titles = []
        incomes = []
        for row in spamreader:
            titles.append(row[0].strip("\""))
            incomes.append(int(row[2]))
        titles[0] = 'Combined'
        ax.grid(linestyle='dashed')
        ax.bar(titles, incomes, color=cmap_colors)
        plt.gca().set_facecolor('whitesmoke')
        ax.set_ylabel('Mean salary income €/year')
        ax.set_xlabel('Age group')

        plt.show()

        return

def plot_data_two(file, file_men, file_all) -> None:
    plt.rcParams["font.family"] = "monospace"
    plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
    cmap_colors = cmr.take_cmap_colors('cmr.arctic', 3, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 5 colors in hex
    i = 0
    incomes = [[],[],[]]
    for f in [file, file_men, file_all]:
        with open(f, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            next(csvfile)
            next(csvfile)
            next(csvfile)
            #cmap_colors = cmr.create_cmap_mod('rainforest')
            #fig, ax = plt.subplots()
            #ax.set_axisbelow(True)
            for row in spamreader:
                new = row[1:]
                incomes[i] = list(map(int, new))
            print(incomes[i])
            years_inner = list(map(int, np.linspace(2004, 2024, 21)))
            title = 'Women' if i == 0 else 'Men' if i == 1 else 'All'
            plt.plot(years_inner, incomes[i], '.-', color=cmap_colors[i], markeredgewidth=2, label=title)
        i += 1

    years = list(map(int, np.linspace(2004, 2024, 11)))
    print(years)
    plt.legend()
    plt.grid(linestyle='dashed', color='gainsboro')
    plt.ylabel('Mean salary income €/year')
    plt.xlabel('Year')
    plt.axis((2004, 2024, 0, 30000))
    plt.xticks(years, years)
    plt.gca().set_facecolor('whitesmoke')
    plt.show()

    return

def plot_data_three(file_men, file_women, file_men_old, file_women_old) -> None:
    plt.rcParams["font.family"] = "monospace"
    plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
    cmap_colors_men = cmr.take_cmap_colors('cmr.flamingo', 2, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 2 colors in hex
    cmap_colors_women = cmr.take_cmap_colors('cmr.arctic', 2, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 2 colors in hex
    i = 0
    incomes = [[],[],[],[]]
    fig, (ax1, ax2) = plt.subplots(1, 2)
    plt.setp(ax2.get_yticklabels(), visible=False)
    # plt.setp(ax2.get_xticklabels(), visible=True)
    ax1.set(xlabel='Year', ylabel='Mean salary income €/year')
    ax2.set(xlabel='Year')
    for f in [file_men, file_men_old, file_women, file_women_old]:
        with open(f, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            next(csvfile)
            next(csvfile)
            next(csvfile)
            for row in spamreader:
                new = row[2:]
                incomes[i] = list(map(int, new))
            # print(incomes[i])
            years_inner = list(map(int, np.linspace(2014, 2024, 11)))
            title = 'Men combined' if i == 0 else 'Men 50-64' if i == 1 else 'Women combined' if i == 2 else 'Women 50-64'
            color = cmap_colors_men[0] if i == 0 else cmap_colors_men[1] if i == 1 else cmap_colors_women[0] if i == 2 else cmap_colors_women[1]
            marker = '.-' if i % 2 == 0 else '-'
            axis = ax1 if i < 2 else ax2
            years = list(map(int, np.linspace(2014, 2024, 11)))
            axis.plot(years_inner, incomes[i], marker, color=color, markeredgewidth=2, label=title)
            # print(years)
            axis.legend()
            axis.grid(linestyle='dashed', color='gainsboro')
            label = 'Men' if i < 2 else 'Women'
            axis.set_title(label)
            # axis.xlabel('Year')
            # axis.axis((2014, 2024, 0, 30000))
            axis.axes.set_ylim(0, 45000)
            axis.set_facecolor('whitesmoke')
        i += 1
    plt.show()

    return

if __name__ == '__main__':
    # plot_data_two('task_2_data.csv', 'task_2_data_men.csv', 'task_2_data_all.csv')
    plot_data_one('task_1_data.csv')
    # plot_data_three('task_3_1_data.csv', 'task_3_2_data.csv', 'task_3_3_data.csv', 'task_3_4_data.csv')
