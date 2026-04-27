import numpy as np
import matplotlib.pyplot as plt
import time

# Weekly Challenge 14: Nearest Neighbor
# Author: Ing. Arturo Javier Borbon Rojas

# start time
start_time= time.time()

# 1 We generate random nodes
n= 20
nodes= np.random.rand(n,2)*100

print(f"Starting Nearest Neighbor for {nodes} nodes")
print("-"*40)

# 2 Nearest Neighbor Algorithm
# We start at node 0
unvisited= list(range(1, n))
current_node=0
route=[current_node]
total_distance=0.0

# 2.1 Loop until all nodes are visited
while unvisited:
    nearest_neighbor = None
    min_distance= float("inf")

    # 2.2 Check distance to all unvisited nodes
    for candidate in unvisited:
        dist= np.linalg.norm(nodes[current_node]-nodes[candidate])

        # 2.3 Keep track of the closest one
        if dist < min_distance:
            min_distance= dist
            nearest_neighbor= candidate

        # move to the nearest neighbor
    route.append(nearest_neighbor)
    total_distance += min_distance
    unvisited.remove(nearest_neighbor)
    current_node= nearest_neighbor
    
# 3 return to the starting point to clase the cycle
return_distance= np.linalg.norm(nodes[current_node]-nodes[route[0]])
total_distance += return_distance
route.append(route[0])

print(f"Route calculation complete")
print(f"Node visit order {route}")
print(f"Total Distance Traveled: {total_distance} units")
print("-"*45)

# 4 Visualization with Matplotlib
plt.figure(figsize=(10,7))

# 4.1 Get X and Y coordinates in the order of the calculated route
route_x= [nodes[i][0] for i in route]
route_y= [nodes[i][1] for i in route]

# 4.2 Plot all nodes
plt.scatter(nodes[:,0], nodes[:,1], c="blue", s=80, label="Cities", zorder=5 )
plt.scatter(nodes[0][0], nodes[0][1], c="red", s=150, marker="*", label="Start/End", zorder=10)

# 4.3 Add labels to the nodes
for i, (x,y) in enumerate(nodes):
    plt.text(x +1, y+1, str(i), fontsize=10, fontweight="bold", color="darkred")


# 4.4 Draw the route using arrows to show direction
for i in range(len(route)-1):
    start_pos = nodes[route[i]]
    end_pos= nodes[route[i+1]]
    plt.annotate("",
               xy= end_pos, xycoords= "data",
               xytext= start_pos, textcoords="data",
               arrowprops=dict(arrowstyle= "->", color="gray", lw=1.5, alpha= 0.8))

# end time
end_time= time.time()

total_time= end_time-start_time
print(f"Process done in:{total_time} seconds")


plt.title(f"Nearest Neighbor {total_distance}")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, alpha= 0.3)
plt.show()



