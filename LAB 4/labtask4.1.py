import heapq
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
h_original = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
h_overestimate = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}
def astar(graph, h, start, goal):
    # Queue entries: (f, g, node, path)
    queue = [(h[start], 0, start, [start])]
    best_g = {start: 0}
    trace = []
    expanded = []
    stale_skipped = 0
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if g != best_g.get(node, float("inf")):
            stale_skipped += 1
            continue
        trace.append((node, g, h[node], f))
        if node == goal:
            return {
                "path": path,
                "cost": g,
                "trace": trace,
                "expanded": expanded,
                "expansion_count": len(expanded),
                "stale_skipped": stale_skipped
            }
        expanded.append(node)
        for neighbour, cost in graph.get(node, []):
            new_g = g + cost
            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g
                new_f = new_g + h[neighbour]
                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )
    return None
def show_result(title, result):
    print("\n===== " + title + " =====")
    print("Path:", " -> ".join(result["path"]))
    print("Path cost (g):", result["cost"])
    print("Independently summed path cost:",
          sum(next(cost for nxt, cost in graph[node] if nxt == path_next)
              for node, path_next in zip(result["path"], result["path"][1:])))
    print("Trace (node, g, h, f):")
    for node, g, h_value, f in result["trace"]:
        note = "  <- goal, not counted as expanded" if node == "G" else ""
        print(f"  {node}: g={g}, h={h_value}, f={f}{note}")
    print("Expanded nodes:", ", ".join(result["expanded"]))
    print("Expansion count:", result["expansion_count"])
    print("Stale entries skipped:", result["stale_skipped"])

original_result = astar(graph, h_original, "S", "G")
modified_result = astar(graph, h_overestimate, "S", "G")
show_result("Original heuristic (h(C)=2)", original_result)
show_result("Overestimate test (h(C)=10)", modified_result)
print("\n===== COMPARISON =====")
print("Original path/cost:", " -> ".join(original_result["path"]),
      "/", original_result["cost"])
print("Modified path/cost:", " -> ".join(modified_result["path"]),
      "/", modified_result["cost"])
print("Original expansion count:", original_result["expansion_count"])
print("Modified expansion count:", modified_result["expansion_count"])
print("\nExplanation:")
print("C's true remaining cost is 3 (edge C -> G costs 3).")
print("Setting h(C)=10 overestimates this cost and violates admissibility.")
print("A* selects the route through B and returns cost 9 before expanding C,")
print("even though the optimal route through C has cost 6.")