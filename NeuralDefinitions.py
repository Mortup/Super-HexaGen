import random
import numpy as np
from NeuralInterface import *
class GeneticAlgorithm:
    def __init__(self, fitnessFun, popGenerator, childGenerator, mutationChance, popSize, stopCondition):
        self.fitnessFun = fitnessFun
        self.population = popGenerator(popSize)
        self.mutationChance = mutationChance
        self.popSize = popSize
        self.childGenerator = childGenerator
        self.stopCondition = stopCondition

    def tournament_selection(self):
        best = None
        for i in range(1, int(len(self.population) / 2)):
            ind = self.population[random.randint(0, self.popSize - 1)]
            if ((best == None) or self.fitnessFun(ind) > self.fitnessFun(best)):
                best = ind
        return best

    def selection(self):
        adecuar = []
        for i in range(0, 2 * self.popSize):
            adecuar.append(self.tournament_selection())
        return adecuar

    def run(self):
        generacion = 0
        while (True):
            generacion += 1
            print("Procesando generacion " + str(generacion))
            new_pop = self.selection()
            self.population = []
            for i in range(0, int(len(new_pop) / 2)):
                padre1 = new_pop.pop(random.randint(0, len(new_pop) - 1))
                padre2 = new_pop.pop(random.randint(0, len(new_pop) - 1))
                child = self.childGenerator(padre1, padre2, self.mutationChance)
                self.population.append(child)
            new_fitnesses = []
            for i in range(0, len(self.population)):
                print("Procesando red "+str(i+1))
                new_fitnesses.append(self.fitnessFun(self.population[i]))
            maxFitness = max(new_fitnesses)
            print(maxFitness)
            maxArg = np.argmax(new_fitnesses)
            if (not self.stopCondition(maxFitness)):
                print(self.population[maxArg].getWeights())
                return self.population[maxArg]


class Perceptron:
    def __init__(self, *args, **kwargs):
        if ('dim' in kwargs):
            self.weights = [0] * kwargs.get('dim')
            for i in range(0, kwargs.get('dim')):
                prob = random.randint(0, 1)
                if prob == 0:  # Pesos entre [-2,-0.5] y [0.5,2]
                    self.weights[i] = random.uniform(0.5, 2)
                else:
                    self.weights[i] = random.uniform(-2, -0.5)
            self.bias = random.uniform(-2, 2)
        else:
            self.weights = args[0]
            self.bias = args[1]

    def feed(self, input):
        calc = 0
        for i in range(len(input)):
            calc += input[i] * self.weights[i]
        return (calc + self.bias > 0)

    def train(self, input, output):
        diff = output - self.feed(input)
        lr = 0.1
        for i in range(0, len(input)):
            self.weights[i] = self.weights[i] + (lr * input[i] * diff)
        self.bias = self.bias + (lr * diff)

    def getWeights(self):
        return self.weights

    def setWeights(self, weights):
        self.weights = weights

    def getBias(self):
        return self.bias

    def setBias(self, bias):
        self.bias = bias


# Perceptron Sigmoide
class PerceptronSigmoide(Perceptron):
    def __init__(self, *args, **kwargs):
        Perceptron.__init__(self, *args, **kwargs)
        self.output = 0
        self.delta = 0

    def feed(self, input):
        calc = 0
        for i in range(len(input)):
            calc += input[i] * self.weights[i]
        self.output = 1 / (1 + math.exp(-calc - self.bias))
        return self.output

    def setDelta(self, delta):
        self.delta = delta

    def getDelta(self):
        return self.delta

    def getOutput(self):
        return self.output


class NeuronLayer():
    def __init__(self, size, input_size):
        self.neurons = []
        self.size = size
        self.input_size = input_size
        for i in range(0, self.size):
            self.neurons.append(PerceptronSigmoide(dim=input_size))

    def feed(self, inputs):
        layer_result = []
        for i in range(0, self.size):
            layer_result.append(self.neurons[i].feed(inputs))
        return layer_result

    def getOutput(self):
        output = []
        for i in range(0, self.size):
            output.append(self.neurons[i].getOutput())
        return output

    def setDelta(self, delta):
        for i in range(0, len(delta)):
            self.neurons[i].setDelta(delta[i])

    def getWeights(self):
        weights = []
        for i in range(0, self.size):
            weights.append(self.neurons[i].getWeights())
        return weights

    def getBias(self):
        bias = []
        for i in range(0, self.size):
            bias.append(self.neurons[i].getBias())
        return bias

    def getNeuron(self, index):
        return self.neurons[index]

    def getSize(self):
        return self.size

    def getNeurons(self):
        return self.neurons


class NeuralNetwork():
    def __init__(self, input_size, hidden_layer_sizes, output_size):
        self.cantCapasOcultas = len(hidden_layer_sizes)
        self.layers = []
        self.output_size = output_size
        first_layer = NeuronLayer(hidden_layer_sizes[0], input_size)
        self.layers.append(first_layer)
        for i in range(1, self.cantCapasOcultas):
            mid_layer = NeuronLayer(hidden_layer_sizes[i], hidden_layer_sizes[i - 1])
            self.layers.append(mid_layer)
        output_layer = NeuronLayer(output_size, hidden_layer_sizes[-1])
        self.layers.append(output_layer)

    def feed(self, inputs):
        if inputs != None:
            for i in range(0, self.cantCapasOcultas + 1):
                inputs = self.layers[i].feed(inputs)
            ret = [bool(round(item)) for item in inputs]
            return ret
        else:
            return [False,False]

    def buildFromWeightBiasList(self, weightList, biasList):
        i = 0
        for layer in self.layers:
            for neuron in layer.getNeurons():
                neuron.setWeights(weightList[i])
                neuron.setBias(biasList[i])
                i = i + 1

    def getFirstWeightsBias(self, n):
        i = 0
        pesos = []
        bias = []
        for layer in self.layers:
            for neuron in layer.getNeurons():
                if i == n:
                    return pesos, bias
                pesos.append(neuron.getWeights())
                bias.append(neuron.getBias())
                i = i + 1

    def getLastWeightsBias(self, n):
        i = 0
        pesos = []
        bias = []
        for layer in self.layers:
            for neuron in layer.getNeurons():
                if i < n:
                    i = i + 1
                    continue
                pesos.append(neuron.getWeights())
                bias.append(neuron.getBias())
                i = i + 1
        return pesos, bias

    def changeNeuron(self, i, weights, bias):
        k = 0
        for layer in self.layers:
            for neuron in layer.getNeurons():
                if k == i:
                    neuron.setWeights(weights)
                    neuron.setBias(bias)
                    return
                k = k + 1

    def getWeights(self):
        pesos = []
        for layer in self.layers:
            for neuron in layer.getNeurons():
                pesos.append(neuron.getWeights())
        return pesos

