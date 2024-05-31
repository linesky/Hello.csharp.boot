import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os
import sys



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("run")

        # Janela amarela
        self.root.configure(bg='yellow')

        

        # Botões
        self.build_button = tk.Button(self.root, text="run", command=self.build_kernel)
        self.build_button.pack(pady=5)

        

    

    def build_kernel(self):
        
        os.system('pkexec nautilus --browser ./')
        
if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
