from nodes import gen_tree
from Hull_White_plot_General_q import plot
from error import error

companies = ["bp","xom","oxy","pxd"]
#companies = ["run","cwen","fslr","nee"]

possible_q = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
errors_by_q = []

for i in possible_q:
    error_for_group = 0
    for stock in companies:
        error_for_group = error_for_group + error(i, stock)
    
    errors_by_q.append([i,error_for_group])

optimized_q = min(errors_by_q, key = lambda t: t[1])

print(errors_by_q,optimized_q)

# for i in range(len(companies)):
#     plot(optimized_q[0],companies[i])

#plot(0.5, "plug")
#percent_error(0.5, "plug")