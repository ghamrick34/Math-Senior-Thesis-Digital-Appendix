import numpy as np
import u_and_d_General as u_and_d
from Hull_White_class import Node
from datetime import datetime, timedelta
import nodes as n

def slope(q, entry, real_life):

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

    # Expected value plot
    real_life_data_day = [0,1,2,3,4]
    day_0_ev = tree[0].price
    day_1_ev = (sum(tree[i].price*tree[i].probability for i in range(1,3)))
    day_2_ev = (sum(tree[i].price*tree[i].probability for i in range(3,6)))
    day_3_ev = (sum(tree[i].price*tree[i].probability for i in range(6,10)))
    day_4_ev = (sum(tree[i].price*tree[i].probability for i in range(10,15)))

    ev = [day_0_ev,day_1_ev,day_2_ev,day_3_ev,day_4_ev]
    x = np.array(real_life_data_day)
    y = np.array(ev)
    m, b = np.polyfit(x, y, 1)
    
    scaled_m = m/day_0_ev

    return scaled_m, day_4_ev
