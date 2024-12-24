#!/usr/bin/python3
import random
from collections import deque

def traverse_all_cities(cities, roads, start_city, strategy):
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
            # all_paths.append(list(visited))
    def dfs(city, path, distance):
        """
        Depth-First Search (DFS) traversal of the graph.
        Parameters:
        - city: The current city.
        - path: The traversal path.
        - cost: The total cost (distance) of the traversal.
        """
        if city not in path:
            path.append(city)
        else:
            return
        if city == "Gondar":
            return
        for c, neighbor in roads.get(city, []):
            print(f"c={c}    neighbor={neighbor}")
            value = neighbor if neighbor else 1
            print(c)
            dfs(c, path, distance + value)     
        fill_path(path, distance, strategy)
        # visited.remove(city)
        path.pop()   # remove city from the path so as to chang other path
    
    def bfs(city, path, cost):
        """
        Breadth-First Search (BFS) traversal of the graph.
        Parameters:
        - city: The current city.
        - path: The traversal path
        - cost: The total cost (distance) of the traversal.
        """
        print("BFS")
        path = []
        
        queue = deque([[city, 0, path]])
        print(queue)
        n = len(roads.keys())
        visited = set()
        
        while queue:
            # Code goes here    
            current_node, cost, path = queue.popleft()
            
            visited.add(current_node)
            path.append(current_node)
            # visit negbors of current_node
            for c, negbor in roads.get(current_node, []):
                print(f"c={c}    neighbor={negbor}")
                if negbor not in visited:
                    value = negbor if negbor else 1
                    print(negbor)
                    visited.add(negbor)
                    queue.append([c, cost + value, path + [negbor]])
            print(path)
        return None
        
    if strategy.lower() == "dfs": 
        for start_city in cities:
            dfs(start_city, [], 0)
            
    elif strategy.lower() == "bfs":
        bfs(start_city, [], 0)

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

start_city = "Addis Ababa"
strategy = "BFS"
all_paths = []
visited = set()
danger = "Gondar"
traverse_all_cities(cities, roads, start_city, strategy)
print(all_paths)


