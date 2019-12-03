import collections

def chess(n, a = 1, b = 2):

	moves = [(-a, -b), (-a, b), (a, -b), (a, b), (-b, -a), (-b, a), (b, -a), (b, a)]
	visited = [[False] * n for i in range(n)]
	
	queue = list()
	queue.append([[0, 0], 0])
	visited[0][0] = True

	q = collections.deque(queue)
	while q:
		x, steps = q.popleft()
		#visited[x[0]][x[1]] = True
		if x == [n - 1, n - 1]:
			return steps
		for move in moves:
			target = [x[0] + move[0], x[1] + move[1]]
			if 0 <= target[0] < n and 0 <= target[1] < n and not visited[target[0]][target[1]]:
				q.append([target, steps + 1])
				visited[target[0]][target[1]] = True
	return -1

n = 5
print chess(n, 1, 1)
print chess(n, 1, 2)
print chess(n, 1, 3)
print chess(n, 1, 4)
print chess(n, 3, 3)
print chess(n, 2, 3)
print chess(n, 2, 4)










