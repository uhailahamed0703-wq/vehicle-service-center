
service_costs = [150000, 80000, 120000, 50000, 100000]

n = len(service_costs)

for i in range(n):
    for j in range(0, n - i - 1):
        if service_costs[j] > service_costs[j + 1]:
            service_costs[j], service_costs[j + 1] = (
                service_costs[j + 1],
                service_costs[j]
            )

print("Sorted service costs:", service_costs)
