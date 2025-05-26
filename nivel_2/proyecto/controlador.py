from tkinter import Tk
from vista import Ventana

class Controlador:
    def __init__(self):
        self.root = Tk()
        self.panel = Ventana()

    def iniciar(self):
        self.panel.vista_principal(self.root)
        self.root.mainloop()

if __name__ == "__main__":
    app = Controlador()
    app.iniciar()