import tkinter as tk
import client.gui as gui 

if __name__ == "__main__":
    root = tk.Tk()
    app = gui.VentanaPrincipal(root)
    app.mainloop()