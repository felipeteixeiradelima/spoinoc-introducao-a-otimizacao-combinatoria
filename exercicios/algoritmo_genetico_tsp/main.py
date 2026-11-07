import os
import sys

from algoritmo_genetico import (
    MetodoAptidao,
    MetodoSelecao,
    MetodoSubstituicao,
    ResultadoExecucao,
    executar_algoritmo_genetico,
)
from cidade import carregar_cidades_de_arquivo


def obter_caminho_base() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def selecionar_arquivo_instancia() -> str:
    diretorio_base = obter_caminho_base()
    caminho_exemplo_1 = os.path.join(diretorio_base, "dados", "exemplo1.csv")
    caminho_exemplo_2 = os.path.join(diretorio_base, "dados", "exemplo2.csv")

    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        caminho_argumento = sys.argv[1]
        if os.path.exists(caminho_argumento):
            return caminho_argumento
        print(
            f"Arquivo '{caminho_argumento}' não encontrado. Selecione uma opção padrão:"
        )

    print("=" * 60)
    print("ALGORITMO GENÉTICO - PROBLEMA DO CAIXEIRO VIAJANTE (TSP)")
    print("=" * 60)
    print("Escolha o conjunto de dados para execução:")
    print("1 - Exemplo 1 (exemplo1.csv - 10 cidades)")
    print("2 - Exemplo 2 (exemplo2.csv - 10 cidades)")

    while True:
        opcao = input("Digite a opção desejada (1 ou 2) [Padrão: 1]: ").strip()
        if opcao in ("", "1"):
            return caminho_exemplo_1
        if opcao == "2":
            return caminho_exemplo_2
        print("Opção inválida. Digite 1 ou 2.")


def selecionar_metodo_aptidao() -> MetodoAptidao:
    if len(sys.argv) > 2:
        parametro = sys.argv[2].lower()
        if "trans" in parametro:
            return MetodoAptidao.TRANSLACAO
        if "escal" in parametro:
            return MetodoAptidao.ESCALONAMENTO

    print("\nEscolha o método de cálculo da aptidão:")
    print("1 - Escalonamento [0, 1] (Padrão)")
    print("2 - Translação")

    while True:
        opcao = input("Digite a opção desejada (1 ou 2) [Padrão: 1]: ").strip()
        if opcao in ("", "1"):
            return MetodoAptidao.ESCALONAMENTO
        if opcao == "2":
            return MetodoAptidao.TRANSLACAO
        print("Opção inválida. Digite 1 ou 2.")


def selecionar_metodo_selecao() -> MetodoSelecao:
    if len(sys.argv) > 3:
        parametro = sys.argv[3].lower()
        if "torn" in parametro:
            return MetodoSelecao.TORNEIO
        if "rolet" in parametro:
            return MetodoSelecao.RODA_DA_ROLETA

    print("\nEscolha o método de seleção:")
    print("1 - Roda da Roleta (Padrão)")
    print("2 - Torneio")

    while True:
        opcao = input("Digite a opção desejada (1 ou 2) [Padrão: 1]: ").strip()
        if opcao in ("", "1"):
            return MetodoSelecao.RODA_DA_ROLETA
        if opcao == "2":
            return MetodoSelecao.TORNEIO
        print("Opção inválida. Digite 1 ou 2.")


def selecionar_metodo_substituicao() -> MetodoSubstituicao:
    if len(sys.argv) > 4:
        parametro = sys.argv[4].lower()
        if "pai" in parametro:
            return MetodoSubstituicao.PAIS
        if "menos" in parametro or "apto" in parametro:
            return MetodoSubstituicao.MENOS_APTOS

    print("\nEscolha a política de substituição:")
    print("1 - Menos Aptos (Padrão)")
    print("2 - Pais")

    while True:
        opcao = input("Digite a opção desejada (1 ou 2) [Padrão: 1]: ").strip()
        if opcao in ("", "1"):
            return MetodoSubstituicao.MENOS_APTOS
        if opcao == "2":
            return MetodoSubstituicao.PAIS
        print("Opção inválida. Digite 1 ou 2.")


def formatar_ciclo_rota(rota: list[int]) -> str:
    return " -> ".join(map(str, rota)) + f" -> {rota[0]}"


def exibir_resumo_final(resultado: ResultadoExecucao) -> None:
    print("\n" + "=" * 60)
    print("RESULTADO FINAL DA OTIMIZAÇÃO")
    print("=" * 60)
    print("Total de gerações executadas: 2000")
    print("Tamanho da população: 100 indivíduos")
    print("Taxa de mutação: 10%")
    print(f"Método de aptidão: {resultado.metodo_aptidao.value}")
    print(f"Método de seleção: {resultado.metodo_selecao.value}")
    print(f"Método de substituição: {resultado.metodo_substituicao.value}")
    print(
        f"Tempo total de processamento: {resultado.tempo_execucao_segundos:.2f} segundos"
    )
    print("-" * 60)
    print(f"Melhor distância obtida: {resultado.melhor_distancia:.4f}")
    print(f"Melhor sequência (vetor): {resultado.melhor_rota}")
    print("Circuito fechado do Caixeiro:")
    print(formatar_ciclo_rota(resultado.melhor_rota))
    print("=" * 60)


def main() -> None:
    caminho_arquivo = selecionar_arquivo_instancia()
    metodo_aptidao = selecionar_metodo_aptidao()
    metodo_selecao = selecionar_metodo_selecao()
    metodo_substituicao = selecionar_metodo_substituicao()

    print(f"\nCarregando dados de: {caminho_arquivo}")
    mapa_cidades = carregar_cidades_de_arquivo(caminho_arquivo)
    print(f"Total de cidades carregadas: {len(mapa_cidades)}")

    print("\nIniciando algoritmo genético...\n")
    resultado = executar_algoritmo_genetico(
        mapa_cidades=mapa_cidades,
        tamanho_populacao=100,
        total_geracoes=2000,
        taxa_mutacao=0.10,
        metodo_aptidao=metodo_aptidao,
        metodo_selecao=metodo_selecao,
        metodo_substituicao=metodo_substituicao,
    )

    exibir_resumo_final(resultado)


if __name__ == "__main__":
    main()
