import math
import random
import time
from dataclasses import dataclass
from cidade import Cidade


@dataclass
class ResultadoExecucao:
    melhor_rota: list[int]
    melhor_distancia: float
    historico_geracoes: list[float]
    tempo_execucao_segundos: float


def calcular_distancia_euclidiana(origem: Cidade, destino: Cidade) -> float:
    diferenca_x = destino.coordenada_x - origem.coordenada_x
    diferenca_y = destino.coordenada_y - origem.coordenada_y
    return math.sqrt(diferenca_x**2 + diferenca_y**2)


def calcular_distancia_total(
    individuo: list[int],
    mapa_cidades: dict[int, Cidade],
) -> float:
    distancia_total = 0.0
    quantidade_cidades = len(individuo)

    for indice in range(quantidade_cidades):
        cidade_atual = mapa_cidades[individuo[indice]]
        proxima_cidade = mapa_cidades[individuo[(indice + 1) % quantidade_cidades]]
        distancia_total += calcular_distancia_euclidiana(cidade_atual, proxima_cidade)

    return distancia_total


def gerar_populacao_inicial(
    tamanho_populacao: int,
    identificadores_cidades: list[int],
) -> list[list[int]]:
    populacao: list[list[int]] = []

    for _ in range(tamanho_populacao):
        individuo = random.sample(identificadores_cidades, len(identificadores_cidades))
        populacao.append(individuo)

    return populacao


def selecionar_pais(
    populacao: list[list[int]],
    mapa_cidades: dict[int, Cidade],
) -> tuple[list[tuple[list[int], list[int]]], list[int], float]:
    distancias = [
        calcular_distancia_total(individuo, mapa_cidades)
        for individuo in populacao
    ]

    indice_melhor = min(range(len(distancias)), key=lambda i: distancias[i])
    melhor_individuo = list(populacao[indice_melhor])
    melhor_distancia = distancias[indice_melhor]

    aptidoes = [1.0 / distancia for distancia in distancias]
    soma_aptidoes = sum(aptidoes)
    probabilidades = [aptidao / soma_aptidoes for aptidao in aptidoes]

    quantidade_pares = len(populacao) // 2
    pares_pais: list[tuple[list[int], list[int]]] = []

    for _ in range(quantidade_pares):
        selecionados = random.choices(populacao, weights=probabilidades, k=2)
        pai_1 = list(selecionados[0])
        pai_2 = list(selecionados[1])
        pares_pais.append((pai_1, pai_2))

    return pares_pais, melhor_individuo, melhor_distancia


def crossover_um_ponto(
    pai_1: list[int],
    pai_2: list[int],
) -> tuple[list[int], list[int]]:
    tamanho = len(pai_1)
    ponto_corte = random.randint(1, tamanho - 1)

    prefixo_filho_1 = pai_1[:ponto_corte]
    genes_restantes_1 = [gene for gene in pai_2 if gene not in prefixo_filho_1]
    filho_1 = prefixo_filho_1 + genes_restantes_1

    prefixo_filho_2 = pai_2[:ponto_corte]
    genes_restantes_2 = [gene for gene in pai_1 if gene not in prefixo_filho_2]
    filho_2 = prefixo_filho_2 + genes_restantes_2

    return filho_1, filho_2


def gerar_filhos_por_crossover(
    pares_pais: list[tuple[list[int], list[int]]],
) -> list[list[int]]:
    filhos: list[list[int]] = []

    for pai_1, pai_2 in pares_pais:
        filho_1, filho_2 = crossover_um_ponto(pai_1, pai_2)
        filhos.append(filho_1)
        filhos.append(filho_2)

    return filhos


def substituir_pais_por_filhos(filhos: list[list[int]]) -> list[list[int]]:
    return [list(filho) for filho in filhos]


def aplicar_mutacao(individuo: list[int], taxa_mutacao: float) -> list[int]:
    individuo_mutado = list(individuo)

    if random.random() < taxa_mutacao:
        posicao_1, posicao_2 = random.sample(range(len(individuo_mutado)), 2)
        individuo_mutado[posicao_1], individuo_mutado[posicao_2] = (
            individuo_mutado[posicao_2],
            individuo_mutado[posicao_1],
        )

    return individuo_mutado


def aplicar_mutacoes_na_populacao(
    populacao: list[list[int]],
    taxa_mutacao: float,
) -> list[list[int]]:
    return [
        aplicar_mutacao(individuo, taxa_mutacao)
        for individuo in populacao
    ]


def exibir_melhor_individuo_no_video(
    geracao: int,
    total_geracoes: int,
    melhor_distancia: float,
    melhor_individuo: list[int],
) -> None:
    print(
        f"Geração {geracao:04d}/{total_geracoes} | "
        f"Distância: {melhor_distancia:8.4f} | "
        f"Rota: {melhor_individuo}"
    )


def executar_algoritmo_genetico(
    mapa_cidades: dict[int, Cidade],
    tamanho_populacao: int = 100,
    total_geracoes: int = 2000,
    taxa_mutacao: float = 0.10,
) -> ResultadoExecucao:
    tempo_inicial = time.perf_counter()

    identificadores_cidades = list(mapa_cidades.keys())
    populacao = gerar_populacao_inicial(tamanho_populacao, identificadores_cidades)

    historico_geracoes: list[float] = []
    melhor_rota_global: list[int] = []
    melhor_distancia_global = float("inf")

    for geracao in range(1, total_geracoes + 1):
        pares_pais, melhor_individuo_geracao, melhor_distancia_geracao = selecionar_pais(
            populacao,
            mapa_cidades,
        )

        historico_geracoes.append(melhor_distancia_geracao)

        if melhor_distancia_geracao < melhor_distancia_global:
            melhor_distancia_global = melhor_distancia_geracao
            melhor_rota_global = list(melhor_individuo_geracao)

        exibir_melhor_individuo_no_video(
            geracao,
            total_geracoes,
            melhor_distancia_geracao,
            melhor_individuo_geracao,
        )

        filhos = gerar_filhos_por_crossover(pares_pais)
        populacao_substituida = substituir_pais_por_filhos(filhos)
        populacao = aplicar_mutacoes_na_populacao(populacao_substituida, taxa_mutacao)

    tempo_final = time.perf_counter()
    tempo_execucao = tempo_final - tempo_inicial

    return ResultadoExecucao(
        melhor_rota=melhor_rota_global,
        melhor_distancia=melhor_distancia_global,
        historico_geracoes=historico_geracoes,
        tempo_execucao_segundos=tempo_execucao,
    )
