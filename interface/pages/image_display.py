import customtkinter as ctk
from .utils import image_handle

class ImageDisplay(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path):
        ctk.CTkFrame.__init__(self,parent)
        self.main_image_path = img_path
        self.setup_grid()
        self.setup_sidebar()
        
        self.img_label_title = ctk.CTkLabel(self,fg_color="#1C1B1B", text='Imagem Original', font=ctk.CTkFont(family='roboto', weight='bold', size=15))
        self.img_label_title.grid(row = 0, column = 0)

        # inicialização do label de imagem
        self.img_label = ctk.CTkLabel(self, text='')
        self.img_label.grid(row = 1, column = 0, padx = 20)
        self.configure_main_img(self.main_image_path)

        self.btn_load = ctk.CTkButton(self, text='Nova Imagem', command=self.update_main_img)
        self.btn_load.grid(row = 2, column = 0, pady = 10)

        self.btn_save = ctk.CTkButton(self, text='Salvar Resultados')
        self.btn_save.grid(row = 3, column = 0, pady = 10)

    def setup_grid(self):
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    #Criação da sidebar e todos os seus frames
    def setup_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
    
    def configure_main_img(self, file_path):
        self.img_label.configure(image = image_handle.open_ctk_img(file_path, (400,500)))

    def update_main_img(self):
        self.configure_main_img(image_handle.select_file())