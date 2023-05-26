import customtkinter
import os
from tkinter import *
import customtkinter as ctk

from .pages.initial_page import InitialPage
from .pages.loading_page import LoadingPage
from .pages.result_pages.single_image_result import SingleImageResult
from .pages.result_pages.multiple_image_result import MultipleImageResult
from .utils import image_handle
from .processor import Processor

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme(
    f'{os.getcwd()}/interface/themes/omni.json')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.processor = Processor()
        self.setup_window()
        self.setup_fullscreen()
        self.setup_container()
        self.center_window()
        self.show_initial_page()

    def setup_window(self):
        self.width = 1200
        self.height = 650
        self.title('TI-6')
        self.geometry(f'{self.width}x{self.height}')

    def setup_container(self):
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def setup_fullscreen(self):
        self.bind('<F11>', self.toggle_fullscreen)
        self.fullscreen = False
        self.attributes('-fullscreen', self.fullscreen)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.attributes('-fullscreen', self.fullscreen)
        self.center_window()

    def center_window(self):
        # obtem as mediddas da janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calcula a posicao da janela
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y-50))

    # mostrando cada página
    def show_initial_page(self):
        # inicializacao do frame inicial
        self.initial_page_frame = InitialPage(self.container, self)
        self.initial_page_frame.grid(row=0, column=0, sticky="nsew")
        self.initial_page_frame.tkraise()

    def load_results(self, file_path):
        self.initial_page_frame.grid_forget()
        self.loading_page_frame = LoadingPage(self.container, self)
        self.loading_page_frame.grid(row=0, column=0, sticky="nsew")
        self.loading_page_frame.tkraise()
        results = self.processor.get_nearest_urls(file_path)
        self.after(1000, lambda: self.show_results_page(file_path, results))

    def show_results_page(self, file_path, results):
        self.loading_page_frame.grid_forget()
        # inicializacao do frame de visualizador de imagem
        if len(file_path) == 1:
            dists, paths = results[0]
            self.results_frame = SingleImageResult(
                parent = self.container, 
                controller = self,
                img_path = file_path[0], 
                nearest_paths = paths,
                dists = dists
            )
            
        else:
            dists, paths = results
            self.results_frame = MultipleImageResult(
                parent = self.container, 
                controller = self,
                img_path_list = file_path, 
                nearest_paths_list = paths,
                dist_list = dists
            )   
            pass
        self.results_frame.grid(row=0, column=0, sticky="nsew")
        self.results_frame.tkraise()
    def new_results_page(self):
        file_path = image_handle.select_file()
        self.results_frame.grid_forget()
        self.load_results(file_path=file_path)
