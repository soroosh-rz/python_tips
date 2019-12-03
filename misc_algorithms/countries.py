def dfs(val, B, A, x, y, z):
    
    if x < 0 or x >= len(A):
        return
    if y < 0 or y >= len(A[0]):
        return
    if not B[x][y] :
        return
    if A[x][y] != val:
        return
    B[x][y] = False
    z[0] += 1
    dfs(val, B, A, x + 1, y, z)
    dfs(val, B, A, x - 1, y, z)
    dfs(val, B, A, x, y - 1, z)
    dfs(val, B, A, x, y + 1, z)

def countries_count( A ):
    B = [[True for x in A[0]] for y in A]
    
    count = 0
    size_area = {}
    
    for x in xrange(0, len(A)):
        for y in xrange(0, len(A[x])):
            
            # if False continue
            if not B[x][y]:
                continue

            count += 1
            size_cnt = [0]

            dfs(A[x][y], B, A, x, y, size_cnt)
            size_area[count] = size_cnt[0]

    print size_area
    return count 

A1 = [[5,4,4],[4,3,4],[3,2,4],[2,2,2],[3,3,4],[1,4,4],[4,1,1]]
A2 = [[1,1,2],[3,2,2]]

'''
5  4  4
4  3  4
3  2  4
2  2  2
3  3  4
1  4  4
4  1  1
'''

print countries_count( A1 )
print countries_count( A2 )
