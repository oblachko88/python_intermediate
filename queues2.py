import queue
q = queue.LifoQueue() #takes the last one from the list to queue

numbers = [1,2,3,4,5,6,7]
for x in numbers:
  q.put(x)

print(q.get())