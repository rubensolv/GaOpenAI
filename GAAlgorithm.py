import random
import numpy as np
from Gene import Gene
from EvaluationFunction import FitnessFuction

class Genetic:
    def __init__(self):
        # variable used to define the probability of a gene be mutated.
        self.mutationRate = 0.2  #test
        self.populationSize = 500  #defined by the same quantity
        self.generationsLimit = 100  # same used by Levi
        self.eliteSize = 100  #10% of the pop size
        self.selectTournamentSize = 40  # 8% of the pop size
        self.eval = FitnessFuction()
        self.invasionSize = 10

    def Crossover(self, gene1, gene2):
        kid1 = Gene()
        kid2 = Gene()
        # crossover genes
        maxSize = gene1.getNumberChromosomes()
        if gene2.getNumberChromosomes() < gene1.getNumberChromosomes():
            maxSize = gene2.getNumberChromosomes()

        ckid1 = np.random.rand(maxSize, gene1.number_limbs) * 2 - 1
        ckid2 = np.random.rand(maxSize, gene1.number_limbs) * 2 - 1
        cutPosition = random.randint(1, gene1.number_limbs - 1)
        for i in range(0, maxSize):
            tChromo1 = np.array_split(gene1.getChromosomes()[i], [cutPosition])
            tChromo2 = np.array_split(gene2.getChromosomes()[i], [cutPosition])
            ckid1[i] = np.concatenate((tChromo1[0], tChromo2[1]), axis=None)
            ckid2[i] = np.concatenate((tChromo2[0], tChromo1[1]), axis=None)

        kid1.setChromosomes(ckid1)
        kid1.setNumberChromosome(maxSize)
        kid2.setChromosomes(ckid2)
        kid2.setNumberChromosome(maxSize)

        #crossover initial genes
        maxSize = gene1.getNumberinitialSteps()
        if gene2.getNumberinitialSteps() < gene1.getNumberinitialSteps():
            maxSize = gene2.getNumberinitialSteps()

        ckid1 = np.random.rand(maxSize, gene1.number_limbs) * 2 - 1
        ckid2 = np.random.rand(maxSize, gene1.number_limbs) * 2 - 1
        cutPosition = random.randint(1, gene1.number_limbs - 1)
        for i in range(0, maxSize):
            tChromo1 = np.array_split(gene1.getInitialChromosome()[i], [cutPosition])
            tChromo2 = np.array_split(gene2.getInitialChromosome()[i], [cutPosition])
            ckid1[i] = np.concatenate((tChromo1[0], tChromo2[1]), axis=None)
            ckid2[i] = np.concatenate((tChromo2[0], tChromo1[1]), axis=None)

        kid1.setInitialChromosome(ckid1)
        kid1.setNumberInitialSteps(maxSize)
        kid2.setInitialChromosome(ckid2)
        kid2.setNumberInitialSteps(maxSize)


        # kid1.setNewChromosomeByPart(i, np.concatenate((tChromo1[0], tChromo2[1]), axis=None))
        # kid2.setNewChromosomeByPart(i, np.concatenate((tChromo2[0], tChromo1[1]), axis=None))

        # print(gene1.getChromosomes())
        # print(gene2.getChromosomes())

        # print(kid1.getChromosomes())
        # print(kid2.getChromosomes())
        return kid1, kid2

    def fullMutation(self, population):
        mutatePop = []
        for p in range(0, self.populationSize):
            wasMutated, newGene = self.simpleMutation(population[p][1])
            if wasMutated:
                mutatePop.append((self.eval.runEvaluation(newGene), newGene))
            else:
                mutatePop.append((population[p][0], newGene))
        return mutatePop

    """
        Simple Mutation change one chromosome in one of the limbs in the gene.
    """
    def simpleMutation(self, gene):
        if random.random() <= self.mutationRate:
            newGeneValue = np.random.rand(1, 1)
            posLimb = random.randint(0, gene.number_limbs - 1)
            if random.random() <= (self.mutationRate * 2):
                posChro = random.randint(0, gene.getNumberinitialSteps() - 1)
                gene.setNewInitialChromosomeById(posChro, posLimb, newGeneValue[0])
            else:
                # print("old", gene.getChromosomes())
                posChro = random.randint(0, gene.number_chromosomes - 1)
                gene.setNewChromosomeById(posChro, posLimb, newGeneValue[0])
                # print("new", gene.getChromosomes())
            return True, gene
        else:
            return False, gene

    def randomSelection(self, population):
        idGene = random.randint(0, len(population) - 1)
        return population[idGene][1]

    def tournamentSelection(self, population):
        tempPopulation = []
        for i in range(0, self.selectTournamentSize):
            idTorn = random.randint(0, self.populationSize - 1)
            tempPopulation.append((population[idTorn][0], population[idTorn][1]))
        tempPopulation.sort(reverse=True, key=lambda gene: gene[0])
        return tempPopulation[0][1]

    def inArraySelection(self, population, size):
        idGene = random.randint(0, size - 1)
        return population[idGene][1]

    def EliteSelection(self, population):
        idGene = random.randint(0, self.populationSize - 1)
        return population[idGene][1]

    def runEvolution(self):
        population = []
        valuesPlot = []
        for _ in range(0, self.populationSize):
            gene = Gene()
            rewardValue = self.eval.runEvaluation(gene)
            population.append((rewardValue, gene))

        for generation in range(0, self.generationsLimit):
            population.sort(reverse=True, key=lambda gene: gene[0])
            print("Best gene in generation ", generation)
            print(population[0][0])
            #print(population[0][1].getChromosomes())
            valuesPlot.append(population[0][0])

            # new population
            # print("initial population")
            #self.printPopulation(population)
            new_pop = []
            # get the elite members
            for nElite in range(0, self.eliteSize):
                new_pop.append((population[nElite][0], population[nElite][1]))

            # new genes invading the population
            for c in range(0, self.invasionSize):
                gene = Gene()
                rewardValue = self.eval.runEvaluation(gene)
                new_pop.append((rewardValue, gene))

            # execute the SimpleCrossover (modify after EliteCrossover)
            qtdSimpleChildren = int((self.populationSize - len(new_pop)) / 2)
            for c in range(0, qtdSimpleChildren):
                # get the parents  -- check if I need to remove duplicated fathers
                father1 = self.tournamentSelection(population)
                father2 = self.tournamentSelection(population)

                # crossover to generate 2 new kids
                kid1, kid2 = self.Crossover(father1, father2)

                # append the new genes
                new_pop.append((self.eval.runEvaluation(kid1), kid1))
                new_pop.append((self.eval.runEvaluation(kid2), kid2))


            population = self.fullMutation(new_pop)
        return valuesPlot


    def printPopulation(self, population):
        for i in range(0, self.populationSize):
            print("gene", population[i][0], population[i][1].getChromosomes())
