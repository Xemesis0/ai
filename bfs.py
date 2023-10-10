graph={'P':['Q','R','S'],
       'Q':['P','R'],
       'R':['P','Q','T'],
       'T':['R'],
       'S':['P']
}
visited=[]
queue=[]

def bfs(visited,graph,node):
  visited.append(node)
  queue.append(node)

  while queue:
    s=queue.pop(0)
    print(s,end = "")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited,graph, 'P')
