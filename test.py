#!/usr/bin/python3
import random
from collections import deque
def bfs(start, goal, path, distance):
        print(f"{strategy} unweighted")
        queue = deque([[start, distance, path]])
        print(f"start: {start}  goal: {goal}  distance:{distance}")
        while queue:
            current_city, cost, path = queue.popleft()
            if current_city == adversary:
                continue
            if current_city not in path:
                # visited.add(current_city)
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
                # print(f" neigbor={neigbor} distance={distance}")
                # if neigbor == adversary:
                #     continue
                if neigbor not in path:
                    value = distance if distance else 1
                
                    queue.append([neigbor, cost + value, path + [neigbor]])
            
        return all_paths
    
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
adversary = "Gondar"


strategy = "BFS"
# initialize all_paths list and visited set
all_paths = []
visited = set()


print(bfs(start_city, goal_city, [], 0))
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

