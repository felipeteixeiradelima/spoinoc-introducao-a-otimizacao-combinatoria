import csv
from dataclasses import dataclass


@dataclass(frozen=True)
class Cidade:
    identificador: int
    coordenada_x: float
    coordenada_y: float


def carregar_cidades_de_arquivo(caminho_arquivo: str) -> dict[int, Cidade]:
    cidades: dict[int, Cidade] = {}

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv, None)

        for linha in leitor_csv:
            if not linha:
                continue

            identificador = int(linha[0].strip())
            coordenada_x = float(linha[1].strip().replace(",", "."))
            coordenada_y = float(linha[2].strip().replace(",", "."))

            cidades[identificador] = Cidade(
                identificador=identificador,
                coordenada_x=coordenada_x,
                coordenada_y=coordenada_y,
            )

    return cidades
