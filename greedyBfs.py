from queue import PriorityQueue

def main():
    graph ={
            'S':{'A':1,'B':4},
            'A':{'B':2,'C':5,'G':12},
            'B':{'C':2},
            'C':{'G':2},
            'G':{}
        }
    H={
        'S':7,
        'A':6,
        'B':2,
        'C':1,
        'G':0
        }
    fn=0
    path=''
    start_node='S'
    path=start_node
    destination_node='G'
    cost,path=greedy_bfs(graph,H,start_node,fn,path,destination_node)
    print(f"The cost from source to destination is {cost} and the path is \n{path}")

def greedy_bfs(graph,H,node,fn,path,destination_node):
    q=PriorityQueue()
    for neighbor in graph[node]:
        q.put((H[neighbor],fn+graph[node][neighbor],f"{path}--->"+neighbor))

    new=q.get()
    path=new[2]
    node=path[-1:]
    fn=new[1]
    if node==destination_node:
        return fn,path
    else: 
        return greedy_bfs(graph,H,node,fn,path,destination_node)


        

if __name__=="__main__":
    main()