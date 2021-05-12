import matplotlib.pyplot as plt
import numpy as np
from Hull_White_class import Node
from datetime import datetime, timedelta
import matplotlib.patches as mpatches

day_0 = Node(0, 0, 10, 1)
day_1_u = Node(1, 1, 11, 0.5)
day_1_d = Node(2, 1, 9, 0.5)

# Change default font
plt.rcParams.update({'font.family':'cmr10'})

tree = [day_0, day_1_u, day_1_d]

fig, [ax1, ax2] = plt.subplots(1,2, sharex=True, sharey=True)

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
    ax1.add_patch(arrow_u)
    ax1.add_patch(arrow_d)
    
# Plot the chart
ax1.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)

    # Label each point with the price
ax1.annotate('$U = S_u - X$', # this is the text
    (1.2,11), # this is the point to label
    va='center',
    ha='left',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center

ax1.annotate('$D=0$', # this is the text
    (1.2,9), # this is the point to label
    va='center',
    ha='left',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center
    
ax1.annotate('$V_0$', # this is the text
    (-0.2,10), # this is the point to label
    va='center',
    ha='center',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center



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
    ax2.add_patch(arrow_u)
    ax2.add_patch(arrow_d)

# Plot the chart
ax2.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)

    # Label each point with the price
ax2.annotate('$U=0$', # this is the text
    (1.2,11), # this is the point to label
    va='center',
    ha='left',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center

ax2.annotate('$D=X-S_d$', # this is the text
    (1.2,9), # this is the point to label
    va='center',
    ha='left',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center
    
ax2.annotate('$V_0$', # this is the text
    (-0.2,10), # this is the point to label
    va='center',
    ha='center',
    c=colors,
    fontname=font,
    fontsize=20) # horizontal alignment can be left, right or center



plt.xticks([0,1],[0,'t'], fontname=font)
plt.yticks([],[])



ax1.set_xlim(-0.4,2.5)
ax1.set_ylim(8.5,11.5)
ax1.set_xlabel('Time (t)', fontname=font, fontsize=18, weight='bold')
## ax1.set_ylabel('Value ($)', fontname=font, fontsize=18, weight='bold')
ax1.set_title('Call Option Value Tree', fontname=font, fontsize=20, weight='bold')

ax2.set_xlabel('Time (t)', fontname=font, fontsize=18, weight='bold')
## ax2.set_ylabel('Value ($)', fontname=font, fontsize=18, weight='bold')
ax2.set_title('Put Option Value Tree', fontname=font, fontsize=20, weight='bold')


plt.tight_layout()
plt.show()