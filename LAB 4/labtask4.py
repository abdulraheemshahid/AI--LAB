import heapq
from tracemalloc import start
start()
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
h_zero = {node: 0 for node in h}
def astar(graph, h, start, goal):
    queue = [(h[start], 0, start, [start])]
    best_g = {start: 0}      
    trace = []               
    expanded = []            
    stale = 0               
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if g != best_g[node]:
            stale += 1
            continue
        trace.append((node, g, h[node], f))
        if node == goal:
            return g, path, trace, expanded, stale
        expanded.append(node)
        for neighbour, cost in graph[node]:
            new_g = g + cost
            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g
                new_f = new_g + h[neighbour]
                heapq.heappush(queue, (new_f, new_g, neighbour, path + [neighbour]))
    return None
def sum_path_cost(graph, path):
    
    total = 0
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        for neighbour, cost in graph[a]:
            if neighbour == b:
                total += cost
    return total
def show(title, result):
    cost, path, trace, expanded, stale = result
    print("=====", title, "=====")
    print("Path           :", " -> ".join(path))
    print("Cost (from g)  :", cost)
    print("Cost (summed)  :", sum_path_cost(graph, path))
    print("Trace (node, g, h, f):")
    for node, g, hv, f in trace:
        note = "   <- goal, not counted" if node == path[-1] else ""
        print(f"   {node}: g={g}, h={hv}, f={f}{note}")
    print("Expanded nodes :", ", ".join(expanded))
    print("Expansion count:", len(expanded))
    print("Stale skipped  :", stale)
    print()
astar_result = astar(graph, h, "S", "G")
ucs_result = astar(graph, h_zero, "S", "G")
show("A* (lab heuristic)", astar_result)
show("UCS (h = 0)", ucs_result)
print("===== Comparison =====")
print("             A*    UCS")
print(f"Cost         {astar_result[0]}     {ucs_result[0]}")
print(f"Expansions   {len(astar_result[3])}     {len(ucs_result[3])}")
print(f"Stale        {astar_result[4]}     {ucs_result[4]}")