'''
0 0 0 0 0
0 2 3 0 1
0 8 5 0 7
7 0 0 0 4

Output should be groups of clusters:
Cluster 1: <2,3,8,5,7>
Cluster 2: <1,7,4>
'''

def dfs(val, A, V, x, y):
	if x < 0 or x >= len(A):
		return
	if y < 0 or y >= len(A[0]):
		return
	if V[x][y]:
		return

	if A[x][y] == 0:
		V[x][y] = True
		return
	V[x][y] = True
	val.append(A[x][y])

	row_x = [-1, -1, -1,  0, 0,  1, 1, 1]
	col_y = [-1,  0,  1, -1, 1, -1, 0, 1]

	for k in xrange(8):
		dfs(val, A, V, x + row_x[k], y + col_y[k])


def cluster(A):
	row = len(A)
	col = len(A[0])
	result = {}
	count = 0

	visited = [[False for j in range(col)] for i in range(row)]
	
	for i in xrange(row):
		for j in xrange(col):

			if visited[i][j]:
				continue

			if A[i][j] == 0:
				visited[i][j] = True
				continue

			count += 1

			result[count] = []
			dfs(result[count], A, visited, i, j)

	return result



a1 = [[0, 0, 0, 0, 0], [0, 2, 3, 0, 1], [0, 8, 5, 0, 7], [7, 0, 0, 0, 4]]
print cluster(a1)

a2 = [[1, 2, 0, 0, 0], [0, 0, 0, 0, 0], [0, 2, 3, 0, 1], [0, 8, 5, 0, 7], [7, 0, 0, 0, 4]]
print cluster(a2)
