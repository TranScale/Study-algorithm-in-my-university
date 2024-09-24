#Trần Viết Hải - 225051529, BFS

from collections import deque


graph = {
    'M':['P','F'],
    'P':['A','B'],
    'F':['Z','T'],
    'A':['O','B'],
    'B':['Z'],
    'T':['C'],
    'C':[],
    'O':[],
    'Z':[]
}

def bfs(graph,start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

print(bfs(graph,'M'))
