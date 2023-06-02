import customtkinter as ctk
from ...utils import file_handle, constants
from ..widgets.result_tabview import ResultTabview
from PIL import Image
import os

class SingleImageResult(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path, nearest_paths, dists):
        self.parent = parent
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)

        self.main_image_path = img_path
        self.nearest_paths = nearest_paths
        self.dists = dists
        self.download_nearest_imgs()

        self.setup_grid()
        self.setup_sidebar()
        self.configure_main_img(self.main_image_path)
        self.setup_tabview()
        self.setup_btns()
    
    def download_nearest_imgs(self):
        self.nearest_imgs = []
        for path in self.nearest_paths:
            pil_img = file_handle.get_image(path)
            self.nearest_imgs.append(pil_img)
        
    def setup_grid(self):
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=0)
    
    def configure_main_img(self, file_path):
        self.img_label.configure(
            image=file_handle.open_ctk_img(file_path, (400, 500)))

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
        # Botão de modo de imagem
        dark_mode_path = f'{os.getcwd()}/interface/assets/darkmode.png'
        white_mode_path = f'{os.getcwd()}/interface/assets/lightmode.png'
        appearance_mode_img = ctk.CTkImage(light_image=Image.open(white_mode_path), dark_image=Image.open(dark_mode_path))
    
        self.appearance_mode_btn = ctk.CTkButton(
            self.sidebar_frame,
            image=appearance_mode_img,
            fg_color = 'transparent',
            command=self.change_appearance_mode,
        )

        self.configure_appearance_btn_txt()    
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.img_label_title.grid(row=0, column=0, padx = 10, pady = 20)
        self.img_label.grid(row=1, column=0, padx=20, pady = 5)
        self.appearance_mode_btn.grid(row = 2, column = 0,sticky ='w', pady = 10, padx = 10)
    
    def change_appearance_mode(self):
        self.controller.change_appearance_mode()
        self.configure_appearance_btn_txt()

    def configure_appearance_btn_txt(self):
        if ctk.get_appearance_mode() == constants.DARK_MODE:
            appearance_txt = 'Modo Escuro'
            txt_color = '#DCE4EE' 
        else: 
            appearance_txt = 'Modo Claro'
            txt_color = '#333333'
        self.appearance_mode_btn.configure(text=appearance_txt, text_color=txt_color)

    def setup_tabview(self):
        self.tabview = ResultTabview(self, self.dists, self.nearest_imgs)
        self.tabview.grid(row=0, column=1, columnspan = 2,padx=20, pady=20, sticky='nsew')

    def setup_btns(self):
        self.btn_load = ctk.CTkButton(
            self, 
            text='Nova Imagem', 
            command=self.controller.new_results_page
        )
        self.btn_save = ctk.CTkButton(self, text='Salvar Resultados', command=self.save_results)
        self.btn_load.grid(row=2, column=1, pady=10)
        self.btn_save.grid(row=3, column=1, pady=10)
        
    # def saveResults(self):
    #     paths_for_pdf = []
    #     for i, original_path in enumerate(self.main_image_path):
    #         # somente 9 imagens
    #         paths_for_pdf.append(original_path + self.dists[i])

    #     for path_list in paths_for_pdf:
    #         print(path_list)
    #         print('')
    #     file_handle.saveResults(paths_for_pdf)
    def save_results(self):
        file_handle.save_images(images=self.tabview.get_imgs(), ask_path=True)