import sys
import Main
import NeuralInterface

tiempo = Main.play_level(int(sys.argv[1]), NeuralInterface.feed)
print(tiempo)
