import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from vt_box.vt_box import VmManager

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("VmManager")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_button = tk.Button(self, text="Crear", command=self.show_window_create_mv)
        self.create_button.pack(fill= tk.X)
        self.start_button = tk.Button(self, text="Arrancar", command=self.show_window_start_mv)
        self.start_button.pack(fill= tk.X)
        self.list_button = tk.Button(self, text="Listar", command=self.show_window_tolist_mv)
        self.list_button.pack(fill= tk.X)
        self.remove_button = tk.Button(self, text="Eliminar", command=self.show_window_remove_mv)
        self.remove_button.pack(fill= tk.X)

    def show_window_create_mv(self):
        self.master.withdraw() # oculta la ventana principal
        create_window_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        segundary_app = CreateVmWindow(create_window_mv) # crea una nueva instancia del frame de la ventana secundaria
        create_window_mv.protocol("WM_DELETE_WINDOW", lambda: self.close_window_create_mv(create_window_mv)) # maneja el cierre de la ventana secundaria
        create_window_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        create_window_mv.wait_window(create_window_mv) # espera hasta que se cierre la ventana secundaria

    def close_window_create_mv(self, create_window_mv):
        create_window_mv.grab_release() # libera el control de la ventana secundaria
        create_window_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

    def show_window_start_mv(self):
        self.master.withdraw() # oculta la ventana principal
        start_window_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        segundary_app = BootWindow(start_window_mv) # crea una nueva instancia del frame de la ventana secundaria
        start_window_mv.protocol("WM_DELETE_WINDOW", lambda: self.close_window_start_mv(start_window_mv)) # maneja el cierre de la ventana secundaria
        start_window_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        start_window_mv.wait_window(start_window_mv) # espera hasta que se cierre la ventana secundaria

    def close_window_start_mv(self, start_window_mv):
        start_window_mv.grab_release() # libera el control de la ventana secundaria
        start_window_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

    def show_window_tolist_mv(self):
        self.master.withdraw() # oculta la ventana principal
        list_window_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        segundary_app = ListWindow(list_window_mv) # crea una nueva instancia del frame de la ventana secundaria
        list_window_mv.protocol("WM_DELETE_WINDOW", lambda: self.close_window_list_mv(list_window_mv)) # maneja el cierre de la ventana secundaria
        list_window_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        list_window_mv.wait_window(list_window_mv) # espera hasta que se cierre la ventana secundaria

    def close_window_list_mv(self, list_window_mv):
        list_window_mv.grab_release() # libera el control de la ventana secundaria
        list_window_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

    def show_window_remove_mv(self):
        self.master.withdraw() # oculta la ventana principal
        remove_window_mv = tk.Toplevel(self.master) # crea una nueva instancia de la ventana secundaria
        segundary_app = RemoveWindow(remove_window_mv) # crea una nueva instancia del frame de la ventana secundaria
        remove_window_mv.protocol("WM_DELETE_WINDOW", lambda: self.close_window_remove_mv(remove_window_mv)) # maneja el cierre de la ventana secundaria
        remove_window_mv.grab_set() # asegura que la ventana secundaria sea la ventana activa
        remove_window_mv.wait_window(remove_window_mv) # espera hasta que se cierre la ventana secundaria

    def close_window_remove_mv(self, start_window_mv):
        start_window_mv.grab_release() # libera el control de la ventana secundaria
        start_window_mv.destroy() # destruye la ventana secundaria
        self.master.deiconify() # restaura la ventana principal

class CreateVmWindow(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Crear Maquina virtual")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        name_label = tk.Label(self, text="Nombre:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        memory_label = tk.Label(self, text="Memoria (MB):")
        memory_label.grid(row=1, column=0, padx=5, pady=5)
        self.memory_entry = tk.Entry(self)
        self.memory_entry.grid(row=1, column=1, padx=5, pady=5)
        
        vcpu_label = tk.Label(self, text="VCPU:")
        vcpu_label.grid(row=2, column=0, padx=5, pady=5)
        self.vcpu_entry = tk.Entry(self)
        self.vcpu_entry.grid(row=2, column=1, padx=5, pady=5)
        
        image_label = tk.Label(self, text="Ruta de la imagen de disco:")
        image_label.grid(row=3, column=0, padx=5, pady=5)
        self.image_entry = tk.Entry(self)
        self.image_entry.grid(row=3, column=1, padx=5, pady=5)
        self.image_entry.insert(0, "/path/to/image.qcow2")
        
        create_button = ttk.Button(self, text="Crear", command=self.create_vm)
        create_button.grid(row=4, column=1, padx=5, pady=5)

    def create_vm(self):       # Obtener los valores ingresados por el usuario
        name = self.name_entry.get()
        memory = self.memory_entry.get()
        vcpu = self.vcpu_entry.get()
        image_path = self.image_entry.get()
        try: 
            vm = VmManager()
            vm.create_vm(name,memory,vcpu,image_path)
            messagebox.showinfo("Éxito", "La máquina virtual se creó correctamente.")
        except: 
            messagebox.showerror("Error", "No se pudo crear la maquina virtual correctamente.")

class BootWindow(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Arrancar Maquina Virtual")
        self.vm = VmManager()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.vm_listbox = tk.Listbox(self.master, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.vm_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vm_listbox.pack(fill=tk.BOTH, expand=True)
        self.refresh_listbox() 
        self.vm_listbox.bind("<Double-Button-1>", self.connect_vm)

    def refresh_listbox(self):
        self.vm_listbox.delete(0, tk.END)
        vms = self.vm.get_vms_active()
        for vm in vms:
            self.vm_listbox.insert(tk.END, vm['name'])
    
    def connect_vm(self, event):
        selected_vm = self.vm_listbox.get(self.vm_listbox.curselection())
        self.vm.connect_to_vm(selected_vm)

class RemoveWindow(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Eliminar Maquina Virtual")
        self.pack()
        self.vm = VmManager()
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.master)
        self.listbox.pack(side="top", fill="both", expand=True)
        
        self.refresh_button = ttk.Button(self.master, text="Refresh", command=self.refresh_listbox)
        self.refresh_button.pack(side="top")

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop_selected_vm)
        self.stop_button.pack(side="bottom")

        self.refresh_listbox()
    
    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        vms = self.vm.get_vms_active()
        for vm in vms:
            self.listbox.insert(tk.END, vm['name'])

    def stop_selected_vm(self):
        try: 
            selection = self.listbox.curselection()
            if len(selection) > 0:
                domain_name = self.listbox.get(selection[0])
                self.vm.stop_vm(domain_name)
                messagebox.showinfo("Éxito", "La máquina virtual se detuvo correctamente")
            else:
                messagebox.showwarning("Advertencia", "Debes seleccionar una maquina virtual")
        except: 
            messagebox.showerror("Error", "No se pudo apagar la maquina virtual correctamente.")

class ListWindow(tk.Frame): 
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Listar Maquina Virtual")
        self.pack()
        self.vm = VmManager()
        self.create_widgets()

    def create_widgets(self):
        scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.vm_listbox = tk.Listbox(self.master, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.vm_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vm_listbox.pack(fill=tk.BOTH, expand=True)
        self.refresh_listbox() 
        self.vm_listbox.bind("<Double-Button-1>", self.show_vm_details)

    def refresh_listbox(self):
        self.vm_listbox.delete(0, tk.END)
        vms = self.vm.get_vms_active()
        for vm in vms:
            self.vm_listbox.insert(tk.END, vm['name'])

    def show_vm_details(self, event):
        selected_vm = self.vm_listbox.get(self.vm_listbox.curselection())
        VMInfoWindow(self.master, selected_vm)

class VMInfoWindow:
    def __init__(self, master, vm_name):
        self.master = tk.Toplevel(master)
        self.vm = VmManager()
        self.vm_name = vm_name
        self.master.title("Detalles de Máquina Virtual: " + self.vm_name)
        self.master.geometry("400x230")
        vm_info_label = ttk.Label(self.master, text=self.get_vm_info())
        vm_info_label.pack(pady=5, padx=10)
        close_button = ttk.Button(self.master, text="Cerrar", command=self.master.destroy)
        close_button.pack(pady=5)

    def get_vm_info(self):
        vm_info = self.vm.get_vm_info(self.vm_name) 
        vm_info_str = "Nombre: {}\n".format(vm_info['name'])
        vm_info_str += "\nEstado: {}\n".format(vm_info['state'])
        vm_info_str += "\nMax_men: {}\n".format(vm_info['max_mem'])
        vm_info_str += "\nNum_VCPUS: {}\n".format(vm_info['num_vcpus'])
        vm_info_str += "\nUUID: {}\n".format(vm_info['uuid'])
        return vm_info_str