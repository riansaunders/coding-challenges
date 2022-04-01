from typing import *


def ninjaTraining( points: List[List[int]]) -> int:

	dp = {} 

	def f(day, last):
		if (day, last) in dp:
			return dp[(day, last)]

		if day == 0:
			maximum = 0
			for i in range(3):
				if i == last:
					continue
				maximum = max(maximum, points[day][i])
			return maximum
		maximum = 0
		for i in range(3):
			if i == last:
				continue
			maximum = max(maximum,  f(day - 1, i) + points[day][i])

		dp[(day,last)] = maximum
		return maximum
		
	return f(len(points) - 1, 3)

def efficient( points: List[List[int]]) -> int: 

	dp2 = [[0,3] for _ in range(len(points))]
	for i in range(3): 
		dp2[0] = [max(points[0][i], dp2[0][0]), i]

	for i in range(1, len(dp2)):
		for j in range(3):
			if j == dp2[i][1]:
				continue
			dp2[i] = [max(dp2[i][0], dp2[i - 1][0] + points[i][j]), j]

	return dp2[len(points) - 1][0] 

def efficientOptimized( points: List[List[int]]) -> int: 

	prev = [0] * 4

	prev[0] = max(points[0][1], points[0][2])
	prev[1] = max(points[0][0], points[0][2])
	prev[2] = max(points[0][0], points[0][1])
	prev[3] = max(points[0][0], points[0][1], points[0][2])
	for day in range(1, len(points)):
		tmp = [0] * 4
		for last in range(1, 4):
			tmp[last] = 0
			for task in range(3):
				if task != last:
					tmp[last] = max(tmp[last], points[day][task] + prev[task])
		prev = tmp
	return prev[3]

# print(ninjaTraining(
# [
# [18, 11, 19],
# [4, 13, 7],
# [1, 8, 13]
#  ]
# ))

print(efficient(
	[
		[1,2,5], 
		[3 ,1 ,1],
		[3,3,3]
	]
)) 
print(efficientOptimized(
	[
		[1,2,5],
		[3 ,1 ,1],
		[3,3,3]
	]
))