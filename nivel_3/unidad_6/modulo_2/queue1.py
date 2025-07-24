import queue

# FIFO

q = queue.Queue() # instancio la clase Queue de la librería queue

q.put(5) # pongo un elemento

print(list(q.queue)) # listo los elementos

print(q.empty()) # vemos si está vacía o no

print(q.get()) # obtiene el elemento y lo borra de la lista

print(list(q.queue)) 

print(q.empty()) 

print("------------------------")

for x in range(3):
    q.put(x)

print(list(q.queue))

while not q.empty():
    print(q.get(), end="\t")