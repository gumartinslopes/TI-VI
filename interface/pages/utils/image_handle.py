from tkinter import filedialog as fd
from PIL import Image
import customtkinter as ctk

def select_file():
        filetypes = (
            ('All files', '*.*'),
            ('text files', '*.txt'),
        )

        file_path = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        return file_path

def open_ctk_img(file_path, size = None):
        # Cria um objeto de imagem
        img = Image.open(file_path)
        if size == None:
            img = ctk.CTkImage(light_image = img)
        else:
            img = ctk.CTkImage(light_image = img, size=size)
        return img