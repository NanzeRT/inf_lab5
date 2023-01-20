import matplotlib as mpl
import matplotlib.pyplot as plt
import random

import csv

with open('data.csv') as file:  
    reader = csv.reader(file, delimiter=",", quotechar='"')
    next(reader, None)
    data_read = [row for row in reader]

opens: dict[str, list[int]] = {}
highs = {}
lows = {}
closes = {}

for raw in data_read:
    if raw[2] not in opens:
        opens[raw[2]] = []
        highs[raw[2]] = []
        lows[raw[2]] = []
        closes[raw[2]] = []
    opens[raw[2]].append(float(raw[4]))
    highs[raw[2]].append(float(raw[5]))
    lows[raw[2]].append(float(raw[6]))
    closes[raw[2]].append(float(raw[7]))

fig, ax = plt.subplots()

patches = []
# generate list of many colors
colors = []
for name, hex in mpl.colors.cnames.items():
    colors.append(name)

for i, date in enumerate(opens):
    # use random colors from list
    open_color = random.choice(colors)
    colors.remove(open_color)
    high_color = random.choice(colors)
    colors.remove(high_color)
    low_color = random.choice(colors)
    colors.remove(low_color)
    close_color = random.choice(colors)
    colors.remove(close_color)
    # create patches for legend (including dates)
    patches.append(mpl.patches.Patch(color=open_color, label=date + ' - Open'))
    patches.append(mpl.patches.Patch(color=high_color, label=date + ' - High'))
    patches.append(mpl.patches.Patch(color=low_color, label=date + ' - Low'))
    patches.append(mpl.patches.Patch(color=close_color, label=date + ' - Close'))
    # plot boxplots
    ax.boxplot(opens[date], positions=[i*4], widths=0.5, patch_artist=True, boxprops=dict(facecolor=open_color))
    ax.boxplot(highs[date], positions=[i*4+1], widths=0.5, patch_artist=True, boxprops=dict(facecolor=high_color))
    ax.boxplot(lows[date], positions=[i*4+2], widths=0.5, patch_artist=True, boxprops=dict(facecolor=low_color))
    ax.boxplot(closes[date], positions=[i*4+3], widths=0.5, patch_artist=True, boxprops=dict(facecolor=close_color))

ax.legend(handles=patches, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True)
# show only every 4th xtick
ax.set_xticks([i*4 for i in range(len(opens))])
ax.set_xticklabels([date for date in opens])
plt.show()
