def solve(
    cost_matrix: list[list[float]],
    production_vector: list[float],
    demand_vector: list[float],
) -> dict:
    supply = list(production_vector)
    demand = list(demand_vector)
    n = len(supply)
    m = len(demand)

    allocation = [[0.0 for _ in range(m)] for _ in range(n)]
    i, j = 0, 0
    total_cost = 0.0

    while i < n and j < m:
        quantity = min(supply[i], demand[j])
        allocation[i][j] = quantity
        total_cost += quantity * cost_matrix[i][j]

        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0 and demand[j] == 0:
            i += 1
            j += 1
        elif supply[i] == 0:
            i += 1
        else:
            j += 1

    return {"allocation": allocation, "total_cost": total_cost}
