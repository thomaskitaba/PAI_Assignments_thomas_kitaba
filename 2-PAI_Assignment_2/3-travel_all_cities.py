#!/usr/bin/python3
import random
from collections import deque

def traverse_all_cities(cities, roads, start_city, strategy, adversary):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
    def fill_path(visited, total_distance, strategy):
        """
        Parameters:
        - visited: List of visited cities.
        - total_distance: The total distance traveled.
        - strategy: The traversal strategy used.
        """
        if visited not in [path.get(strategy) for path in all_paths]:
            
            data = {}
            data[f"{strategy}"] = list(visited)
            data["with cost"] = total_distance
            all_paths.append(data)
    
            
    # Depth First Search            
    def dfs(city, path, distance):
        """
        Depth-First Search (DFS) traversal of the graph.
        Parameters:
        - city: The current city.
        - path: The traversal path.
        - distance: The total cost (distance) of the traversal.
        """
        if city == adversary:
            return
        if city not in path:
            path.append(city)
        else:
            return
        
        for c, neighbor in roads.get(city, []):
            # if the road has weight use it else use 1 as defaul
            value = neighbor if neighbor else 1
            dfs(c, path, distance + value)     
        # add path to all_path list
        fill_path(path, distance, strategy)
        path.pop()   # remove city from the path so as to chang other path
    
    # Breadth First Search
    def bfs(start, path, distance):
        """
        Breadth-First Search (BFS) traversal of the graph.
        Parameters:
        - city: The current city.
        - path: The traversal path
        - cost: The total cost (distance) of the traversal.
        """
        print(f"{strategy} unweighted")
        
        # create a queue to hold node information
        queue = deque([[start, distance, path]])
        # loop until queue is empty to do a level order search
        while queue:
            #
            current_city, cost, path = queue.popleft()
            
            if current_city not in path:
                path.append(current_city)
            else:
                # print(f"Goal {current_city} found with cost {cost}")
                data = {}
                data[f"{strategy}"] = list(path)
                data["with cost"] = cost
                all_paths.append(data)
                print(data)
            
            # now do a level order traversal using for loop
            for neigbor, distance in roads.get(current_city, []): # unpack city and 
                # if the city has adversary then dont go through that city
                if neigbor == adversary:
                    continue
                if neigbor not in path:
                    value = distance if distance else 1
                    # add negibor to queue if its is in visited earlier
                    queue.append([neigbor, cost + value, path + [neigbor]])
        return all_paths
            
    if strategy.lower() == "dfs": 
        for start_city in cities:
            dfs(start_city, [], 0)
            
    elif strategy.lower() == "bfs":
        bfs(start_city, [], 0)
        
    return all_paths

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300), ('Hawassa', 100)]
}


start_city = "Addis Ababa"
strategy = "DFS"
all_paths = []
visited = set()
adversary = "Gondar"

result = traverse_all_cities(cities, roads, start_city, strategy, adversary)

for path in result:
    print(path)