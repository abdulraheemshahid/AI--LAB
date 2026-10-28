from collections import deque 
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    order = []
    while queue:
        node, path = queue.popleft()
        order.append(node)
        if node == goal:
            return path, order
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(
                    (neighbor, path + [neighbor])
                )
    return None, order
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    order = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        if node == goal:
            return path, order
        # Reverse order so B is explored before C
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor])
                )
    return None, order

bfs_path, bfs_order = bfs("A", "G")
dfs_path, dfs_order = dfs("A", "G")
print("BFS Path:", " -> ".join(bfs_path))
print("BFS Visit Order:", bfs_order)
print()
print("DFS Path:", " -> ".join(dfs_path))
print("DFS Visit Order:", dfs_order)
