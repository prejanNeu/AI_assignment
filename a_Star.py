from queue import PriorityQueue

def main():
    cost_path=float('inf')
    state=[]
    path_queue=PriorityQueue()
    q=PriorityQueue()
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
    start_node='S'
    next_state(graph,start_node,'S',H,q,0,path_queue,cost_path)
    possible_state=path_queue.get()
    print(f"The path for the graph is :\n{possible_state[1]} \nand cost is {possible_state[0]}")

def next_state(graph,node,path,H,q,fn,path_queue,cost_path):
    while(True):
        for neighbors in graph[node]:
            q.put((graph[node][neighbors]+H[neighbors]+fn,fn+graph[node][neighbors],f'{path}--->'+neighbors))
        if q.empty():
            return None
        new=q.get()
        path=new[2]
        # print(path)
        node=path[-1:]
        fn=new[1]
        # print(path)
        if node=='G':
            if cost_path>new[1]:
                cost_path=new[1]
            path_queue.put((new[1],new[2]))
        if not path_queue.empty():
            if cost_path>new[1]:
                next_state(graph,node,path,H,q,fn,path_queue,cost_path)
    
if __name__=="__main__":
    main()