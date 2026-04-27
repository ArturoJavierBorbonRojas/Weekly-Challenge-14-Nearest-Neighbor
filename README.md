# Weekly-Challenge-14-Nearest-Neighbor
For Week 15, I integrated one of my Master's degree assignments into my weekly coding challenge. The goal was to solve the **Traveling Salesperson Problem (TSP)** using the **Nearest Neighbor** algorithm.

This is a classic **Greedy Algorithm**. Instead of calculating every possible permutation (which is computationally impossible for large datasets), the algorithm simply makes the locally optimal choice at each step: *go to the closest unvisited city*. 

While it doesn't guarantee the absolute shortest possible path, it provides a very fast and highly optimized route in a fraction of a second.

## ⚙️ How it works
1. **Initialization:** Start at a random node (in this case, Node 0).
2. **Evaluation:** Calculate the Euclidean distance $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ to all remaining unvisited nodes.
3. **Selection:** Pick the node with the shortest distance and move there.
4. **Iteration:** Repeat until the unvisited list is empty.
5. **Return:** Add the distance from the last node back to the starting node to complete the cycle.

## 🚀 Complexity Analysis
* **Time Complexity:** $O(V^2)$ where $V$ is the number of vertices (nodes). For every unvisited node, we must iterate through the remaining unvisited nodes to find the minimum distance.
* **Space Complexity:** $O(V)$ to store the list of nodes, the unvisited list, and the final route sequence.

## 🛠 Dependencies
* Python 3.14.3
* NumPy
* Matplotlib
* time
