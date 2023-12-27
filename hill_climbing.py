from queue import PriorityQueue
from a_Star import next_state

def main():
    cost_path=float('inf')
    state=[]
    path_queue=PriorityQueue()
    q=PriorityQueue()
    graph ={
        'S':{'A':1,'G':12},
        'A':{'B':3,'C':1},
        'B':{'D':3},
        'C':{'D':1,"G":2},
        'D':{'G':3},
        'G':{}
    }
    H={
        's':40,
        'A':20,
        'B':60,
        'C':20,
        'D':30,
        'G':0
    }
    start_node='S'
    next_state(graph,start_node,'S',H,q,0,path_queue,cost_path)
    possible_state=path_queue.get()
    print(f"The path for the graph is :\n{possible_state[1]} \nand cost is {possible_state[0]}")

if __name__=="__main__":
    main()

