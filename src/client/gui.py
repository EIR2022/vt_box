import tkinter as tk

class VentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.boton_crear = tk.Button(self, text="Crear", command=self.mostrar_ventana_crear_mv)
        self.boton_crear.pack(fill= tk.X)
        self.boton_arrancar = tk.Button(self, text="Arrancar", command=self.mostrar_ventana_arrancar_mv)
        self.boton_arrancar.pack(fill= tk.X)
        self.boton_listar = tk.Button(self, text="Listar", command=self.mostrar_ventana_listar_mv)
        self.boton_listar.pack(fill= tk.X)
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.mostrar_ventana_eliminar_mv)
        self.boton_eliminar.pack(fill= tk.X)

    def mostrar_ventana_crear_mv(self):
        self.master.withdraw() # oculta la ventana principal
        ventana_crear_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        app_secundaria = VentanaCrearMV(ventana_crear_mv) # crea una nueva instancia del frame de la ventana secundaria
        ventana_crear_mv.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_crear_mv(ventana_crear_mv)) # maneja el cierre de la ventana secundaria
        ventana_crear_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        ventana_crear_mv.wait_window(ventana_crear_mv) # espera hasta que se cierre la ventana secundaria

    def cerrar_ventana_crear_mv(self, ventana_crear_mv):
        ventana_crear_mv.grab_release() # libera el control de la ventana secundaria
        ventana_crear_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

    def mostrar_ventana_arrancar_mv(self):
        self.master.withdraw() # oculta la ventana principal
        ventana_arrancar_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        app_secundaria = VentanaArrancar(ventana_arrancar_mv) # crea una nueva instancia del frame de la ventana secundaria
        ventana_arrancar_mv.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_crear_mv(ventana_arrancar_mv)) # maneja el cierre de la ventana secundaria
        ventana_arrancar_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        ventana_arrancar_mv.wait_window(ventana_arrancar_mv) # espera hasta que se cierre la ventana secundaria

    def cerrar_ventana_arrancar_mv(self, ventana_arrancar_mv):
        ventana_arrancar_mv.grab_release() # libera el control de la ventana secundaria
        ventana_arrancar_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

    def mostrar_ventana_listar_mv(self):
        self.master.withdraw() # oculta la ventana principal
        ventana_listar_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        app_secundaria = VentanaListar(ventana_listar_mv) # crea una nueva instancia del frame de la ventana secundaria
        ventana_listar_mv.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_listar_mv(ventana_listar_mv)) # maneja el cierre de la ventana secundaria
        ventana_listar_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        ventana_listar_mv.wait_window(ventana_listar_mv) # espera hasta que se cierre la ventana secundaria

    def cerrar_ventana_listar_mv(self, ventana_listar_mv):
        ventana_listar_mv.grab_release() # libera el control de la ventana secundaria
        ventana_listar_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

    def mostrar_ventana_eliminar_mv(self):
        self.master.withdraw() # oculta la ventana principal
        ventana_eliminar_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        app_secundaria = VentanaEliminar(ventana_eliminar_mv) # crea una nueva instancia del frame de la ventana secundaria
        ventana_eliminar_mv.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_ventana_eliminar_mv(ventana_eliminar_mv)) # maneja el cierre de la ventana secundaria
        ventana_eliminar_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        ventana_eliminar_mv.wait_window(ventana_eliminar_mv) # espera hasta que se cierre la ventana secundaria

    def cerrar_ventana_eliminar_mv(self, ventana_arrancar_mv):
        ventana_arrancar_mv.grab_release() # libera el control de la ventana secundaria
        ventana_arrancar_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

class VentanaCrearMV(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = tk.Label(self, text="Crear")
        self.etiqueta.pack()

class VentanaArrancar(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = tk.Label(self, text="Arrancar")
        self.etiqueta.pack()

class VentanaListar(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = tk.Label(self, text="Listar")
        self.etiqueta.pack()

class VentanaEliminar(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = tk.Label(self, text="Eliminar")
        self.etiqueta.pack()

