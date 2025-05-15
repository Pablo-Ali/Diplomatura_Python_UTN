from tkinter.messagebox import askyesno


class MisAlertas():
    def confirmar_borrar(self, ):
        if askyesno("Precaución", "¿Está seguro que desea borrar el registro?"):
            return True
            
        else:
            return False

    def confirmar_actualizar(self, ):
        if askyesno("Precaución", "¿Está seguro que desea cambiar el stock?"):
            return True
            
        else:
            return False