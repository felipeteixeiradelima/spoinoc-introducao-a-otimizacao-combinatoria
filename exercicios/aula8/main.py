from core import scanner
from core.methods import canto_noroeste, custo_minimo, vogel


def print_options() -> None:
    print("Escolha o método:")
    print("1. Canto Noroeste")
    print("2. Custo Mínimo")
    print("3. Vogel")


def main() -> None:
    n = scanner.get_num_rows()
    m = scanner.get_num_columns()

    production_vector = scanner.get_list(
        num_elements=n, element_label="produtor", message="Input dos produtores"
    )

    demand_vector = scanner.get_list(
        num_elements=m, element_label="depósito", message="Input dos depósitos"
    )

    cost_matrix = scanner.get_cost_matrix(n, m)

    print_options()
    option = scanner.get_option(min=1, max=3)

    match option:
        case 1:
            resultado = canto_noroeste.solve(
                cost_matrix, production_vector, demand_vector
            )
        case 2:
            resultado = custo_minimo.solve(
                cost_matrix, production_vector, demand_vector
            )
        case 3:
            resultado = vogel.solve(cost_matrix, production_vector, demand_vector)

    print("Resultado:", resultado, sep="\n")


if __name__ == "__main__":
    main()
