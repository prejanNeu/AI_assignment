from queue import Queue
import sys

def main():
    que=Queue()

    graph ={
            'S':{'A':1,'B':4},
            'A':{'B':2,'C':5,'G':12},
            'B':{'C':2},
            'C':{'G':2},
            'G':{}
        }
    visited_node=[]
    if len(sys.argv)<2:
        sys.exit("No destination node ")
    destination_node=sys.argv[1]
    node=list(graph.keys())[0]
    que.put(node)
    breadthFirstSeawrch(graph,que,node,destination_node,visited_node)
    print(visited_node)


def breadthFirstSeawrch(graph,que,node,destination_node,visited_node):
    while not que.empty():
        node=que.get()
        visited_node.append(node)
        if node==destination_node:
            break
        for neighbor in graph[node]:
            if neighbor not in visited_node and neighbor not in que.queue:
                que.put(neighbor)
        

if __name__=="__main__":
    main()

