from  queue import PriorityQueue


q=PriorityQueue()
q.put(2,'A')

first,last=q.get()
print(f"{first},{last}")