# Algoritmo Genético para o Problema do Caixeiro Viajante (TSP) - Versão 1

Implementação em Python de um Algoritmo Genético para solucionar o Problema do Caixeiro Viajante (*Traveling Salesperson Problem* - TSP) para instâncias de 10 cidades, em conformidade com o conteúdo apresentado em aula.

---

## Características da Implementação

| Parâmetro | Configuração |
| :--- | :--- |
| **Tamanho da População** | 100 indivíduos |
| **Codificação do Indivíduo** | Permutação com 10 cidades |
| **Geração da População Inicial** | Aleatória |
| **Método de Crossover** | Crossover de 1 ponto aleatório para TSP (preserva permutação) |
| **Política de Substituição** | Substituição dos pais pelos descendentes |
| **Taxa de Mutação** | 10% (0.10) com troca aleatória de dois alelos (*swap*) |
| **Critério de Parada** | 2000 gerações |
| **Cálculo da Função Objetivo** | Realizado dentro da etapa de seleção |
| **Saída no Vídeo** | Exibição no console do melhor indivíduo e sua distância a cada geração |

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
├── algoritmo_genetico.py # Operadores genéticos e laço evolutivo
├── main.py               # Ponto de entrada e interface com usuário
├── testes.py             # Suíte de testes unitários
└── README.md             # Instruções e documentação
```

---

## Requisitos do Sistema

- **Python**: versão 3.10 ou superior.
- **Bibliotecas**: utiliza exclusivamente a biblioteca padrão do Python (`math`, `random`, `time`, `csv`, `dataclasses`, `unittest`). Não é necessária a instalação de pacotes externos.

---

## Como Executar o Código

### 1. Execução Interativa (com menu de seleção)

No terminal, navegue até a pasta do exercício (ou a partir da raiz do repositório) e execute:

```bash
# A partir da raiz do repositório:
python exercicios/algoritmo_genetico_tsp/main.py

# Ou entrando na pasta do exercício:
cd exercicios/algoritmo_genetico_tsp
python main.py
```

O programa apresentará um menu para escolher qual instância resolver:
- `1`: Exemplo 1 (`exemplo1.csv` - 10 cidades)
- `2`: Exemplo 2 (`exemplo2.csv` - 10 cidades)

### 2. Execução Direta via Linha de Comando (Passando o CSV)

Você também pode fornecer o caminho do arquivo CSV diretamente como argumento:

```bash
# Executando o Exemplo 1:
python exercicios/algoritmo_genetico_tsp/main.py exercicios/algoritmo_genetico_tsp/dados/exemplo1.csv

# Executando o Exemplo 2:
python exercicios/algoritmo_genetico_tsp/main.py exercicios/algoritmo_genetico_tsp/dados/exemplo2.csv
```

### 3. Execução dos Testes Unitários

Para validar os operadores genéticos, leitura dos dados e integridade das permutações:

```bash
python exercicios/algoritmo_genetico_tsp/testes.py
```

---

## Detalhes dos Operadores Implementados

1. **Cálculo da Função Objetivo dentro da Seleção**:
   - A distância euclidiana total do circuito fechado (retornando à cidade de partida) é calculada para cada indivíduo da população dentro da função de seleção.
   - A aptidão de cada indivíduo é obtida a partir do inverso da distância total da rota ($1 / \text{distância}$), priorizando rotas mais curtas na roleta de seleção.

2. **Crossover de 1 Ponto Aleatório (TSP)**:
   - Um ponto de corte aleatório divide o primeiro pai.
   - O primeiro filho herda o segmento inicial do Pai 1. As cidades faltantes são preenchidas respeitando a ordem de aparição no Pai 2.
   - O segundo filho é gerado de forma simétrica (iniciando com o prefixo do Pai 2 e completando com as cidades do Pai 1).

3. **Substituição dos Pais**:
   - Cada par de pais selecionados para reprodução é substituído pelos seus dois descendentes gerados após o crossover e mutação.

4. **Mutação**:
   - Para cada indivíduo gerado, aplica-se uma probabilidade de mutação de 10%. Quando sorteado, dois alelos (cidades) em posições aleatórias têm seus lugares trocados no cromossomo.
