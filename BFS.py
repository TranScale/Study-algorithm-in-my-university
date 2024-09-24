#Trần Viết Hải - 225051529, BFS
'''
Thuật toán này là thuật toán tìm kiếm theo chiều rộng, chia đồ thị thành các level rồi tìm dần

vd:         A
           / \
          B   C -- level 1
         / \
        D   E   -- level 2
       /
      F         -- level 3

Như đồ thị trên thì chia thành 3 level(1,2,3), sau đó duyệt theo từng level
'''
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
