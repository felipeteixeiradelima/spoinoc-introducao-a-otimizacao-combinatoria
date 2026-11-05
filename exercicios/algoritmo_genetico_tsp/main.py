import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from algoritmo_genetico import ResultadoExecucao, executar_algoritmo_genetico
from cidade import carregar_cidades_de_arquivo


def obter_caminho_base() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def selecionar_arquivo_instancia() -> str:
    diretorio_base = obter_caminho_base()
    caminho_exemplo_1 = os.path.join(diretorio_base, "dados", "exemplo1.csv")
    caminho_exemplo_2 = os.path.join(diretorio_base, "dados", "exemplo2.csv")

    if len(sys.argv) > 1:
        caminho_argumento = sys.argv[1]
        if os.path.exists(caminho_argumento):
            return caminho_argumento
        print(f"Arquivo '{caminho_argumento}' não encontrado. Selecione uma opção padrão:")

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


def formatar_ciclo_rota(rota: list[int]) -> str:
    return " -> ".join(map(str, rota)) + f" -> {rota[0]}"


def exibir_resumo_final(resultado: ResultadoExecucao) -> None:
    print("\n" + "=" * 60)
    print("RESULTADO FINAL DA OTIMIZAÇÃO")
    print("=" * 60)
    print("Total de gerações executadas: 2000")
    print("Tamanho da população: 100 indivíduos")
    print("Taxa de mutação: 10%")
    print(f"Tempo total de processamento: {resultado.tempo_execucao_segundos:.2f} segundos")
    print("-" * 60)
    print(f"Melhor distância obtida: {resultado.melhor_distancia:.4f}")
    print(f"Melhor sequência (vetor): {resultado.melhor_rota}")
    print("Circuito fechado do Caixeiro:")
    print(formatar_ciclo_rota(resultado.melhor_rota))
    print("=" * 60)


def main() -> None:
    caminho_arquivo = selecionar_arquivo_instancia()
    print(f"\nCarregando dados de: {caminho_arquivo}")
    mapa_cidades = carregar_cidades_de_arquivo(caminho_arquivo)
    print(f"Total de cidades carregadas: {len(mapa_cidades)}")

    print("\nIniciando algoritmo genético...\n")
    resultado = executar_algoritmo_genetico(
        mapa_cidades=mapa_cidades,
        tamanho_populacao=100,
        total_geracoes=2000,
        taxa_mutacao=0.10,
    )

    exibir_resumo_final(resultado)


if __name__ == "__main__":
    main()
