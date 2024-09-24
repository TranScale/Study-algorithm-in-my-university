#Trần Viết Hải - 225051529

graph = {
    '0':[('1',2),('2',6)],
    '1':[('0',2),('3',5)],
    '2':[('0',6),('3',8)],
    '3':[('1',5),('2',8),('4',10),('5',15)],
    '4':[('3',10),('5',6),('6',2)],
    '5':[('3',15),('4',6),('6',6)],
    '6':[('4',2),('5',6)],
}
import heapq
def Dijkstra(graph,start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(start,0)]
    while queue:
        now_Node, now_Distance = heapq.heappop(queue)

        if now_Distance > distances[now_Node]:
            continue

        for neighbour, weight in graph[now_Node]:
            distance = now_Distance+weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance

            heapq.heappush(queue,(neighbour,distance))
    return distances

print("Hello World")
a = Dijkstra(graph,'0')
print(a)
