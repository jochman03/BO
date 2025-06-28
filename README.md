# Operations Research Projects

This repository contains a set of exercises and implementations developed as part of a course on **Operations Research**. The goal is to model and solve various optimization problems using mathematical programming techniques and Python.

## Contents

- ✅ Linear Programming (LP)  
- 🔢 Integer Programming (ILP, MILP)  
- 🌐 Network Flow Algorithms (max flow, min-cost flow)  
- 📅 Scheduling and Assignment Problems  
- 📈 Visualization of solutions and optimization processes  

## Technologies Used

- Python 3  
- NetworkX (graph algorithms)  
- Matplotlib (visualization)  
- NumPy

## Problem Descriptions

###  Lab 2 – Graph Algorithms: Representation and BFS  
Implemented graph representations (adjacency matrix and adjacency list) and performed Breadth-First Search (BFS) to explore reachable nodes from a given starting point. Used Python data structures and visualized traversal steps.

###  Lab 3 – Minimum Spanning Tree: Dijkstra-Prims Algorithm (DPA)  
Constructed a Minimum Spanning Tree (MST) using a variation of Prim's algorithm often referred to as Dijkstra-Prims Algorithm (DPA). Implemented on weighted undirected graphs and compared tree costs. Focused on maintaining a priority queue and updating the MST incrementally.

### Lab 4 – A* Search Algorithm
Implemented the A* pathfinding algorithm on graph structures. Used heuristic functions to guide the search and optimized traversal from source to target. Compared path costs and explored impact of heuristic accuracy.

### Lab 6 – Traveling Salesman Problem (G-TSP)
Implemented a greedy algorithm for the Generalized Traveling Salesman Problem (G-TSP). The algorithm sorts all edges by increasing weight and adds them one by one, ensuring that no cycles are formed during the construction of the tour.

### Lab 7 – PERT Algorithm
Implemented the Program Evaluation and Review Technique (PERT) for project scheduling. Modeled tasks as edges and events as vertices to compute earliest and latest start times, detect critical paths, and visualize project timelines.