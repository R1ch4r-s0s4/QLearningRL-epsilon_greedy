import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from epsilon_greedy import Epsilon_Greedy
from itertools import count


class ActionValue:
    def __init__(self, brazos, muestras):
        self.brazos = brazos
        self.muestras = muestras
        self.cummulative_reward = []
        self.mean_value = []
        self.qvalues_k = [0, 0, 0, 0]
        self.qvalues = []
        self.CR = np.array([0.0, 0.0, 0.0, 0.0])
        self.epsilon_tradeoff = 0.0
        self.policy1 = Epsilon_Greedy(self.epsilon_tradeoff, [2.3, 2.1, 1.5, 1.3])

    def set_epsilon(self, epsilon_tradeoff):
        self.epsilon_tradeoff = epsilon_tradeoff

    def UpdateQa(self):

        R_4xmuestras = []
        r_k = []
        for i in range(len(self.brazos)):
            R_4xmuestras.append(self.brazos[i].get_immediate_rewards())
        Rk = np.array(R_4xmuestras)
        # print(Rk)
        # print(Rk[0][0])
        Vast = 0
        prom = 0
        for k in range(self.muestras):
            r_k.clear()

            # print(r_k)
            # print(V_ast)

            Arm = self.policy1.seleccion(self.epsilon_tradeoff, self.qvalues_k)
            if k == 0:
                Arm = self.policy1.ramdom_action()
            for i in range(len(self.brazos)):
                r_k.append(R_4xmuestras[i][k + 1])

            self.cummulative_reward.append(self.CR[Arm])
            self.mean_value.append(prom)
            # self.CR[Arm]=self.CR[Arm] + 1/(k + 1)*(r_k[Arm]-self.CR[Arm])

            self.CR[Arm] = self.CR[Arm] + 0.1 * (r_k[Arm] - self.CR[Arm])
            Vast = Vast + self.CR[Arm]
            if (k >= 1):
                prom = Vast / k

            # Vast=Vast + 1/(k + 1)*(r_k[Arm]-self.CR[Arm])

            self.qvalues_k = self.CR.tolist()
            self.qvalues.append(self.CR.T.tolist())

            print(k, self.CR, r_k)
        # Q=np.array(self.qvalues)
        # print(Q)
        # plt.figure(1)
        self.graficarCR()
        self.plot_Qvalues_per_arm()

    def get_mean_CR(self):
        return self.mean_value

    def graficarCR(self):

        x = self.mean_value
        # x=np.arange(self.media - self.varianza, self.media + self.varianza, self.varianza*2/self.muestras)
        # plt.figure(1)
        plt.plot(x, label="V*")
        # plt.plot(y,label = "r_k", linewidth = 2)
        plt.grid(True)
        plt.legend()  # Colocamos la leyenda
        plt.title('Cummulative reward ')  # Colocamos el título del gráfico
        plt.xlabel('Samples')  # Colocamos la etiqueta en el eje x
        plt.ylabel('Cummulative reward ')  # Colocamos la etiqueta en el eje y
        plt.show()

    def plot_Qvalues_per_arm(self):
        bra = []
        for i in range(len(self.brazos)):
            bra.append(self.brazos[i].id_arm)
        plt.plot(self.qvalues, linewidth=1)
        plt.grid(True)
        plt.legend()  # Colocamos la leyenda
        plt.title('Cummulative reward ')  # Colocamos el título del gráfico
        plt.xlabel('Samples')  # Colocamos la etiqueta en el eje x
        plt.ylabel('Cummulative reward ')  # Colocamos la etiqueta en el eje y
        plt.show()
