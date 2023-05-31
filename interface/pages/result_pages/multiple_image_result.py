import customtkinter as ctk
from tkinter import filedialog as fd
from ...utils import file_handle, constants
from ..widgets.result_tabview import ResultTabview
import os
from PIL import Image

class MultipleImageResult(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path_list, result_list, dist_list):
        self.parent = parent
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)

        self.img_path_list = img_path_list
        self.result_list = result_list
        self.dist_list = dist_list
        self.download_nearest_imgs()
        self.setup_grid()
        # Título da imagem Original
        self.setup_main_img()
        self.setup_sidebar()
        self.setup_tabview()
    
    def setup_grid(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2), weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
    
    def setup_main_img(self):
        self.img_label_title = ctk.CTkLabel(
            self,  
            text='Imagem Original', 
            font=ctk.CTkFont(
                family='roboto', 
                weight='bold',
                size=20,
            )
        )
        self.img_label = ctk.CTkLabel(
            self, 
            image=file_handle.open_ctk_img(self.img_path_list[0], constants.MULTIPLE_RESULT_MAIN_IMG_DIMS),
            text='',
        )
        self.img_label_title.grid(row=0, column=1, padx = 10, pady = 10)
        self.img_label.grid(row=1, column=1, padx=10)
    
    def configure_main_img(self, file_path):
        self.img_label.configure(
            image=file_handle.open_ctk_img(file_path, constants.MULTIPLE_RESULT_MAIN_IMG_DIMS))
    
    def download_nearest_imgs(self):
        self.nearest_imgs = []
        for path_list in self.result_list:
            img_list = []
            for path in path_list:
                pil_img = file_handle.get_image(path)
                img_list.append(pil_img)
            self.nearest_imgs.append(img_list)
    
    # Criação da sidebar e todos os seus frames
    def setup_sidebar(self):
        option_menu_values = [f'imagem {i + 1}' for i in range(len(self.img_path_list))]
        self.sidebar_frame = ctk.CTkFrame(
            self,
            width=200,
            corner_radius=0, 
            fg_color=(constants.SIDEBAR_LIGHT_BG_COLOR,constants.SIDEBAR_DARK_BG_COLOR)
        )
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.option_menu = ctk.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=option_menu_values,
                                                        command=self.change_results)
        self.option_menu.grid(row = 2, column = 0, pady = 20)
        self.setup_sidebar_btns()
    
    def change_results(self, option):
        index = int(option.split(' ')[1]) - 1
        self.configure_main_img(self.img_path_list[index])
        self.tabview.update_info(self.nearest_imgs[index], self.dist_list[index])

    def setup_sidebar_btns(self):
        # Botão de modo de imagem   
        dark_mode_path = f'{os.getcwd()}/interface/assets/darkmode.png'
        white_mode_path = f'{os.getcwd()}/interface/assets/lightmode.png'
        appearance_mode_img = ctk.CTkImage(light_image=Image.open(white_mode_path), 
                                           dark_image=Image.open(dark_mode_path))
        self.appearance_mode_btn = ctk.CTkButton(
            self.sidebar_frame,
            image=appearance_mode_img,
            fg_color = 'transparent',
            command=self.change_appearance_mode,
        )
        self.configure_appearance_btn_txt()    

        self.btn_load = ctk.CTkButton(
            self.sidebar_frame, 
            text='Nova Imagem', 
            command=self.controller.new_results_page
        )
        self.btn_save = ctk.CTkButton(self.sidebar_frame, text='Salvar Resultados', 
                                      command=self.save_results)
        self.btn_load.grid(row=0, column=0, pady=20)
        self.btn_save.grid(row=1, column=0, pady=20)
        self.appearance_mode_btn.grid(row = 4, column = 0, pady = 10, padx = 10, sticky = 's')

    def change_appearance_mode(self):
        self.controller.change_appearance_mode()
        self.configure_appearance_btn_txt()

    def configure_appearance_btn_txt(self):
        if ctk.get_appearance_mode() == constants.DARK_MODE:
            appearance_txt = 'Modo Escuro'
            txt_color = constants.BTN_TEXT_DARK_COLOR 
        else: 
            appearance_txt = 'Modo Claro'
            txt_color = constants.BTN_TEXT_LIGHT_COLOR
        self.appearance_mode_btn.configure(text=appearance_txt, text_color=txt_color)

    def setup_tabview(self):
        self.tabview = ResultTabview(self, self.dist_list[0], self.nearest_imgs[0], num_cols=2)
        self.tabview.grid(row=0, column=2, columnspan = 2,rowspan = 2, padx=20, pady=20, sticky='nsew')
        
    def save_results(self):
        save_path = fd.askdirectory()
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for i in range(len(self.img_path_list)):
            result_path = f'{save_path}/result_{i + 1}' 
            file_handle.save_images(images=self.nearest_imgs[i], ask_path=False, save_path=result_path)