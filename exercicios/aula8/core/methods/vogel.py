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

    rows_available = list(range(n))
    cols_available = list(range(m))

    while rows_available and cols_available:
        # Se restar apenas uma linha ou uma coluna, aloca diretamente
        if len(rows_available) == 1:
            i = rows_available[0]
            for j in list(cols_available):
                qty = min(supply[i], demand[j])
                allocation[i][j] = qty
                total_cost += qty * cost_matrix[i][j]
                supply[i] -= qty
                demand[j] -= qty
                if demand[j] == 0:
                    cols_available.remove(j)
            break

        if len(cols_available) == 1:
            j = cols_available[0]
            for i in list(rows_available):
                qty = min(supply[i], demand[j])
                allocation[i][j] = qty
                total_cost += qty * cost_matrix[i][j]
                supply[i] -= qty
                demand[j] -= qty
                if supply[i] == 0:
                    rows_available.remove(i)
            break

        row_penalties = {}
        for i in rows_available:
            costs = sorted([cost_matrix[i][j] for j in cols_available])
            row_penalties[i] = costs[1] - costs[0] if len(costs) > 1 else costs[0]

        col_penalties = {}
        for j in cols_available:
            costs = sorted([cost_matrix[i][j] for i in rows_available])
            col_penalties[j] = costs[1] - costs[0] if len(costs) > 1 else costs[0]

        max_row_penalty = max(row_penalties.values())
        max_col_penalty = max(col_penalties.values())

        # Seleciona linha ou coluna com maior penalidade e a célula de menor custo nela
        if max_row_penalty >= max_col_penalty:
            best_i = max(row_penalties, key=row_penalties.get)
            best_j = min(cols_available, key=lambda j: cost_matrix[best_i][j])
        else:
            best_j = max(col_penalties, key=col_penalties.get)
            best_i = min(rows_available, key=lambda i: cost_matrix[i][best_j])

        quantity = min(supply[best_i], demand[best_j])
        allocation[best_i][best_j] = quantity
        total_cost += quantity * cost_matrix[best_i][best_j]

        supply[best_i] -= quantity
        demand[best_j] -= quantity

        if supply[best_i] == 0:
            rows_available.remove(best_i)
        if demand[best_j] == 0:
            cols_available.remove(best_j)

    return {"allocation": allocation, "total_cost": total_cost}
