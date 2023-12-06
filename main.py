import random


def searchMin(visited, unvisited):
	minim = 1000000
	minIndex = ()
	for i in visited:
		for j in unvisited:
			print("(" + str(i + 1) + ", ", str(j + 1) + ", ", str(matrix[i][j]) + ")", end=', ')
			if 0 < matrix[i][j] < minim:
				minim = matrix[i][j]
				minIndex = (i, j)
	print()
	return minIndex


def reCountQ(visited):
	counter = 0.0
	for i in range(1, len(visited)):
		counter += matrix[visited[i]][visited[i - 1]]
	return counter



f = open("matrix.txt")
matrix = []
for i in f:
	matrix.append([float(x) for x in i.split()])

N= len(matrix)
print()
print("Работаем с матрицей: ")
for i in matrix:
	for j in i:
		print(j, end=' ')
	print()
print()

Q = 0
unvisitedCities = [i for i in range(0, N)]
currentCity = random.choice(unvisitedCities)
firstCity = currentCity
unvisitedCities.remove(currentCity)
visitedCities = [currentCity]

for i in range(0, N - 1):
	print("Шаг " + str(i + 1) + ":")
	print("Текущий обход: " + str(list(map(lambda x: x + 1, visitedCities))))
	print("Текущая длина обхода: " + str(round(Q, 2)))
	print("Кандидаты: ", end='')
	currentCity = searchMin(visitedCities, unvisitedCities)
	print("Выбран кандидат: (" + str(currentCity[0] + 1) + ", " + str(currentCity[1] + 1) + ", " + str(
		matrix[currentCity[0]][currentCity[1]]) + ")")
	for j in visitedCities:
		if j == currentCity[0]:
			visitedCities.insert(visitedCities.index(j) + 1, currentCity[1])
			break
	Q = reCountQ(visitedCities)
	unvisitedCities.remove(currentCity[1])
	print()

print("Шаг " + str(N) + ":")
print("Текущий обход: " + str(list(map(lambda x: x + 1, visitedCities))))
print("Текущая длина обхода: " + str(round(Q, 2)))
print("Возвращаемся в начальный город: " + str(firstCity + 1))
visitedCities.append(firstCity)
Q = reCountQ(visitedCities)
print()
print("Итоговый обход: " + str(list(map(lambda x: x + 1, visitedCities))))
print("Итоговая длина пути: " + str(round(Q, 2)))