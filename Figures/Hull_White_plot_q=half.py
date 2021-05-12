import matplotlib.pyplot as plt
import numpy as np
import u_and_d_Hull_White as u_and_d
import fetch
from Hull_White_class import Node
from datetime import datetime, timedelta
import matplotlib.patches as mpatches

u = u_and_d.u()
d = u_and_d.d()

day_0 = Node(0, 0, fetch.close_data()[-5], 1)
day_1_u = Node(1, 1, day_0.price * u, 0.5)
day_1_d = Node(2, 1, day_0.price * d, 0.5)
day_2_uu = Node(3, 2, day_1_u.price * u, 0.25)
day_2_ud = Node(4, 2, day_1_u.price * d, 0.5)
day_2_dd = Node(5, 2, day_1_d.price * d, 0.25)
day_3_uuu = Node(6, 3, day_2_uu.price * u, 0.125)
day_3_uud = Node(7, 3, day_2_uu.price * d, 0.375)
day_3_udd = Node(8, 3, day_2_ud.price * d, 0.375)
day_3_ddd = Node(9, 3, day_2_dd.price * d, 0.125)
day_4_uuuu = Node(10, 4, day_3_uuu.price * u, 0.0625)
day_4_uuud = Node(11, 4, day_3_uuu.price * d, 0.25)
day_4_uudd = Node(12, 4, day_3_uud.price * d, 0.375)
day_4_uddd = Node(13, 4, day_3_udd.price * d, 0.25)
day_4_dddd = Node(14, 4, day_3_ddd.price * d, 0.0625)

tree = [day_0, day_1_u, day_1_d, day_2_uu, day_2_ud, day_2_dd, day_3_uuu, day_3_uud, day_3_udd, day_3_ddd, day_4_uuuu, day_4_uuud, day_4_uudd, day_4_uddd, day_4_dddd]

fig,ax = plt.subplots()

day = [i.day for i in tree]
price = [i.price for i in tree]
scale = 150
colors = 'royalblue'
colors_2 = 'grey'
colors_3 = 'white'
colors_4 = 'black'
marker = '.'
font = 'Tahoma'

# Add arrows
for i in tree[0:10]:
    x_tail = i.day
    y_tail = i.price
    x_head = i.day + 1
    y_head_u = i.price * u
    y_head_d = i.price * d
    dx = x_head - x_tail
    arrow_u = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_u), mutation_scale=15, zorder=1, color=colors_2)
    arrow_d = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_d), mutation_scale=15, zorder=1, color=colors_2)
    ax.add_patch(arrow_u)
    ax.add_patch(arrow_d)
    
# Plot the chart
ax.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)

# Add rectangles
width = 0.5
height = (day_4_uuuu.price-day_4_dddd.price)/15

for x,y in zip(day,price):
    ax.add_patch(mpatches.Rectangle(xy=(x-width/2, y-height/2+(day_1_u.price-day_0.price)/2), 
                width=width, 
                height=height, 
                linewidth=1, 
                color=colors))

# Zip joins x and y coordinates in pairs
for x,y in zip(day,price):

    label = "{:.2f}".format(y)

    # Label each point with the price
    ax.annotate(label, # this is the text
                 (x,y+(day_1_u.price-day_0.price)/2), # this is the point to label
                 va='center',
                 ha='center',
                 c=colors_3,
                 fontname=font) # horizontal alignment can be left, right or center



# Real-life data
real_life_data_day = [0,1,2,3,4]
real_life_data_price = [(fetch.close_data()[i-5]) for i in range(5)]

# Plot real-life data as a line plot
ax.plot(real_life_data_day,real_life_data_price, c=colors_4, zorder=4)


plt.xticks(np.arange(0,5,1))

stock = fetch.stock()
start_day = datetime.today() - timedelta(days=4)
d1 = start_day.strftime("%B %d, %Y")
ax.set_xlabel('Days past ' + d1, fontname=font, weight='bold')
ax.set_ylabel('Price ($)', fontname=font, weight='bold')
ax.set_title(stock + ' Predicted Close Price Over Time', fontname=font, weight='bold')

fig.tight_layout()

plt.show()