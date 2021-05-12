import matplotlib.pyplot as plt
import numpy as np
import u_and_d_General as u_and_d
from Hull_White_class import Node
from datetime import datetime, timedelta
import matplotlib.patches as mpatches
import nodes as n

def plot(q, entry, real_life):
    u = u_and_d.u(q, entry, real_life)
    d = u_and_d.d(q, entry, real_life)

    
    tree_object = n.gen_tree(q, entry, real_life)

    tree = [
    tree_object.n0, 
    tree_object.n1, 
    tree_object.n2, 
    tree_object.n3, 
    tree_object.n4, 
    tree_object.n5, 
    tree_object.n6, 
    tree_object.n7, 
    tree_object.n8, 
    tree_object.n9, 
    tree_object.n10,
    tree_object.n11,
    tree_object.n12,
    tree_object.n13,
    tree_object.n14
    ]

    fig,ax = plt.subplots()

    day = [i.day for i in tree]
    price = [i.price for i in tree]
    #scale = [1000*abs(i.probability) for i in tree]
    scale = 150
    #colors = [i.probability for i in tree]
    colors = 'royalblue'
    colors_2 = 'grey'
    colors_3 = 'white'
    colors_4 = 'black'
    colors_5 = 'red'
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
        #dy_u = y_head_u - y_tail
        #dy_d = y_head_d - y_tail
        arrow_u = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_u), mutation_scale=15, zorder=1, color=colors_2)
        arrow_d = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_d), mutation_scale=15, zorder=1, color=colors_2)
        ax.add_patch(arrow_u)
        ax.add_patch(arrow_d)
        
    # Plot the chart
    ax.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)

    # Add rectangles
    width = 0.5
    height = (tree_object.n10.price-tree_object.n14.price)/15

    for x,y in zip(day,price):
        ax.add_patch(mpatches.Rectangle(xy=(x-width/2, y-height/2+(tree_object.n1.price-tree_object.n0.price)/2), 
                    width=width, 
                    height=height, 
                    linewidth=1, 
                    color=colors))

    # Zip joins x and y coordinates in pairs
    for x,y in zip(day,price):

        label = "{:.2f}".format(y)

        # Label each point with the price
        ax.annotate(label, # this is the text
                    (x,y+(tree_object.n1.price-tree_object.n0.price)/2), # this is the point to label
                    va='center',
                    ha='center',
                    c=colors_3,
                    fontname=font) # horizontal alignment can be left, right or center

    # Expected value plot
    real_life_data_day = [0,1,2,3,4]
    day_0_ev = tree[0].price
    day_1_ev = (sum(tree[i].price*tree[i].probability for i in range(1,3)))
    day_2_ev = (sum(tree[i].price*tree[i].probability for i in range(3,6)))
    day_3_ev = (sum(tree[i].price*tree[i].probability for i in range(6,10)))
    day_4_ev = (sum(tree[i].price*tree[i].probability for i in range(10,15)))

    ev = [day_0_ev,day_1_ev,day_2_ev,day_3_ev,day_4_ev]
    print(ev)
    x = np.array(real_life_data_day)
    y = np.array(ev)
    m, b = np.polyfit(x, y, 1)
    print(m)
    ax.scatter(real_life_data_day,ev, s=scale, c=colors_5, marker="", zorder=2)
    ax.plot(x, m*x + b, c=colors_5)
    label2 = str(round(m,3)) + "(x)+ " + str(round(b,2))
    print(label2)
    ax.annotate(label2, # this is the text
                    (0.5,(tree_object.n14.price)), # this is the point to label
                    va='center',
                    ha='center',
                    c=colors_5,
                    fontname=font) # horizontal alignment can be left, right or center


    label3 = "q = " + str(q)
    ax.annotate(label3, # this is the text
                    (2,tree_object.n14.price), # this is the point to label
                    va='center',
                    ha='center',
                    c=colors,
                    fontname=font) # horizontal alignment can be left, right or center

    # Real-life data

    real_life_data_price = [real_life[i] for i in range(5,10)]

    # Plot real-life data as a line plot
    ax.plot(real_life_data_day,real_life_data_price, c=colors_4, zorder=4)


    plt.xticks(np.arange(0,5,1))

    stock = entry.upper()
    start_day = datetime.today() - timedelta(days=4)
    d1 = start_day.strftime("%B %d, %Y")
    ax.set_xlabel('Days', fontname=font, weight='bold')
    ax.set_ylabel('Price ($)', fontname=font, weight='bold')
    ax.set_title(stock + ' Predicted Close Price Over Time', fontname=font, weight='bold')

    fig.tight_layout()
    plt.show()

def plot_no_fitting(q, entry, real_life):
    u = u_and_d.u(q, entry, real_life)
    d = u_and_d.d(q, entry, real_life)

    
    tree_object = n.gen_tree(q, entry, real_life)

    tree = [
    tree_object.n0, 
    tree_object.n1, 
    tree_object.n2, 
    tree_object.n3, 
    tree_object.n4, 
    tree_object.n5, 
    tree_object.n6, 
    tree_object.n7, 
    tree_object.n8, 
    tree_object.n9, 
    tree_object.n10,
    tree_object.n11,
    tree_object.n12,
    tree_object.n13,
    tree_object.n14
    ]

    fig,ax = plt.subplots()

    day = [i.day for i in tree]
    price = [i.price for i in tree]
    #scale = [1000*abs(i.probability) for i in tree]
    scale = 150
    #colors = [i.probability for i in tree]
    colors = 'royalblue'
    colors_2 = 'grey'
    colors_3 = 'white'
    colors_4 = 'black'
    colors_5 = 'red'
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
        #dy_u = y_head_u - y_tail
        #dy_d = y_head_d - y_tail
        arrow_u = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_u), mutation_scale=15, zorder=1, color=colors_2)
        arrow_d = mpatches.FancyArrowPatch((x_tail, y_tail),(x_head, y_head_d), mutation_scale=15, zorder=1, color=colors_2)
        ax.add_patch(arrow_u)
        ax.add_patch(arrow_d)
        
    # Plot the chart
    ax.scatter(day,price, s=scale, c=colors, marker=marker, zorder=2)

    # Add rectangles
    width = 0.5
    height = (tree_object.n10.price-tree_object.n14.price)/15

    for x,y in zip(day,price):
        ax.add_patch(mpatches.Rectangle(xy=(x-width/2, y-height/2+(tree_object.n1.price-tree_object.n0.price)/2), 
                    width=width, 
                    height=height, 
                    linewidth=1, 
                    color=colors))

    # Zip joins x and y coordinates in pairs
    for x,y in zip(day,price):

        label = "{:.2f}".format(y)

        # Label each point with the price
        ax.annotate(label, # this is the text
                    (x,y+(tree_object.n1.price-tree_object.n0.price)/2), # this is the point to label
                    va='center',
                    ha='center',
                    c=colors_3,
                    fontname=font) # horizontal alignment can be left, right or center

    # Expected value plot
    real_life_data_day = [0,1,2,3,4]


    label3 = "q = " + str(q)
    ax.annotate(label3, # this is the text
                    (2,(tree_object.n9.price+tree_object.n14.price)/2), # this is the point to label
                    va='center',
                    ha='center',
                    c=colors,
                    fontname=font) # horizontal alignment can be left, right or center

    # Real-life data

    real_life_data_price = [real_life[i] for i in range(5,10)]

    # Plot real-life data as a line plot
    ax.plot(real_life_data_day,real_life_data_price, c=colors_4, zorder=4)


    plt.xticks(np.arange(0,5,1))

    stock = entry.upper()
    start_day = datetime.today() - timedelta(days=4)
    d1 = start_day.strftime("%B %d, %Y")
    ax.set_xlabel('Days', fontname=font, weight='bold')
    ax.set_ylabel('Price ($)', fontname=font, weight='bold')
    ax.set_title(stock + ' Predicted Close Price Over Time', fontname=font, weight='bold')

    fig.tight_layout()
    plt.show()
