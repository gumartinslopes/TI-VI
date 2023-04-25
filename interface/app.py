import customtkinter
import os
from tkinter import *
import customtkinter as ctk

from pages.image_display import ImageDisplay
from pages.initial_page import InitialPage
from pages.loading_page import LoadingPage
from pages.utils import image_handle

customtkinter.set_appearance_mode('System') 
customtkinter.set_default_color_theme(f'{os.getcwd()}/themes/flamingo.json')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
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
        self.container.pack(side="top", fill="both", expand = True)
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

    def show_loading_page(self, file_path):
        self.initial_page_frame.grid_forget()
        self.loading_page_frame = LoadingPage(self.container, self)
        self.loading_page_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.loading_page_frame.tkraise()
        self.after(1000 , lambda:self.show_image_display(file_path=file_path))

    def show_image_display(self, file_path):
        self.loading_page_frame.grid_forget()
        #inicializacao do frame de visualizador de imagem
        self.image_visualizer_frame = ImageDisplay(self.container, self, file_path)
        self.image_visualizer_frame.grid(row = 0, column = 0, sticky = "nsew")
        self.image_visualizer_frame.tkraise()
    
    def new_image_display(self):
        file_path = image_handle.select_file()
        self.image_visualizer_frame.grid_forget()
        self.show_loading_page(file_path=file_path)