import gym
from GAAlgorithm import Genetic
from Gene import Gene
from EvaluationFunction import FitnessFuction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    """
    ga = Genetic()
    gen1 = Gene()
    gen2 = Gene()
    print("Gene1")
    print(gen1.number_chromosomes)
    print(gen1.getinitialChromosomes(), "\n")
    print(gen1.getChromosomes(), "\n")

    print("Gene2")
    print(gen2.number_chromosomes)
    print(gen2.getinitialChromosomes(), "\n")
    print(gen2.getChromosomes(), "\n")

    print("-----")
    kid1, kid2 = ga.Crossover(gen1, gen2)
    print("kid2")
    print(kid2.getinitialChromosomes(), "\n")
    print(kid2.getChromosomes())



    _, kid1 = ga.simpleMutation(kid1)
    print("kid1")
    print(kid1.getChromosomes())
    
    """


    ga = Genetic()
    values = ga.runEvolution()
    plt.plot(values)
    plt.ylabel('Fitness Values')
    plt.xlabel('Generation')
    plt.savefig('SimpleGA_multiCutCrossOver')

    """
    print("Gene2")
    print(gen2.number_chromosomes)
    print(gen2.getChromosomes())

    ga.Crossover(gen1, gen2)
    
    gene = Gene()
    print(gene.getChromosomes())
    fitness = FitnessFuction()
    fitness.runEvaluation(gene)
    
    env = gym.make('BipedalWalker-v2')
    env.reset()
    for _ in range(500):
        env.render()
        action = env.action_space.sample()
        print('Action: ', action)
        observation, reward, done, info = env.step(action)  # take a random action
        print('Reward: ', reward)
    env.close()
    """

main()
