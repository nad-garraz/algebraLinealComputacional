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


def generar_estado_inicial1(n):
    cantidad_pasos = n
    v = np.zeros(cantidad_pasos + 2)
    for estado in range(1, cantidad_pasos + 1):
        v[estado] = 1 / cantidad_pasos

    return np.array(v)


def generar_estado_inicial2(n):
    cantidad_pasos = n
    v = np.zeros(cantidad_pasos + 2)
    v[1] = 1
    return np.array(v)


def generar_plot_evolucion(
    pasos_entre_bar_casa, p, iteraciones, muestras, v, state, dir, file
):
    P = generar_matriz_transicion(pasos_entre_bar_casa, p)

    estados_a_plotear = np.array(np.zeros((iteraciones + 1, pasos_entre_bar_casa + 2)))
    estados_a_plotear[0] = v

    for i in range(1, iteraciones):
        if i <= iteraciones:
            v = P @ v  # Estado siguiente
            estados_a_plotear[i] = v

    pasos_vector = np.arange(0.0, 22.0, 1)  # data para el eje x

    # Plotear
    # Genero el gráfico loopeando en algunos resultados de la matriz
    fig = plt.figure()
    ax1 = fig.subplots(1, 1, sharex=True)

    for i in range(0, muestras):
        ax1.scatter(
            pasos_vector,
            estados_a_plotear[state[i]],
            label=f"estado {state[i]}",
            alpha=0.7,
        )

        # Genero data para poder hacer el gráfico en TiKz
        np.savetxt(
            f"./dataFiles/{dir}/{i}{file}",
            np.transpose(
                [pasos_vector, estados_a_plotear[state[i]]]
            ),
            fmt="%.10e",
            header="Output para la simulación de ejercicio de Markov borracho",
            comments="# Data pasos vs probabilidad",
        )

    ax1.legend(loc="upper center")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3)
    ax1.set_title(f"Estados del beodo que dio {iteraciones} pasos")

    plt.show()


estado_inicial1 = generar_estado_inicial1(20)
estado_inicial2 = generar_estado_inicial2(20)

principio = [1, 5, 10, 21]
final = [100, 200, 500, 1000]
generar_plot_evolucion(
    20, 0.5, 30, 4, estado_inicial1, principio, "item-b-plot/", "-step-item-b.data"
)
generar_plot_evolucion(
    20, 0.5, 1001, 4, estado_inicial1, final, "item-b-plot/", "-step-item-b-final.data"
)
generar_plot_evolucion(
    20, 0.5, 30, 4, estado_inicial2, principio, "item-c-plot/", "-step-item-c.data"
)
generar_plot_evolucion(
    20, 0.5, 1001, 4, estado_inicial2, final, "item-c-plot/", "-step-item-c-final.data"
)
generar_plot_evolucion(
    20, 0.8, 30, 4, estado_inicial1, principio, "item-d-plot/", "-step-item-d.data"
)
generar_plot_evolucion(
    20, 0.8, 1001, 4, estado_inicial1, final, "item-d-plot/", "-step-item-d-final.data"
)
generar_plot_evolucion(
    20, 0.8, 30, 4, estado_inicial2, principio, "item-d-plot/", "-step-item-d2.data"
)
generar_plot_evolucion(
    20, 0.8, 1001, 4, estado_inicial2, final, "item-d-plot/", "-step-item-d2-final.data"
)
