import customtkinter as ctk
from ..pages.initial_page import InitialPage
from ..pages.result_pages.single_image_result import SingleImageResult
from ..pages.result_pages.multiple_image_result import MultipleImageResult
from ..pages.loading_page import LoadingPage
from ..utils import file_handle, constants
import os

class MIRTApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_container()
        #self.processor = Processor()
        #self.show_initial_page()
        self.mock_filepaths = [
            f'{os.getcwd()}/interface/imgs/vestido.jpeg',
            f'{os.getcwd()}/interface/imgs/azul2.jpg'
        ]

        #dist, self.paths = self.processor.get_nearest_urls(self.filepath)[0]
        generic_path = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1HfAGEhO8vAQVI1xi6Kngd0Ol5YaIp-zE_Q&usqp=CAU'
        generic_path_2 = 'https://images.tcdn.com.br/img/img_prod/699026/vestido_longo_ombro_so_turquesa_1365_3_d21eb19d0d56bf7250f84785610250ad.jpg'

        self.mock_results = [
            [
                generic_path, generic_path, generic_path,
                generic_path, generic_path, generic_path,
                generic_path, generic_path, generic_path
            ],
            [
                generic_path_2, generic_path_2, generic_path_2,
                generic_path_2, generic_path_2, generic_path_2,
                generic_path_2, generic_path_2, generic_path_2
            ]
        ]
        self.mock_dists = [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
        ]

        self.show_multiple_results()
        self.center_window()
    
    def setup_window(self):
        self.width = 1200
        self.height = 650
        self.title('TI-6')
        self.geometry(f'{self.width}x{self.height}')

    def show_initial_page(self):
        # inicializacao do frame inicial
        self.initial_page_frame = InitialPage(self.container, self)
        self.initial_page_frame.grid(row=0, column=0, sticky="nsew")
        self.initial_page_frame.tkraise()
    
    def center_window(self):
        # obtem as mediddas da janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calcula a posicao da janela
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y-50))
    
    def setup_container(self):
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=0)
        self.container.grid_rowconfigure(1, weight=1)

        self.container.grid_columnconfigure(0, weight=1)
    
    def show_multiple_results(self):
        self.image_visualizer_frame = MultipleImageResult(
            parent = self.container, 
            controller = self, 
            img_path_list=self.mock_filepaths, 
            result_list=self.mock_results, 
            dist_list=self.mock_dists
        )
                
        self.image_visualizer_frame.grid(row=0, column=0, sticky="nsew", rowspan = 4)
        self.image_visualizer_frame.tkraise()

    def new_results_page(self):
        file_path = file_handle.select_file()
        if file_path != '':
            self.image_visualizer_frame.grid_forget()
            self.show_loading_page(file_path=file_path)

    def change_appearance_mode(self):
        if ctk.get_appearance_mode() == constants.DARK_MODE:
            ctk.set_appearance_mode(constants.LIGHT_MODE)
        else:
            ctk.set_appearance_mode(constants.DARK_MODE)

    def show_loading_page(self, file_path):
        self.loading_page_frame = LoadingPage(self.container, self)
        self.loading_page_frame.grid(row=0, column=0, sticky="nsew")
        self.loading_page_frame.tkraise()
        self.filepath = file_path
        self.after(500, lambda: self.show_results_page())