import math
from City import City
from math import hypot

class Solution:
	'''
	Classe qui regroupe un ensemble de Ville formant un chemin et une distance totale (evaluation)
	'''
	def __init__(self, cities):
		self._cities = cities

		if len(cities) > 0:
			self.evaluate()
		else:
			self._evaluation = 0

	# Evaluation en fonction des distances entre les villes
	def evaluate(self):
		length = 0
		for i in range(len(self._cities) - 1):
			cityA = self._cities[i]
			cityB = self._cities[i + 1]
			length += getPythagoreDistance(cityA, cityB)

		length += getPythagoreDistance(self._cities[0], self._cities[-1])
		self._evaluation = length

	def clone(self):
		return Solution(self._cities[:])

	def add(self, city):
		self._cities.append(city)
		self._evaluation = self.evaluate()

	def __repr__(self):
		names = ""
		for city in self._cities:
			names += city._name + ", "
		names += "(" + str(self._evaluation) + ")\n"
		return names

	@property
	def evaluation(self):
		return self._evaluation

	@property
	def cities(self):
		return self._cities

	# Recuperation d'une liste de tuple (x,y) pour l'affichage sur le GUI
	def getPoints(self):
		points = []
		for city in self._cities:
			points.append((city.x, city.y))
		return points

	# utilisé pour accéder aux villes contenues dans une Solution
	def __getitem__(self, item):
		return self._cities[item]

	def __setitem__(self, key, value):
		self._cities[key] = value

	def __len__(self):
		return len(self._cities)

	def __iter__(self):
		for city in self._cities:
			yield city

	#Fonction pour savoir si une ville appartient a la solution
	def contains(self, citySrc):
		for city in self._cities:
			if city == citySrc:
				return True
		return False


	def getDict(self):
		dico = dict()
		for city in self._cities:
			dico[city._name] = (city._x, city._y)

		return dico

	def getCities(self):
		cityList = []
		for city in self._cities:
			cityList.append(city.name)
		return cityList

	def swap(self, a, b):
		self._cities[a], self._cities[b] = self._cities[b], self._cities[a]

	def index(self, city):
		return self._cities.index(city)

	def decal(self, n):
		self._cities = self._cities[n:] + self._cities[:n]



# Retourne le distance entre 2 villes
def getPythagoreDistance(cityA, cityB):
	return hypot(cityB.x - cityA.x, cityB.y - cityA.y)


def getDistanceManathan(cityA, cityB):
	return abs(cityB.x - cityA.x) + abs(cityB.y - cityA.y)

def getDistanceChessboard(cityA, cityB):
	return max(abs(cityA.x - cityB.x),abs(cityA.y - cityB.y))

## Test unitaire !
if __name__ == '__main__':
	cities = []
	c1 = City(0, 0)
	c2 = City(0, 5)
	c3 = City(0, 10)
	c4 = City(0, 15)
	cities.append(c1)
	cities.append(c2)
	cities.append(c3)
	cities.append(c4)

	solution = Solution(cities)
	length = solution.evaluate()
	print(length)