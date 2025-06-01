import numpy as np
import matplotlib.pyplot as plt


def generar_matriz_transicion(n, p):
    cantidad_pasos = n
    casa = cantidad_pasos + 1
    bar = 0
    matriz_transicion = np.zeros((cantidad_pasos + 2, cantidad_pasos + 2))
    matriz_transicion[bar][bar] = 1
    matriz_transicion[casa][casa] = 1

    for col in range(1, cantidad_pasos + 1):
        row = col - 1
        matriz_transicion[row][col] = 1 - p
        matriz_transicion[row + 2][col] = p

    return np.array(matriz_transicion)


def generar_estado_inicial(n):
    cantidad_pasos = n
    v = np.zeros(cantidad_pasos + 2)
    for estado in range(1, cantidad_pasos + 1):
        v[estado] = 1 / cantidad_pasos

    return np.array(v)


def generar_plot_evolucion(pasos_entre_bar_casa, p, iteraciones):
    P = generar_matriz_transicion(pasos_entre_bar_casa, p)

    v = generar_estado_inicial(pasos_entre_bar_casa)  # Inicializo vectores estado final

    estados_a_plotear = np.array(np.zeros((iteraciones + 1, pasos_entre_bar_casa + 2)))
    estados_a_plotear[0] = v

    for i in range(1, iteraciones + 1):
        if i == iteraciones:
            print(f"v{i}: {v}")
        if i <= iteraciones:
            v = P @ v  # Estado siguiente
            estados_a_plotear[i] = v

    pasos_vector = np.arange(0.0, 22.0, 1)
    muestras = 5

    # Plotear
    # Genero el gráfico loopeando en algunos resultados de la matriz
    fig = plt.figure()
    ax1, ax2 = fig.subplots(1, 2, sharex=True)

    iteraciones = 10
    for i in range(muestras + 1):
        ax1.scatter(
            pasos_vector,
            estados_a_plotear[iteraciones // muestras * i],
            label=f"estado {iteraciones//muestras * i}",
            alpha=0.7,
        )
        # Genero data para poder hacer el gráfico en TiKz
        np.savetxt(f"./dataFiles/test{i}-item-b.data",
                   np.transpose([pasos_vector,estados_a_plotear[iteraciones // muestras * i]]),
                   fmt='%.10e',
                   header='Output para la simulación de ejercicio de Markov borracho',
                   comments="# Data pasos vs probabilidad")
    ax1.legend(loc="upper center")
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale("log")
    ax1.set_title(f"Estados del beodo que dio {iteraciones} pasos")
    
    iteraciones = 1000
    for i in range(muestras + 1):
        ax2.scatter(
            pasos_vector,
            estados_a_plotear[iteraciones // muestras * i],
            label=f"estado {iteraciones//muestras * i}",
            alpha=0.7,
        )
        # Genero data para poder hacer el gráfico en TiKz
        np.savetxt(f"./dataFiles/test{i}-item-b-final.data",
                   np.transpose([pasos_vector,estados_a_plotear[iteraciones // muestras * i]]),
                   fmt='%.10e',
                   header='Output para la simulación de ejercicio de Markov borracho',
                   comments="# Data pasos vs probabilidad")
    ax2.legend(loc="upper center")
    ax2.set_yscale("log")
    ax2.grid(True, alpha=0.3)
    ax2.set_title(f"Estados del beodo que dio {iteraciones} pasos")

    plt.show()


generar_plot_evolucion(20, 0.5, 1000)
