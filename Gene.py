import numpy as np
import random


class Gene:

    def __init__(self):
        self.number_limbs = 4
        self.number_chromosomes = random.randint(1, 14)
        # self.number_chromosomes = 8
        self.chromosomes = np.random.rand(self.number_chromosomes, self.number_limbs) * 2 - 1
        self.numberinitialSteps = random.randint(1, 10)
        # self.numberinitialSteps = 6
        self.initialChromosomes = np.random.rand(self.numberinitialSteps, self.number_limbs) * 2 - 1

    def getChromosomes(self):
        return self.chromosomes

    def setChromosomes(self, newChromosomes):
        self.chromosomes = newChromosomes

    def setNewChromosomeById(self, idLimb, idPart, chromosome):
        self.chromosomes[idLimb][idPart] = chromosome

    def setNewChromosomeByPart(self, idPart, chromosome):
        self.chromosomes[idPart] = chromosome

    def getNumberChromosomes(self):
        return self.number_chromosomes

    def setNumberChromosome(self, number):
        self.number_chromosomes = number

    def getinitialChromosomes(self):
        return self.initialChromosomes

    def getNumberinitialSteps(self):
        return self.numberinitialSteps

    def getInitialChromosome(self):
        return self.initialChromosomes

    def setNewInitialChromosomeById(self, idLimb, idPart, chromosome):
        self.initialChromosomes[idLimb][idPart] = chromosome

    def setInitialChromosome(self, newInitialChoromose):
        self.initialChromosomes = newInitialChoromose

    def setNumberInitialSteps(self, initialNumber):
        self.numberinitialSteps = initialNumber

    """
        # execute the EliteCrossover
        qtdEliteChildren = int(self.eliteSize)
        for c in range(0, qtdEliteChildren):
            # get the parents  -- check if I need to remove duplicated fathers
            father1 = self.inArraySelection(new_pop, self.eliteSize)
            father2 = self.inArraySelection(new_pop, self.eliteSize)

            # crossover to generate 2 new kids
            kid1, kid2 = self.Crossover(father1, father2)

            # append the new genes
            new_pop.append((self.eval.runEvaluation(kid1), kid1))
            new_pop.append((self.eval.runEvaluation(kid2), kid2))
    """