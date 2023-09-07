import queue

q = queue.PriorityQueue() 
# allowes you to give every element a sertain priority,
# the less is the number the more priroty it has, example: 1 has more priority than 100 

q.put((2, "Hello world"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
  print(q.get()[1])