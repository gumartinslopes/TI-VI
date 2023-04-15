import customtkinter
import os
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image

from tkinter.messagebox import showinfo
customtkinter.set_appearance_mode('System') 
customtkinter.set_appearance_mode('System') 
customtkinter.set_default_color_theme(f'{os.getcwd()}/themes/flamingo.json')
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.width = 1200
        self.height = 650
        self.title('TI-6')
        self.geometry(f'{self.width}x{self.height}')

        self.bind('<F11>', self.toggle_fullscreen)        
        self.fullscreen = False
        self.attributes('-fullscreen', self.fullscreen)
        self.center_window()

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.configure_sidebar()
        
        self.img_label_title = customtkinter.CTkLabel(self,fg_color="#1C1B1B", text='Imagem Original', font=customtkinter.CTkFont(family='roboto', weight='bold', size=15))
        self.img_label_title.grid(row = 0, column = 0)

        # inicialização do label de imagem
        self.img_label = customtkinter.CTkLabel(self, text='')
        self.img_label.grid(row = 1, column = 0, padx = 20)
        self.open_img('C:/Users/gumar/faculdade/6oPeriodo/TIVI/TI-VI/interface/imgs/bebe.jpeg')

        self.btn_load = customtkinter.CTkButton(self, text='Nova Imagem', command=self.load_img_file)
        self.btn_load.grid(row = 2, column = 0, pady = 10)

        self.btn_save = customtkinter.CTkButton(self, text='Salvar Resultados')
        self.btn_save.grid(row = 3, column = 0, pady = 10)

    #Criação da sidebar e todos os seus frames
    def configure_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.attributes('-fullscreen', self.fullscreen)
        self.center_window()
        
    def center_window(self):
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y-50))
    
 
    def load_img_file(self):
         filetypes = (
             ('All files', '*.*'),
             ('text files', '*.txt'),
         )

         file_path = fd.askopenfilename(
             title='Open a file',
             initialdir='/',
             filetypes=filetypes
         )
         self.open_img(file_path)

    def open_img(self, file_path):
        # Cria um objeto de imagem
        img = Image.open(file_path)
        img = customtkinter.CTkImage(light_image = img, size=(400,500))
        # Cria um widget Label
        self.img_label.configure(image = img)

if __name__ == '__main__':
    app = App()
    app.mainloop()