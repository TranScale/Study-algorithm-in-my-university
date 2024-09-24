#Trần Viết Hải - 225051529
'''
Thuật toán này là thuật toán tìm kiếm đường đi ngắn nhất từ đỉnh gốc đến các đỉnh khác,


vd: A -- 2 -- B -- 10 -- D 
    A -- 3 -- C -- 5 -- D
Mục tiêu: A đến D
Theo thuật toán Dijkstra, thì thuật toán sẽ chọn hướng tối ưu nhất là đỉnh C vì:
    - Khoảng cách A đến C: 3
    - Khoảng cách C đến D: 10
    --> Vậy khoảng cách A đến D: 3 + 5 = 8
Vậy nếu A đến D bằng 6 thì nó sẽ chọn đến D hay C ??
    A -- 6 -- D
Theo Prim, thì thuật toán sẽ chọn đường ngắn nhất trong thời điểm nó xét thì đó là B do A đến B có 2.
Nhưng theo Dijkstra, thì thuật toán sẽ chọn D ngay vì lúc này khoảng cách A đến D chỉ có 6.
'''
import heapq
graph = {
    '0':[('1',2),('2',6)],
    '1':[('0',2),('3',5)],
    '2':[('0',6),('3',8)],
    '3':[('1',5),('2',8),('4',10),('5',15)],
    '4':[('3',10),('5',6),('6',2)],
    '5':[('3',15),('4',6),('6',6)],
    '6':[('4',2),('5',6)],
}

def Dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(start, 0)]
    while queue:
        nowNode , nowDistance =  heapq.heappop(queue)

        if nowDistance > distances[nowNode]:
            continue

        for neighbour, weight in graph[nowNode]:
            distance = nowDistance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(queue,(neighbour,distance))
    return distances
    
a = Dijkstra(graph,'0')
print(a)
