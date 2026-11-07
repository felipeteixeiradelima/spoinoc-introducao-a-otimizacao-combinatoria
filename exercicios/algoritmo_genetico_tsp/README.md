# Algoritmo Genético para o Problema do Caixeiro Viajante (TSP)

Implementação em Python de um Algoritmo Genético para solucionar o Problema do Caixeiro Viajante (*Traveling Salesperson Problem* - TSP) para instâncias de 10 cidades, em conformidade com o conteúdo apresentado em aula.

---

## Autores

- Amanda Jen - **SP3154068**
- Felipe Teixeira de Lima - **SP3155048**

---

## Características da Implementação

| Parâmetro | Opções Disponíveis | Padrão |
| :--- | :--- | :--- |
| **Tamanho da População** | 100 indivíduos | 100 |
| **Codificação do Indivíduo** | Permutação com 10 cidades | 10 cidades |
| **Geração da População Inicial** | Aleatória | Aleatória |
| **Cálculo da Aptidão** | **Translação** ou **Escalonamento** | Escalonamento |
| **Método de Seleção** | **Roda da Roleta** ou **Torneio** | Roda da Roleta |
| **Método de Crossover** | Crossover de 1 ponto aleatório para TSP | 1 ponto aleatório |
| **Política de Substituição** | **Substituição dos Pais** ou **Menos Aptos** | Menos Aptos |
| **Taxa de Mutação** | 10% (0.10) com troca aleatória de dois alelos (*swap*) | 10% |
| **Critério de Parada** | 2000 gerações | 2000 gerações |
| **Cálculo da Função Objetivo** | Dentro da etapa de seleção | Sim |
| **Saída no Vídeo** | Exibição no console do melhor indivíduo a cada geração | Sim |

---

## Estrutura dos Arquivos

```text
exercicios/algoritmo_genetico_tsp/
│
├── dados/
│   ├── exemplo1.csv      # Coordenadas das 10 cidades do Exemplo 1
│   └── exemplo2.csv      # Coordenadas das 10 cidades do Exemplo 2
│
├── cidade.py             # Modelo de dados da cidade e leitor de CSV
├── algoritmo_genetico.py # Operadores genéticos, aptidão, seleção e laço evolutivo
├── main.py               # Ponto de entrada com menu interativo e suporte a argumentos CLI
├── testes.py             # Suíte de testes unitários
└── README.md             # Instruções e documentação
```

---

## Requisitos do Sistema

- **Python**: versão 3.10 ou superior.
- **Bibliotecas**: utiliza exclusivamente a biblioteca padrão do Python (`math`, `random`, `time`, `csv`, `dataclasses`, `enum`, `unittest`).
- **Linter e Formatador (opcional para desenvolvimento)**: [Ruff](https://docs.astral.sh/ruff/).

---

## Como Executar o Código

### 1. Execução Interativa (com menus de seleção)

No terminal, execute:

```bash
# A partir da raiz do repositório:
python exercicios/algoritmo_genetico_tsp/main.py

# Ou entrando na pasta do exercício:
cd exercicios/algoritmo_genetico_tsp
python main.py
```

O programa apresentará menus para configurar a execução:
1. **Conjunto de dados**: `1` para Exemplo 1 ou `2` para Exemplo 2.
2. **Cálculo da aptidão**: `1` para Escalonamento ou `2` para Translação.
3. **Método de seleção**: `1` para Roda da Roleta ou `2` para Torneio.
4. **Política de substituição**: `1` para Menos Aptos ou `2` para Pais.

*(Pressionar `Enter` seleciona automaticamente a opção padrão de cada menu)*

### 2. Execução Direta via Linha de Comando (Passando Argumentos)

Você pode passar os parâmetros diretamente na chamada do script:

```bash
# Sintaxe:
# python main.py [arquivo_csv] [metodo_aptidao] [metodo_selecao] [metodo_substituicao]

# Exemplo: Escalonamento + Torneio + Menos Aptos no Exemplo 1:
python exercicios/algoritmo_genetico_tsp/main.py exercicios/algoritmo_genetico_tsp/dados/exemplo1.csv escalonamento torneio menos_aptos

# Exemplo: Translação + Roleta + Pais no Exemplo 2:
python exercicios/algoritmo_genetico_tsp/main.py exercicios/algoritmo_genetico_tsp/dados/exemplo2.csv translacao roleta pais
```

### 3. Execução dos Testes Unitários

Para validar os operadores genéticos, leitura dos dados e integridade das permutações:

```bash
python exercicios/algoritmo_genetico_tsp/testes.py
```

---

## Detalhes dos Operadores Implementados

1. **Cálculo da Aptidão**:
   - **Translação**: subtrai a avaliação de cada indivíduo do pior valor encontrado ($\tilde{f}_k = f_{\max} - f_k$), garantindo que o menos apto receba valor 0 e os mais aptos recebam valores positivos.
   - **Escalonamento**: normaliza linearmente a aptidão no intervalo $[0, 1]$ através da fórmula $\bar{f}_k = \frac{f_{\max} - f_k}{f_{\max} - f_{\min}}$.

2. **Métodos de Seleção**:
   - **Roda da Roleta**: probabilidade de seleção de cada indivíduo proporcional à sua aptidão ($P(i) = \text{aptidão}_i / \sum \text{aptidões}$).
   - **Torneio**: sorteia aleatoriamente dois competidores distintos da população; o de maior aptidão vence o torneio e é selecionado como progenitor.

3. **Políticas de Substituição**:
   - **Substituição dos Pais**: os descendentes gerados após recombinação e mutação substituem diretamente os progenitores.
   - **Substituição dos Menos Aptos**: os descendentes são adicionados à população e os indivíduos com pior aptidão são descartados, preservando os mais aptos.

4. **Crossover de 1 Ponto Aleatório (TSP)**:
   - Um ponto de corte aleatório divide o cromossomo. O filho herda o prefixo do primeiro pai e as cidades restantes são completadas conforme a ordem do segundo pai, evitando cidades duplicadas.

5. **Mutação**:
   - Probabilidade de 10% por indivíduo de sofrer troca aleatória de posição entre dois alelos (*swap*).
