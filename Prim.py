#Trần Viết Hải - 225051529, Bài tập Prim's MST
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

