import numpy as np
import matplotlib.pyplot as plt
import random as rnd


class Epsilon_Greedy:
    def __init__(self, epsilon_tradeoff, qvalues_k):
        self.epsilon_tradeoff = epsilon_tradeoff
        self.qvalues_k = qvalues_k
        print(len(qvalues_k), max(qvalues_k))

    def seleccion(self, epsilon_tradeoff, qvalues_k):
        self.epsilon_tradeoff = epsilon_tradeoff
        self.qvalues_k = qvalues_k
        Rnd = np.random.uniform(0, 1)

        if (Rnd < (1 - self.epsilon_tradeoff)):
            a = max(self.qvalues_k)
            i = self.qvalues_k.index(a)
            # print("EG El brazo {}y el #rnd {}".format(max(self.qvalues_k), Rnd))
            return i
        else:
            # print("El brazo {}y el #rnd {}".format(self.ramdom_action(), Rnd))
            return self.ramdom_action()

    def ramdom_action(self):
        R = np.random.uniform(0, 1)
        portions = 1 / len(self.qvalues_k)
        return int(R // portions)  # This step ensures to obtain qvalues_k uniformly