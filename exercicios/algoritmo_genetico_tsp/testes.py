import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cidade import Cidade, carregar_cidades_de_arquivo
from algoritmo_genetico import (
    calcular_distancia_euclidiana,
    calcular_distancia_total,
    gerar_populacao_inicial,
    selecionar_pais,
    crossover_um_ponto,
    gerar_filhos_por_crossover,
    substituir_pais_por_filhos,
    aplicar_mutacao,
    aplicar_mutacoes_na_populacao,
    executar_algoritmo_genetico,
)


class TesteAlgoritmoGeneticoTSP(unittest.TestCase):
    def setUp(self) -> None:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.caminho_exemplo_1 = os.path.join(diretorio_atual, "dados", "exemplo1.csv")
        self.caminho_exemplo_2 = os.path.join(diretorio_atual, "dados", "exemplo2.csv")

    def test_carregamento_exemplo_1(self) -> None:
        cidades = carregar_cidades_de_arquivo(self.caminho_exemplo_1)
        self.assertEqual(len(cidades), 10)
        self.assertIn(1, cidades)
        self.assertEqual(cidades[1].coordenada_x, 1.0)
        self.assertEqual(cidades[1].coordenada_y, 1.0)

    def test_carregamento_exemplo_2_com_virgula(self) -> None:
        cidades = carregar_cidades_de_arquivo(self.caminho_exemplo_2)
        self.assertEqual(len(cidades), 10)
        self.assertIn(3, cidades)
        self.assertEqual(cidades[3].coordenada_x, 1.25)
        self.assertEqual(cidades[3].coordenada_y, 7.0)

    def test_calculo_distancia_euclidiana(self) -> None:
        cidade_a = Cidade(identificador=1, coordenada_x=0.0, coordenada_y=0.0)
        cidade_b = Cidade(identificador=2, coordenada_x=3.0, coordenada_y=4.0)
        distancia = calcular_distancia_euclidiana(cidade_a, cidade_b)
        self.assertAlmostEqual(distancia, 5.0)

    def test_geracao_populacao_inicial(self) -> None:
        cidades = list(range(1, 11))
        tamanho_populacao = 100
        populacao = gerar_populacao_inicial(tamanho_populacao, cidades)

        self.assertEqual(len(populacao), 100)
        for individuo in populacao:
            self.assertEqual(len(individuo), 10)
            self.assertEqual(sorted(individuo), cidades)

    def test_crossover_um_ponto_mantem_permutacao_valida(self) -> None:
        pai_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pai_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        filho_1, filho_2 = crossover_um_ponto(pai_1, pai_2)

        self.assertEqual(len(filho_1), 10)
        self.assertEqual(len(filho_2), 10)
        self.assertEqual(sorted(filho_1), sorted(pai_1))
        self.assertEqual(sorted(filho_2), sorted(pai_2))

    def test_crossover_caso_especifico_dos_slides(self) -> None:
        pai_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        pai_2 = [4, 5, 3, 6, 8, 9, 7, 2, 1]
        ponto_corte = 6

        prefixo = pai_1[:ponto_corte]
        restante = [gene for gene in pai_2 if gene not in prefixo]
        filho = prefixo + restante

        self.assertEqual(filho, [1, 2, 3, 4, 5, 6, 8, 9, 7])

    def test_mutacao_mantem_cidades_unicas(self) -> None:
        individuo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        mutado = aplicar_mutacao(individuo, taxa_mutacao=1.0)
        self.assertEqual(len(mutado), 10)
        self.assertEqual(sorted(mutado), sorted(individuo))

    def test_selecao_e_calculo_funcao_objetivo(self) -> None:
        mapa_cidades = carregar_cidades_de_arquivo(self.caminho_exemplo_1)
        populacao = gerar_populacao_inicial(100, list(mapa_cidades.keys()))

        pares_pais, melhor_individuo, melhor_distancia = selecionar_pais(
            populacao,
            mapa_cidades,
        )

        self.assertEqual(len(pares_pais), 50)
        self.assertEqual(len(melhor_individuo), 10)
        self.assertGreater(melhor_distancia, 0.0)

    def test_execucao_completa_reduzida(self) -> None:
        mapa_cidades = carregar_cidades_de_arquivo(self.caminho_exemplo_1)
        resultado = executar_algoritmo_genetico(
            mapa_cidades=mapa_cidades,
            tamanho_populacao=100,
            total_geracoes=10,
            taxa_mutacao=0.10,
        )

        self.assertEqual(len(resultado.melhor_rota), 10)
        self.assertGreater(resultado.melhor_distancia, 0.0)
        self.assertEqual(len(resultado.historico_geracoes), 10)


if __name__ == "__main__":
    unittest.main()
