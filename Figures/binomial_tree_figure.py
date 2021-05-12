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
day_3_uuu = Node(6, 3, 13, 0.125)
day_3_uud = Node(7, 3, 11, 0.375)
day_3_udd = Node(8, 3, 9, 0.375)
day_3_ddd = Node(9, 3, 7, 0.125)
day_4_uuuu = Node(10, 4, 14, 0.0625)
day_4_uuud = Node(11, 4, 12, 0.25)
day_4_uudd = Node(12, 4, 10, 0.375)
day_4_uddd = Node(13, 4, 8, 0.25)
day_4_dddd = Node(14, 4, 6, 0.0625)

tree = [day_0, day_1_u, day_1_d, day_2_uu, day_2_ud, day_2_dd, day_3_uuu, day_3_uud, day_3_udd, day_3_ddd, day_4_uuuu, day_4_uuud, day_4_uudd, day_4_uddd, day_4_dddd]

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
for i in tree[0:10]:
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


# Add rectangles
width = 0.5
height = 0.5

n = 0
binomial_tree_prices = ['$S_0$','$S_0 u$','$S_0 d$','$S_0 u^2$','$S_0 u d$','$S_0 d^2$','$S_0 u^3$','$S_0 u^2 d$','$S_0 u d^2$','$S_0 d^3$','$S_0 u^4$','$S_0 u^3 d$','$S_0 u^2 d^2$','$S_0 u d^3$','$S_0 d^4$']


for x,y in zip(day,price):
    ax.add_patch(mpatches.Rectangle(xy=(x-6*width/11, y-height/2), 
                width=width, 
                height=height, 
                linewidth=1, 
                color=colors))
    
for n in range(15):    
    ax.annotate(binomial_tree_prices[n], # this is the text
        (day[n],price[n]), # this is the point to label
        va='center',
        ha='center',
        c=colors_3,
        fontname=font,
        fontsize=12) # horizontal alignment can be left, right or center

    



# Plot the chart
ax.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)



plt.xticks(np.arange(0,5,1),[0,'t','2t','3t','4t'], fontname=font)
plt.yticks([])

start_day = datetime.today() - timedelta(days=4)
d1 = start_day.strftime("%B %d, %Y")
ax.set_xlabel('Time (t)', fontname=font, fontsize=18, weight='bold')
ax.set_ylabel('Price ($)', fontname=font, fontsize=18, weight='bold')
ax.set_title('4-Period Binomial Stock Price Tree', fontname=font, fontsize=20, weight='bold')

fig.tight_layout()

plt.show()