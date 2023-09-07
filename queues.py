import queue

q = queue.Queue() #takes the first one from the list to queue

# 1,2,3,4,5
# 1
# 2,3,4,5

numbers = [10, 20, 30, 40, 50, 60, 70]
for number in numbers:
  q.put(number)

print(q.get())
print(q.get())