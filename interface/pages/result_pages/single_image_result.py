import customtkinter as ctk
import pandas as pd

from ...utils import image_handle
from ..widgets.result_tabview import ResultTabview
from PIL import Image
import os
from io import BytesIO
import requests
import os
from PIL import Image


class SingleImageResult(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path, nearest_paths, dists):
        self.parent = parent
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)

        self.main_image_path = img_path
        self.nearest_paths = nearest_paths
        self.dists = dists

        self.setup_grid()
        self.setup_sidebar()
        self.configure_main_img(self.main_image_path)
        self.setup_tabview()
        self.setup_btns()
    
    def setup_grid(self):
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=0)
    

    def configure_main_img(self, file_path):
        self.img_label.configure(
            image=image_handle.open_ctk_img(file_path, (400, 500)))

    # Criação da sidebar e todos os seus frames
    def setup_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.img_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text='',
        )
        # Título da imagem Original
        self.img_label_title = ctk.CTkLabel(
            self.sidebar_frame,  
            text='Imagem Original', 
            font=ctk.CTkFont(
                family='roboto', 
                weight='bold',
                size=20
            )
        )
        dark_mode_path = f'{os.getcwd()}/interface/assets/darkmode.png'
        white_mode_path = f'{os.getcwd()}/interface/assets/lightmode.png'
        appearance_mode_img = ctk.CTkImage(light_image=Image.open(white_mode_path), dark_image=Image.open(dark_mode_path))
        appearance = 'Modo Escuro' if ctk.get_appearance_mode() == 'Dark'else 'Modo Claro'
        self.appearance_mode_btn = ctk.CTkButton(
            self.sidebar_frame,
            image=appearance_mode_img,
            text=appearance,
            fg_color = 'transparent',
            command=self.change_appearance_mode,
        )
        
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.img_label_title.grid(row=0, column=0, padx = 10, pady = 20)
        self.img_label.grid(row=1, column=0, padx=20, pady = 5)
        self.appearance_mode_btn.grid(row = 2, column = 0,sticky ='w', pady = 10, padx = 10)

    def setup_tabview(self):
        self.tabview = ResultTabview(self, self.dists, self.nearest_paths)
        self.tabview.grid(row=0, column=1, columnspan = 2,padx=20, pady=20, sticky='nsew')
    
    def change_appearance_mode(self):
        if ctk.get_appearance_mode() == 'Dark':
            ctk.set_appearance_mode("Light")
            self.appearance_mode_btn.configure(text = 'Modo Claro', text_color = '#333333')
        else:
            ctk.set_appearance_mode("Dark")
            self.appearance_mode_btn.configure(text = 'Modo Escuro', text_color = '#DCE4EE')

    def setup_btns(self):
        self.btn_load = ctk.CTkButton(
            self, 
            text='Nova Imagem', 
            command=self.controller.new_results_page
        )
        self.btn_save = ctk.CTkButton(self, text='Salvar Resultados')
        self.btn_load.grid(row=2, column=1, pady=10)
        self.btn_save.grid(row=3, column=1, pady=10)
        
    def savePDF(self):
        paths_for_pdf = []
        for i, original_path in enumerate(self.main_image_path):
            # somente 9 imagens
            self.dist_path_per_img[i][1] = self.dist_path_per_img[i][1][1:-1]
            paths_for_pdf.append(
                [original_path] + self.dist_path_per_img[i][1])

        for path_list in paths_for_pdf:
            print(path_list)
            print('')
        image_handle.savePDF(paths_for_pdf)