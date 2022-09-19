import numpy as np
import matplotlib.pyplot as plt
import random as rnd


class Accion:
    def __init__(self, id_arm, muestras, media, varianza):
        self.id_arm = id_arm
        self.muestras = muestras
        self.media = media
        self.varianza = varianza
        self.immediate_rewards = []

        self.fill_immediate_reward_vector()
        print("bobo")

    def get_immediate_rewards(self):
        return self.immediate_rewards

    def calc_immediate_reward(self):
        return rnd.gauss(self.media, self.varianza)

    def fill_immediate_reward_vector(self):
        for i in range(self.muestras + 1):
            self.immediate_rewards.append(self.calc_immediate_reward())

    def print_immediate_rewards(self):
        print("These are the immediate rewards of Arm {}".format(self.id_arm))
        print(self.immediate_rewards)

    def plot_immediate_reward(self, muestra_inicial, muestra_final):
        y = self.immediate_rewards
        x = np.arange(self.media - self.varianza, self.media + self.varianza, self.varianza * 2 / self.muestras)
        plt.plot(x, label="x_k", linewidth=2)
        plt.plot(y, label="r_k", linewidth=2)
        plt.grid(True)
        plt.legend()  # Colocamos la leyenda
        plt.title('Immediate reward from arm {}'.format(self.id_arm))  # Colocamos el título del gráfico
        plt.xlabel('Muestras')  # Colocamos la etiqueta en el eje x
        plt.ylabel('Immediate reward %')  # Colocamos la etiqueta en el eje y
        plt.show()