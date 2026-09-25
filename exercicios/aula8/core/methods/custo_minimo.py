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
    total_cost = 0.0

    rows_available = set(range(n))
    cols_available = set(range(m))

    while rows_available and cols_available:
        min_cost = float("inf")
        best_i, best_j = -1, -1

        # Encontra a célula de menor custo entre linhas e colunas disponíveis
        for i in rows_available:
            for j in cols_available:
                if cost_matrix[i][j] < min_cost:
                    min_cost = cost_matrix[i][j]
                    best_i, best_j = i, j

        quantity = min(supply[best_i], demand[best_j])
        allocation[best_i][best_j] = quantity
        total_cost += quantity * min_cost

        supply[best_i] -= quantity
        demand[best_j] -= quantity

        if supply[best_i] == 0:
            rows_available.remove(best_i)
        if demand[best_j] == 0:
            cols_available.remove(best_j)

    return {"allocation": allocation, "total_cost": total_cost}
