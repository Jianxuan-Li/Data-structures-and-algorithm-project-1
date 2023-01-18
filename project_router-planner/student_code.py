import math
import heapq

def euclidean_distance(n: (float, float), m: (float, float)) -> float:
    return math.hypot(m[0] - n[0], m[1] - n[1])

def path_cost(input_map, path):
    if len(path) < 2:
        return 0
    
    length = 0
    for i in range(1, len(path)):
        length += euclidean_distance(input_map.intersections[path[i]], input_map.intersections[path[i - 1]])
        
    return length

def shortest_path(input_map, start, end):
    # edge case
    if start == end:
        return [start]
    
    # the result paths, use the (weight, [point1, point2, ...]) to save paths.
    #  if the weight of a path is small, then it's a good path, so we choice it in every loop
    paths = []
    heapq.heappush(paths, (0, [start]))
    
    while len(paths):
        # get the shortest path
        p = heapq.heappop(paths)
        
        path = p[1] # current path
        frontier = p[1][-1] # current frontier
        
        # if this path is closed, return this path
        if frontier == end:
            return path
        
        # neighbours of frontier
        neighbours = input_map.roads[frontier]
        
        for n in neighbours:
            # ignore the loops or backwards
            if n in path:
                continue
                
            # copy current path, and add the frontier to it
            new_path = [x for x in path] + [n]
            
            # the heuristic distance
            h = euclidean_distance(input_map.intersections[end], input_map.intersections[n])
            
            # the path cost
            g = path_cost(input_map, new_path)
            
            # total score (weight)
            f = h + g
            
            # push to the heap queue, with weight
            heapq.heappush(paths, (f, new_path))

    return []