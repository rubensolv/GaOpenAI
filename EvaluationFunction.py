import numpy as np
import random
import gym


class FitnessFuction:

    def __init__(self):
        self.env = gym.make('BipedalWalker-v2')
        self.playoutSize = 500

    def runEvaluation(self, gene):
        self.env.reset()
        contAction = 0
        sumReward = 0

        for c in range(0, gene.getNumberinitialSteps()):
            step = gene.getInitialChromosome()[c]
            _, reward, _, _ = self.env.step(step)
            sumReward += reward

        """
        for _ in range(0, self.playoutSize):
                """
        # print("Gene ", gene.getChromosomes(), "\n")
        for _ in range(0, self.playoutSize - gene.getNumberinitialSteps()):
            # self.env.render()
            step = gene.getChromosomes()[contAction]
            # print(step)
            _, reward, _, _ = self.env.step(step)
            sumReward += reward
            contAction += 1
            if contAction == gene.getNumberChromosomes():
                contAction = 0
        # print(sumReward)
        return sumReward
