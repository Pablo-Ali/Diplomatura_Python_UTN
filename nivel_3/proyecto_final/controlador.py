from tkinter import Tk
from vista import Ventana
import observador
import funciones
import threading
import servidor

class Controlador:
    """
    Clase principal que inicia la aplicación gráfica y gestiona su ciclo de vida.
    """
    def __init__(self):
        """
        Inicializa la interfaz principal de la aplicación.
        """
        self.root = Tk()
        self.panel = Ventana()

    def iniciar(self) -> None:
        """
        Inicia la ventana principal y el bucle de eventos de Tkinter.
        """
        threading.Thread(target=servidor.iniciar_servidor).start() # lanza el servidor
        threading.Thread(target=funciones.conectar_servidor).start() # se conecta al servidor
        self.panel.vista_principal(self.root)
        self.el_observador = observador.ConcreteObserverA(self.panel.crud)
        self.root.mainloop()

if __name__ == "__main__":
    app = Controlador()
    app.iniciar()