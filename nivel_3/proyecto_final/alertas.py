from tkinter.messagebox import askyesno


class MisAlertas():
    """
    Clase que contiene métodos para mostrar cuadros de diálogo de confirmación
    para acciones sensibles como borrar o actualizar registros.
    """
    
    def confirmar_borrar(self, ) -> bool:
        """
        Muestra una alerta de confirmación antes de borrar un registro.

        :return: True si el usuario confirma, False en caso contrario.
        :rtype: bool
        """
        if askyesno("Precaución", "¿Está seguro que desea borrar el registro?"):
            return True
            
        else:
            return False

    def confirmar_actualizar(self, ) -> bool:
        """
        Muestra una alerta de confirmación antes de actualizar el stock.

        :return: True si el usuario confirma, False en caso contrario.
        :rtype: bool
        """
        if askyesno("Precaución", "¿Está seguro que desea cambiar el stock?"):
            return True
            
        else:
            return False