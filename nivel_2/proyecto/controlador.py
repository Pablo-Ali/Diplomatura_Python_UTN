from tkinter import Tk
from vista import Ventana

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

    def iniciar(self):
        """
        Inicia la ventana principal y el bucle de eventos de Tkinter.
        """
        self.panel.vista_principal(self.root)
        self.root.mainloop()

if __name__ == "__main__":
    app = Controlador()
    app.iniciar()