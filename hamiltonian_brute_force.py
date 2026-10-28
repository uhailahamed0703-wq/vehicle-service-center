# Task 5 - Brute Force Algorithm
# Hamiltonian circuit on a complete graph of 6 nodes
# M.I. Uhail Ahamed - NIM 20250040214

from itertools import permutations

nodes = ["A", "B", "C", "D", "E", "F"]

# distance between every pair of nodes (complete graph, symmetric)
edges = {
    ("A", "B"): 12, ("A", "C"): 10, ("A", "D"): 19, ("A", "E"): 8,  ("A", "F"): 15,
    ("B", "C"): 3,  ("B", "D"): 7,  ("B", "E"): 11, ("B", "F"): 9,
    ("C", "D"): 6,  ("C", "E"): 14, ("C", "F"): 5,
    ("D", "E"): 4,  ("D", "F"): 13,
    ("E", "F"): 16,
}


def dist(u, v):
    return edges[(u, v)] if (u, v) in edges else edges[(v, u)]


def route_cost(route):
    total = 0
    for i in range(len(route) - 1):
        total += dist(route[i], route[i + 1])
    return total


start = nodes[0]
others = nodes[1:]

all_routes = []
seen = set()

# fix A as the starting point, try every order of the other 5 nodes
for p in permutations(others):
    route = [start] + list(p) + [start]
    # a route and its reverse are the same circuit, keep only one
    key = tuple(route[1:-1]) if route[1] < route[-2] else tuple(reversed(route[1:-1]))
    if key in seen:
        continue
    seen.add(key)
    all_routes.append((route, route_cost(route)))

print("Number of possible circuits:", len(all_routes))
print()
for no, (route, cost) in enumerate(all_routes, 1):
    print(f"{no:2d}. {' - '.join(route)}  = {cost}")

best_route, best_cost = min(all_routes, key=lambda x: x[1])
print()
print("Fastest (shortest) route:", " - ".join(best_route))
print("Total distance:", best_cost)
