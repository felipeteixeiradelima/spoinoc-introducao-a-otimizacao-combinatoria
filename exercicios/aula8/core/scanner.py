def _get_int_input(message="", min: int | None = None, max: int | None = None) -> int:
    while True:
        raw_input = input(message)

        if not raw_input:
            continue

        clean_input = raw_input.strip()

        try:
            clean_input = int(clean_input)
        except ValueError:
            continue

        if min and clean_input < min:
            continue

        if max and clean_input > max:
            continue

        return clean_input


def get_num_rows() -> int:
    return _get_int_input("Digite o número N de linhas: ", min=0)


def get_num_columns() -> int:
    return _get_int_input("Digite o número M de colunas: ", min=0)


def _get_matrix_element(row, col) -> int:
    return _get_int_input(f"Digite o elemento A{row}{col} da matriz de custo")


def get_list(num_elements: int, element_label: str, message: str) -> list[int]:
    print(message)

    list_: list[int] = []

    for i in range(num_elements):
        list_.append(
            _get_int_input(f"Digite a quantidade do {i + 1}º {element_label}: ")
        )

    return list_


def get_cost_matrix(num_rows: int, num_cols: int) -> list[list[int]]:
    print("Input da matriz de custo")

    matrix: list[list[int]] = [[]]

    for i in range(num_rows):
        row: list[int] = []
        for j in range(num_cols):
            row.append(_get_matrix_element(i, j))
        matrix.append(row)

    return matrix


def get_option(max: int, min: int = 0):
    return _get_int_input("Digite uma opção: ", min, max)
