graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dls(start, goal, limit):
    def search(node, path, depth):
        if node == goal:
            return "FOUND", path
        if depth == limit:
            if graph[node]:
                return "CUTOFF", None
            return "FAILURE", None
        cutoff_occurred = False
        for neighbor in graph[node]:
            if neighbor not in path:
                status, result = search(
                    neighbor, path + [neighbor], depth + 1
                )
                if status == "FOUND":
                    return status, result
                if status == "CUTOFF":
                    cutoff_occurred = True
        if cutoff_occurred:
            return "CUTOFF", None
        return "FAILURE", None
    return search(start, [start], 0)
def iddfs(start, goal, max_depth):
    attempts = []
    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit)
        attempts.append((limit, status))
        if status == "FOUND":
            return status, path, attempts
    return "CUTOFF", None, attempts
print("DEPTH LIMITED SEARCH")
for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit)
    print(f"Limit {limit}: {status}, Path: {path}")
print("\nITERATIVE DEEPENING DFS")
for max_depth in [1, 2, 3, 4]:
    status, path, attempts = iddfs("A", "G", max_depth)
    print(
        f"Max Depth {max_depth}: {status}, "
        f"Path: {path}, Attempts: {attempts}"
    )
