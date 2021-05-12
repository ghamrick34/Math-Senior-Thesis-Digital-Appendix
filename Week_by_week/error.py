import matplotlib.pyplot as plt
import numpy as np
from Hull_White_class import Node
import matplotlib.patches as mpatches
import nodes as n

def error_fun(q, stock, real_life):
    # Predicted nodes
    tree_object = n.gen_tree(q, stock, real_life)

    tree = [tree_object.n0, 
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
    tree_object.n14]

    # Real-life data
    real_life_data_day = [0,1,2,3,4]
    real_life_data_price = [real_life[i] for i in range(5,10)]

    # Day 1 error
    day_1 = tree[1:3]
    error_day_1 = min([abs(real_life_data_price[1]-day_1[i].price) for i in range(2)])/real_life_data_price[1]
    #print(error_day_1)

    # Day 2 error
    day_2 = tree[3:6]
    error_day_2 = min([abs(real_life_data_price[2]-day_2[i].price) for i in range(3)])/real_life_data_price[2]
    #print(error_day_2)

    # Day 3 error
    day_3 = tree[6:10]
    error_day_3 = min([abs(real_life_data_price[3]-day_3[i].price) for i in range(4)])/real_life_data_price[3]
    #print(error_day_3)

    # Day 4 error
    day_4 = tree[10:15]
    error_day_4 = min([abs(real_life_data_price[4]-day_4[i].price) for i in range(5)])/real_life_data_price[4]
    #print(error_day_4)

    # Error set

    errors = [error_day_1, error_day_2, error_day_3, error_day_4]
    total_error = sum(errors)
    #print(total_error)

    return total_error