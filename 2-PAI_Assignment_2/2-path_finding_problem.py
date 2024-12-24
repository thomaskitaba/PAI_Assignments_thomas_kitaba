#!/usr/bin/python3
import random 
from collections import deque

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
            visited.remove(start)
            rec_path.pop()  # go one step back in your path
            # visited.add(start)
            return # Backtrack
        
        for neigbors in roads.get(start, []):
            
            value = neigbors[1] if len(neigbors) == 2 else 1 # if we have no weight we use 1 as number of road
            dfs(neigbors[0], goal, rec_path, value + distance)
        visited.remove(start)
        rec_path.pop()
    
    def bfs(start, goal, path, distance):
        print(f"{strategy} unweighted")
        queue = deque([[start, distance, path]])
      
        while queue:
            current_city, cost, path = queue.popleft()
            # print(f"Popped = {current_city}")
            # just in case check if poped item is in visited
            if current_city not in visited:
                visited.add(current_city)
                path.append(current_city)
            # print(path)
            if current_city == goal:
                # print(f"Goal {current_city} found with cost {cost}")
                data = {}
                data[f"{strategy}"] = list(path)
                data["with cost"] = cost
                all_paths.append(data)
                return all_paths
            # now do a level order traversal using for loop
            for neigbor, distance in roads.get(current_city, []):  # unpack city and 
                # print(f" neigbor={neigbor} distance={distance}")
                if neigbor not in visited:
                    value = distance if distance else 1
                    visited.add(neigbor)
                    queue.append([neigbor, cost + value, path + [neigbor]])
            
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
    
    'Mekelle': [('Gondar', 300), ('Hawassa', 275)]
}

# select random city
start_city = cities[random.randint(0, len(cities) - 1)]
goal_city = cities[random.randint(0, len(cities) - 1)]

start_city = "Addis Ababa"
goal_city = "Hawassa"


strategy = "DFS"
# initialize all_paths list and visited set
all_paths = []
visited = set()

# find shortest path from start to goal city using uninformed search
uninformed_path_finder(cities, roads, start_city, goal_city, strategy)

# Print all possible paths and shortest path among those paths
print("====================================")
print("All Paths")
print(all_paths)
print("====================================")
print("Shortest Path")
if all_paths:
    shortest_path = [path for path in all_paths if path["with cost"] == min(list(d["with cost"] for d in all_paths)) ]
    print(shortest_path)
    print("====================================")
else:
    print("No Path found")

# print(f'visited: {visited}')
