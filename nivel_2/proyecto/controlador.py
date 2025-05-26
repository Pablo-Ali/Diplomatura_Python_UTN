from tkinter import Tk
from vista import Ventana

if __name__ == "__main__":
    root_tk = Tk()
    panel = Ventana()
    panel.vista_principal(root_tk)
    root_tk.mainloop()
