import threading
import time

def en_espera(arg, tiempo):
    print("Este argumento se pasa en el hilo: {}, {} segundos después \n".format(arg, tiempo))
    time.sleep(tiempo)
    print("El hilo: {} finaliza su ejecución \n".format(arg))

t = threading.Thread(target=en_espera, name="thread", args=("trhead", 7)) # instanciamos la clase Thread
t.start()
print("hola") # esto se muestra antes de que finalice el hilo
t.join() # esto me permite esperar a que termine el hilo antes de seguir con el código
print("chau") # esto se muestra cuando finaliza el hilo