import customtkinter as ctk
from gui import Gui
from utils import *  

if __name__ == "__main__":
    contador = Contador()
    ctk.set_appearance_mode("system")
    root = ctk.CTk()
    root.option_add('*tearOff', False)
    root.title("Contador")
    root.geometry("800x500")
    
    gui = Gui(root, contador)
    gui.gui()

    root.mainloop()