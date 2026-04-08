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

def plot_data(file) -> None:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvfile)
        plt.rcParams["font.family"] = "monospace"
        plt.rcParams["font.monospace"] = ["DejaVu Sans Mono"]
        cmap_colors = cmr.take_cmap_colors('cmr.arctic', 5, cmap_range=(0.2, 0.8), return_fmt='hex')    # CMasher 5 colors in hex
        # Let's do comparisons between Nordic countries: Denmark, Finland, Iceland, Norway and Sweden
        # Each has different year data as some years might be missing
        denmark = []
        denmark_yrs = []
        finland = []
        finland_yrs = []
        iceland = []
        iceland_yrs = []
        norway = []
        norway_yrs = []
        sweden = []
        sweden_yrs = []
        mean_temp = [ [] for _ in range(66) ]
        # 65 years so 0 = 1965, do a list of that
        mean_yrs = np.linspace(1960, 2025, 66)
        # print(mean_yrs)
        for row in spamreader:
            year = int(row[1])
            idx = year-1965
            mean_temp[idx].append(float(row[2]))
            match row[0]:
                case "Denmark":
                    denmark_yrs.append(year)
                    denmark.append(float(row[2]))
                case "Finland":
                    finland_yrs.append(year)
                    finland.append(float(row[2]))
                case "Iceland":
                    iceland_yrs.append(year)
                    iceland.append(float(row[2]))
                case "Norway":
                    norway_yrs.append(year)
                    norway.append(float(row[2]))
                case "Sweden":
                    sweden_yrs.append(year)
                    sweden.append(float(row[2]))
        mean = []
        i = 0
        for m in mean_temp:
            # print(i)
            mean.append(sum(m) / len(m))
            i += 1
        plt.grid()
        plt.ylabel('Gini index disposable')
        plt.xlabel('Year')
        plt.axis((1960, 2025, 0, 50))
        plt.title("Disposable incomes after tax and transfer by Gini")
        plt.gca().set_facecolor('whitesmoke')

        plt.plot(finland_yrs, finland, 'x-', markeredgewidth=2, color=cmap_colors[0], label='Finland')
        #plt.scatter(finland_yrs, finland, color='b')

        plt.plot(denmark_yrs, denmark, '-', color=cmap_colors[1], label='Denmark')
        #plt.scatter(denmark_yrs, denmark, color='orange')

        plt.plot(iceland_yrs, iceland, '-', color=cmap_colors[2], label='Iceland')
        #plt.scatter(iceland_yrs, iceland, color='turquoise')

        plt.plot(norway_yrs, norway, '-', color=cmap_colors[3], label='Norway')
        #plt.scatter(norway_yrs, norway, color='red')

        plt.plot(sweden_yrs, sweden, '-', color=cmap_colors[4], label='Sweden')
        #plt.scatter(sweden_yrs, sweden, color='yellow')

        plt.plot(mean_yrs, mean, 'o-', color='darkgray', label='Mean')
        #plt.scatter(mean_yrs, mean, color='gray')

        plt.legend()

        plt.show()

        return

if __name__ == '__main__':
    plot_data('swiid9_91_summary.csv')
