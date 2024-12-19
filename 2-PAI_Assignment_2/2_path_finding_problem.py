#!/usr/bin/python3
import random
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
            return 
        if start == goal:
            info = {}
            info[f"{strategy} Path"] = list(rec_path)
            info["with cost"] = distance
            all_paths.append(info)
            rec_path.pop()  # go one step back in your path
            return
        visited.add(start)
        for neigbors in roads.get(start):
            dfs(neigbors[0], goal, rec_path, neigbors[1] + distance)
        rec_path.pop()
    
    def bfs(stat, end, path, distance):
        print("bfs selected")
        
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
    'Mekelle': [('Gondar', 300)]
}

random_index = random.randint(0, len(cities) - 1)
print(random_index)
start_city = cities[random_index]
goal_city = "Bahir Dar"
strategy = "DFS"
all_paths = []
visited = set()

# find shortest path from start to goal city using uninformed search
uninformed_path_finder(cities, roads, start_city, goal_city, strategy)
shortest_path = [path for path in all_paths if path["with cost"] == min(list(d["with cost"] for d in all_paths)) ]
print(shortest_path)

