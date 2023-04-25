import customtkinter as ctk
from .utils import image_handle
# Página inicial da aplicação
class InitialPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        ctk.CTkFrame.__init__(self,parent)
        label = ctk.CTkLabel(self, text="Selecione uma Imagem")
        label.pack(pady=10,padx=10)

        button = ctk.CTkButton(self, text="Selecionar",
                            command = self.switch_tabs)

        button.pack()

    # traca de página após selecionar uma imagem
    def switch_tabs(self):
        file_path = image_handle.select_file()
        self.controller.show_loading_page(file_path)


    
