import fetch
from nodes import gen_tree
from Hull_White_plot_General_q import plot
from error import error

stock = "plug"

possible_q = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
errors = []

for i in possible_q:
    errors.append([i,error(i, stock)])

optimized_q = min(errors, key = lambda t: t[1])

print(optimized_q)
plot(optimized_q[0],stock)

#plot(0.5, "plug")
#percent_error(0.5, "plug")