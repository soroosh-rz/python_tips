

N = 30
jump = 6
queue = []  # empty queue
visited = [False] * N

mappings = {}
mappings[2] = 21
mappings[4] = 7
mappings[10] = 25
mappings[19] = 28

mappings[26] = 0
mappings[20] = 8
mappings[16] = 3
mappings[18] = 6


visited[0] = True
entry = (0, 0)  # (vertex, step)
queue.append(entry)


while queue:
    vertex, step = queue.pop(0)
    print vertex
    print step

    if vertex == N - 1:
        break

    visited[vertex] = True
    step += 1

    neighbors = [nbr for nbr in range(1+vertex, 1+vertex+jump) if nbr < 30]
    print neighbors


    for nbr in neighbors:
        if not visited[nbr]:
            if nbr in mappings.keys():
                queue.append((mappings[nbr], step))
                visited[mappings[nbr]] = True
            else:
                queue.append((nbr, step))
                visited[nbr] = True

    print queue
    print visited
    print "\n"






