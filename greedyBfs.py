
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
    print(graph)
    print(H)


if __name__=="__main__":
    main()