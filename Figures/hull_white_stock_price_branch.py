import matplotlib.pyplot as plt
import numpy as np
from Hull_White_class import Node
from datetime import datetime, timedelta
import matplotlib.patches as mpatches

# Change default font
plt.rcParams.update({'font.family':'cmr10'})

day_0 = Node(0, 0, 10, 1)
day_1_u = Node(1, 1, 11, 0.5)
day_1_d = Node(2, 1, 9, 0.5)


tree = [day_0, day_1_u, day_1_d]

fig,ax = plt.subplots()

day = [i.day for i in tree]
price = [i.price for i in tree]
scale = 150
colors = 'black'
colors_2 = 'darkgrey'
colors_3 = 'white'
colors_4 = 'black'
marker = '.'
font = 'cmr10'

# Add arrows
for i in tree[0:1]:
    x_tail = i.day
    y_tail = i.price
    x_head = i.day + 1
    y_head_u = i.price+1
    y_head_d = i.price-1
    dx = x_head - x_tail
    arrow_u = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_u), mutation_scale=15, zorder=1, color=colors_2)
    arrow_d = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_d), mutation_scale=15, zorder=1, color=colors_2)
    ax.add_patch(arrow_u)
    ax.add_patch(arrow_d)
    
# Plot the chart
ax.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)

    # Label each point with the price
ax.annotate('$u \cdot S_{k-1}$', # this is the text
    (1.05,11), # this is the point to label
    va='center',
    ha='left',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center

ax.annotate('$d \cdot S_{k-1}$', # this is the text
    (1.05,9), # this is the point to label
    va='center',
    ha='left',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center
    
ax.annotate('$S_{k-1}$', # this is the text
    (-0.05,10), # this is the point to label
    va='center',
    ha='right',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center

ax.annotate('1/2', # this is the text
    (0.5,10.75), # this is the point to label
    va='center',
    ha='center',
    c=colors_2,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center

ax.annotate('1/2', # this is the text
    (0.5,9.25), # this is the point to label
    va='center',
    ha='center',
    c=colors_2,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center

plt.xticks([0,1],['r','r + t'],fontsize=14)
plt.yticks([],[])


ax.set_xlim(-0.4,1.4)
ax.set_ylim(8.75,11.25)
ax.set_xlabel('Time (t)', fontname=font, fontsize=18, weight='bold')
ax.set_ylabel('Price ($)', fontname=font, fontsize=18, weight='bold')
ax.set_title('Hull-White Stock Price Branch', fontname=font, fontsize=28, weight='bold')


plt.tight_layout()
plt.show()