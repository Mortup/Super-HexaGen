import sys
import Main

from NeuralDefinitions import *
import random

def crearPoblacion(N):
  poblacion=[]
  for i in range(0,N):
    red = NeuralNetwork(7,(15,),2)
    poblacion.append(red)
  return poblacion

def tenerHijo(padre1,padre2, mutationRate):
  randomIndex = random.randint(0,16)
  childWeights = padre1.getFirstWeightsBias(randomIndex)[0]+padre2.getLastWeightsBias(randomIndex)[0]
  childBias = padre1.getFirstWeightsBias(randomIndex)[1]+padre2.getLastWeightsBias(randomIndex)[1]
  child = NeuralNetwork(7,(15,),2)
  child.buildFromWeightBiasList(childWeights,childBias)
  for i in range(0,16):
    randomMutation = random.uniform(0,1)
    if(randomMutation <= mutationRate):
      if i<=14:
        newChildWeights = PerceptronSigmoide(dim=7)
        child.changeNeuron(i,newChildWeights.getWeights(),newChildWeights.getBias())
      else:
        newChildWeights = PerceptronSigmoide(dim=15)
        child.changeNeuron(i,newChildWeights.getWeights(),newChildWeights.getBias())
  return child

def stopCondition(fitness):
  if fitness>=1000000:
    return False
  else:
    return True

def fitness(red):
    def feed(obstacles, player_angle, player_height):
        close_obs = get_closer_obstacles(obstacles, 100, player_height)
        input = get_space_vector(close_obs)+[player_angle/(2*math.pi)]
        return red.feed(input)
    return Main.play_level(0, feed)

alg = GeneticAlgorithm(fitness,crearPoblacion,tenerHijo,0.10,100, stopCondition)
alg.run()
