
from itertools import permutations

locations = [
    "Workshop A",
    "Workshop B",
    "Workshop C",
    "Workshop D",
    "Workshop E"
]

distances = {
    ("Service Center", "Workshop A"): 4,
    ("Service Center", "Workshop B"): 7,
    ("Service Center", "Workshop C"): 8,
    ("Service Center", "Workshop D"): 6,
    ("Service Center", "Workshop E"): 9,

    ("Workshop A", "Workshop B"): 3,
    ("Workshop A", "Workshop C"): 6,
    ("Workshop A", "Workshop D"): 5,
    ("Workshop A", "Workshop E"): 7,

    ("Workshop B", "Workshop C"): 4,
    ("Workshop B", "Workshop D"): 6,
    ("Workshop B", "Workshop E"): 5,

    ("Workshop C", "Workshop D"): 3,
    ("Workshop C", "Workshop E"): 4,

    ("Workshop D", "Workshop E"): 2
}

def get_distance(a, b):
    if (a, b) in distances:
        return distances[(a, b)]
    return distances[(b, a)]

best_route = None
shortest_distance = float("inf")

for route in permutations(locations):
    journey = ("Service Center",) + route + ("Service Center",)
    total_distance = 0

    for i in range(len(journey) - 1):
        total_distance += get_distance(
            journey[i],
            journey[i + 1]
        )

    if total_distance < shortest_distance:
        shortest_distance = total_distance
        best_route = journey

print("Best delivery route:")
print(" -> ".join(best_route))
print("Total distance:", shortest_distance, "km")
