import queue

# LIFO

q = queue.LifoQueue() # instancio la clase LifoQueue de la librería queue

for x in range(3):
    q.put(x)

print(list(q.queue))

while not q.empty():
    print(q.get(), end="\t")