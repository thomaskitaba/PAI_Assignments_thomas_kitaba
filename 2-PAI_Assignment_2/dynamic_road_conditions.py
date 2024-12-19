#!/usr/bin/python3
import random 
from collections import deque
import sys
def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city (for specific tasks).
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the path from start_city to goal_city. (=BFS Path: ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle'] with cost 990.=)
    
    - cost: Total cost (number of steps or distance) of the path.
    """
    

    def dfs(start, goal, rec_path, distance):
        if start not in rec_path:
            rec_path.append(start)
        if start in visited:
            return # backtrack : avoid revisiting visited nodes
        
        visited.add(start)
        if start == goal:
            info = {}
            info[f"{strategy} Path"] = list(rec_path)
            info["with cost"] = distance
            all_paths.append(info)
            rec_path.pop()  # go one step back in your path
            visited.remove(start)
            return # Backtrack
        
        for neigbors in roads.get(start, []):
            
            value = neigbors[1] if len(neigbors) == 2 else 1 # if we have no weight we use 1 as number of road
            dfs(neigbors[0], goal, rec_path, value + distance)
        visited.remove(start) 
        rec_path.pop()
    
    def bfs(stat, end, path, distance):
        print(f"{strategy} unweighted")
        
    if strategy == "DFS":
        dfs(start_city, goal_city, [], 0)
        
    if strategy == "BFS":
        bfs(start_city, goal_city, [], 0)
    
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300), ("Hawassa", 100)]
}

# select random city

if __name__ == "__main__":
        
    start_city = "Mekelle"
    goal_city = "Hawassa"

    print(f'{start_city} to {goal_city}')
    strategy = "DFS"
    # initialize all_paths list and visited set
    all_paths = []
    visited = set()

    # find shortest path from start to goal city using uninformed search
    uninformed_path_finder(cities, roads, start_city, goal_city, strategy)
    # get the shortest path among all the other paths
    sorted_all_paths = sorted(all_paths, key=lambda x: x["with cost"])

    i = eval(sys.argv[1])
    k = len(all_paths) if i > len(all_paths) else i
    
    if i > len(all_paths):
        print("Usage: provide interger for number of shortest paths")
        print("all shortes pathers are")
    print(f"k = {k} shortest paths")
    for i in range(k):
        print(sorted_all_paths[i])


