#Trần Viết Hải - 225051529, Bài tập Prim's MST
'''
Thuật toán này là thuật toán tìm kiếm đường đi ngắn nhất, tối ưu nhất trong thời điểm mà nó tìm kiếm,
không quan tâm đến những vấn đề phát sinh phía sau.

vd: A -- 2 -- B -- 10 -- D
    A -- 3 -- C -- 5 -- D
Mục tiêu: A đến D
Theo ví dụ trên thì thuật toán Prim sẽ chọn điểm B làm điểm kế tiếp do 2 < 3, không quan B đến D tốn 10 mà C đến D chỉ tốn 5
'''
import heapq
graph = {
    'A':[('C',6)],
    'B':[('C',10),('D',4)],
    'C':[('A',6),('B',10),('D',2),('E',3)],
    'D':[('B',4),('C',2),('E',1)],
    'E':[('C',3),('D',1)]
}

def Prim(graph,start):
    mst = []
    visited = set()
    waitlist = [(0,start,None)]
    while waitlist:
        weight, you, parent = heapq.heappop(waitlist)

        if you in visited:
            continue

        visited.add(you)

        if parent is not None:
            mst.append((parent,you,weight))
        
        for v,w in graph[you]:
            if v not in visited:
                heapq.heappush(waitlist,(w,v,you))

    return mst
        


print(Prim(graph,'A'))

