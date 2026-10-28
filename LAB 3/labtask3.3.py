import heapq
from collections import deque
graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 5), ("E", 1)],
    "C": [("F", 4), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}
def ucs(start, goal):
    priority_queue = [(0, start, [start])]
    best_cost = {start: 0}
    processed = []
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if cost != best_cost.get(node):
            continue
        processed.append((node, cost))
        if node == goal:
            return path, cost, processed
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, path + [neighbor])
                )
    return None, float("inf"), processed
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None
def calculate_cost(path):
    total = 0
    for a, b in zip(path, path[1:]):
        for neighbor, weight in graph[a]:
            if neighbor == b:
                total += weight
                break
    return total
ucs_path, ucs_cost, order = ucs("A", "G")
print("UNIFORM COST SEARCH")
print("UCS Path:", " -> ".join(ucs_path))
print("UCS Total Cost:", ucs_cost)
print("Processing Order:", order)
print("Verified Cost:", calculate_cost(ucs_path))
bfs_path = bfs("A", "G")
print("\nBREADTH FIRST SEARCH")
print("BFS Path:", " -> ".join(bfs_path))
print("BFS Total Cost:", calculate_cost(bfs_path))
