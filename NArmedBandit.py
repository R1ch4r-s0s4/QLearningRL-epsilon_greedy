import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from accion import Accion
from epsilon_greedy import Epsilon_Greedy
from ActionValue import ActionValue

muestras = 10000


def main():
    brazos = []
    brazo1 = Accion(1, muestras, 2.3, 0.6)  # 0.6
    brazos.append(brazo1)
    brazo2 = Accion(2, muestras, 2.1, 0.9)  # 0.9
    brazos.append(brazo2)
    brazo3 = Accion(3, muestras, 1.5, 1.0)  # 2.0
    brazos.append(brazo3)
    brazo4 = Accion(4, muestras, 1.3, 0.4)  # 0.4
    brazos.append(brazo4)

    CR = ActionValue(brazos, muestras)
    CR.set_epsilon(0.1)
    CR.UpdateQa()
    # CR.graficarCR()
    # for i in range(10):
    #   e1.seleccion(0.1,[2.3, 2.1, 1.5, 1.3])
    # print(e1.ramdom_action())
    graficar_brazos_juntos(brazos)
    plt.show()


def graficar_brazos_juntos(brazos):
    for i in range(len(brazos)):
        plt.plot(brazos[i].get_immediate_rewards(), label="Arm {}".format(brazos[i].id_arm), linewidth=1)

    plt.grid(True)
    plt.legend()  # Colocamos la leyenda
    # plt.title('Immediate reward from arm {}'.format(self.id_arm))  # Colocamos el título del gráfico
    plt.xlabel('Muestras')  # Colocamos la etiqueta en el eje x
    plt.ylabel('Immediate reward %')  # Colocamos la etiqueta en el eje y
    plt.show()


if __name__ == "__main__":
    main()