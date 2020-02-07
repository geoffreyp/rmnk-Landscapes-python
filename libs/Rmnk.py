import random
import numpy as np
"""
  Fitness function of the rMNK-landscapes
  reading a rhoMNK-landscapes instance file in python 3
  Other examples are available in C, C++ or java : http://svn.code.sf.net/p/mocobench/code/trunk/rmnk/generator/

  rhoMNK-landscapes instances can be generated with 
  the rmnkGenerator.R available here : http://svn.code.sf.net/p/mocobench/code/trunk/rmnk/generator/rmnkGenerator.R

  More information on rhoMNK-landscapes, see original paper:
  Verel S., Liefooghe A., Jourdan L., Dhaenens C. "Analyzing the Effect of Objective Correlation on the Efficient 
  Set of MNK-Landscapes", In Proceedings of Learning and Intelligent OptimizatioN Conference (LION 5), LNCS, p. , 2011.
 """


class Rmnk:

    def __init__(self, instance_file):
        file_rmnk = open(instance_file, 'r')
        file_content = list(map(str.strip, file_rmnk.readlines()))
        file_content = file_content[3:]

        definition = file_content[0].split(" ")
        self.rho = float(definition[2])
        self.m = int(definition[3])
        self.n = int(definition[4])
        self.k = int(definition[5])

        self.links = np.zeros((self.m, self.n, self.k + 1))
        self.tables = np.zeros((self.m, self.n, 1 << (self.k + 1)))

        file_content = file_content[2:]
        line = self.load_links(file_content)

        file_content = file_content[line+1:]
        self.load_tables(file_content)

    def f(self, function_id, solution):
        accu = 0

        for i in range(self.n):
            accu += self.tables[function_id][i][self.sigma(function_id, solution, i)]

        return -1 * (accu / self.n)

    def sigma(self, function_id, solution_array, item):
        n = 1
        accu = 0

        for j in range(self.k + 1):
            link = int(self.links[function_id][item][j])
            if solution_array[link]:
                accu = accu | n

            n = n << 1

        return accu

    def generate_random_solution(self):
        solution = []
        for i in range(0, self.n):
            solution.append(random.getrandbits(1))

        return solution

    def load_links(self, array):
        line = 0
        for i in range(self.n):
            for j in range(self.k + 1):
                s = array[line].split("  ")
                line += 1
                for n in range(self.m):
                    self.links[n][i][j] = float(s[n])

        return line

    def load_tables(self, array):
        line = 0
        for i in range(self.n):
            for j in range(1 << (self.k + 1)):
                s = array[line].split("  ")
                line += 1
                for n in range(self.m):
                    self.tables[n][i][j] = float(s[n])
