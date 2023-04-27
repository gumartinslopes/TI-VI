import customtkinter as ctk
from .utils import image_handle
import time

# Página inicial da aplicação
class LoadingPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        
        self.parent = parent
        ctk.CTkFrame.__init__(self,parent)
        label = ctk.CTkLabel(self, text="Processando Imagem...", font=("roboto bold", 20) )
        label.pack(pady=30,padx=30)
        self.progress_bar = ctk.CTkProgressBar(self, mode='indeterminate')
        self.progress_bar.pack(pady = 30, padx = 10)
        self.progress_bar.start()