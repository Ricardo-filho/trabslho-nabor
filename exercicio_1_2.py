import random
import math
import matplotlib.pyplot as plt


# CÁLCULO ANALÍTICO

def disponibilidade_analitica(n, k, p):
    disponibilidade = 0

    for i in range(k, n + 1):
        disponibilidade += (
            math.comb(n, i)
            * (p ** i)
            * ((1 - p) ** (n - i))
        )

    return disponibilidade


# SIMULADOR ESTOCÁSTICO

def disponibilidade_simulada(n, k, p, rodadas=100000):
    rodadas_bem_sucedidas = 0

    for _ in range(rodadas):
        servidores_disponiveis = 0

        for _ in range(n):
            numero_aleatorio = random.random()

            if numero_aleatorio <= p:
                servidores_disponiveis += 1

        if servidores_disponiveis >= k:
            rodadas_bem_sucedidas += 1

    return rodadas_bem_sucedidas / rodadas


# CONFIGURAÇÕES

valores_n = [2, 4, 6, 8]

valores_p = [
    0.0,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0
]

rodadas = 100000


# FUNCAOO PARA EXECUTAR UM CASO

def executar_caso(nome_caso, funcao_k):

    plt.figure(figsize=(10, 6))

    print("\n")
    print("=" * 70)
    print(nome_caso)
    print("=" * 70)

    for n in valores_n:

        k = funcao_k(n)

        valores_analiticos = []
        valores_experimentais = []

        print(f"\nn = {n} | k = {k}")
        print("-" * 55)
        print("p      Analítico      Experimental      Diferença")
        print("-" * 55)

        for p in valores_p:

            analitico = disponibilidade_analitica(n, k, p)

            experimental = disponibilidade_simulada(
                n,
                k,
                p,
                rodadas
            )

            diferenca = abs(analitico - experimental)

            valores_analiticos.append(analitico)
            valores_experimentais.append(experimental)

            print(
                f"{p:.1f}     "
                f"{analitico:.6f}      "
                f"{experimental:.6f}        "
                f"{diferenca:.6f}"
            )

        plt.plot(
            valores_p,
            valores_analiticos,
            label=f"Analítico n={n}"
        )

        plt.scatter(
            valores_p,
            valores_experimentais,
            label=f"Experimental n={n}"
        )

    plt.xlabel("p")
    plt.ylabel("Disponibilidade")
    plt.title(nome_caso)
    plt.xlim(0, 1)
    plt.ylim(0, 1.05)
    plt.grid()
    plt.legend()
    plt.show()


# CASO 1: k = 1 

executar_caso(
    "Disponibilidade - Caso k = 1",
    lambda n: 1
)


# CASO 2: k = n/2

executar_caso(
    "Disponibilidade - Caso k = n/2",
    lambda n: n // 2
)


# CASO 3: k = n

executar_caso(
    "Disponibilidade - Caso k = n",
    lambda n: n
)


# |   p |       AnalItico |   Experimental | Diferença |
#| --: | --------------: | -------------: | --------: |
#| 0.0 | valor calculado | valor simulado | diferença |
#| 0.1 | valor calculado | valor simulado | diferença |
#| ... |             ... |            ... |       ... |
#| 1.0 | valor calculado | valor simulado | diferença |


#4. Conclusão Os resultados experimentais obtidos pelo simulador estocástico ficaram próximos dos valores calculados analiticamente. A pequena diferença entre os resultados ocorre devido ao caráter aleatório da simulação. 
#Com 100.000 rodadas, é possível observar uma boa aproximação entre os valores teóricos e experimentais. Para \(k=1\), o aumento do número de servidores aumenta a disponibilidade. Para \(k=n\), ocorre o comportamento contrário, pois todos os servidores precisam estar disponíveis. Para \(k=n/2\), observa-se um comportamento intermediário.
#Dessa forma, os resultados da simulação confirmam o comportamento previsto pela fórmula matemática obtida no Exercício 1.1.
