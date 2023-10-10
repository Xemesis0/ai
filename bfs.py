graph={
    'p': ['q','r','s'],
    'q': ['p','r'],
    'r': ['p','q','t'],
    't': ['r'],
    's': ['p']
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("following is breadth first search")
bfs(visited,graph,'p')
                
