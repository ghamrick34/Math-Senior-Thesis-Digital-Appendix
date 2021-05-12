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
day_2_uu = Node(3, 2, 12, 0.25)
day_2_ud = Node(4, 2, 10, 0.5)
day_2_dd = Node(5, 2, 8, 0.25)

tree = [day_0, day_1_u, day_1_d, day_2_uu, day_2_ud, day_2_dd]

fig,ax = plt.subplots()

day = [i.day for i in tree]
price = [i.price for i in tree]
scale = 150
colors = 'dimgray'
colors_2 = 'darkgrey'
colors_3 = 'white'
colors_4 = 'black'
marker = '.'
font = 'cmr10'

# Add arrows
for i in tree[0:3]:
    x_tail = i.day+0.25
    y_tail_u = i.price+0.25
    y_tail_d = i.price-0.25
    x_head = i.day + 0.7
    y_head_u = i.price+0.85
    y_head_d = i.price-0.85
    dx = x_head - x_tail
    arrow_u = mpatches.FancyArrowPatch((x_tail, y_tail_u),(x_head, y_head_u), mutation_scale=15, zorder=1, color=colors_2)
    arrow_d = mpatches.FancyArrowPatch((x_tail, y_tail_d),(x_head, y_head_d), mutation_scale=15, zorder=1, color=colors_2)
    ax.add_patch(arrow_u)
    ax.add_patch(arrow_d)

    ax.annotate(r'$ \times 1.10195$', # this is the text
        (x_tail+0.13,y_tail_u+0.5), # this is the point to label
        va='center',
        ha='center',
        c=colors,
        fontname=font,
        fontsize=10)

    ax.annotate(r'$ \times 0.9221$', # this is the text
        (x_tail+0.13,y_tail_d-0.5), # this is the point to label
        va='center',
        ha='center',
        c=colors,
        fontname=font,
        fontsize=10)


# Add rectangles
width = 0.5
height = 0.5

n = 0
binomial_tree_prices = ['$27.44','$30.24','$25.30','$33.32','$27.88','$23.33']


for x,y in zip(day,price):
    ax.add_patch(mpatches.Rectangle(xy=(x-6*width/11, y-height/2), 
                width=width, 
                height=height, 
                linewidth=1, 
                color=colors))
    
for n in range(6):    
    ax.annotate(binomial_tree_prices[n], # this is the text
        (day[n]-6*width/11+width/2,price[n]-height/2+height/2), # this is the point to label
        va='center',
        ha='center',
        c=colors_3,
        fontname=font,
        fontsize=12) # horizontal alignment can be left, right or center

    



# Plot the chart
ax.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)



plt.xticks(np.arange(0,3,1),['Day 6','Day 7', 'Day 8'], fontname=font)
plt.yticks([])

start_day = datetime.today() - timedelta(days=4)
d1 = start_day.strftime("%B %d, %Y")
ax.set_xlabel('Time (t)', fontname=font, fontsize=18, weight='bold')
ax.set_ylabel('Price ($)', fontname=font, fontsize=18, weight='bold')
ax.set_title('Boeing (BA) Stock Price Prediction', fontname=font, fontsize=20, weight='bold')

fig.tight_layout()

plt.show()