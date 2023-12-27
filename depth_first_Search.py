import sys 

def main():
    stack=[]
    visited_node=[]
    graph ={
            'S':{'A':1,'B':4},
            'A':{'B':2,'C':5,'G':12},
            'B':{'C':2},
            'C':{'G':2},
            'G':{}
        }
    if len(sys.argv)<2:
        sys.exit("No destination node ")

    destination_node=sys.argv[1]
    node=list(graph.keys())[0]
    stack.append(node)
    print(depth_first_Search(graph,stack,destination_node,visited_node))
    print(visited_node)

def depth_first_Search(graph,stack,destination_node,visited_node):
    while stack:
        node=stack.pop()
        if node not in visited_node :
            for new_node in graph[node]:
                stack.append(new_node)
            visited_node.append(node)
            if node==destination_node:
                return "the search element is found"
            
    if not stack:
                return "No destination node found "

if __name__=="__main__":
    main()
