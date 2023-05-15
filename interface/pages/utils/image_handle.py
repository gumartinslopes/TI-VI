from tkinter import filedialog as fd
from PIL import Image
import customtkinter as ctk
import requests
from io import BytesIO

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
        print(f"print pegando a img: {(img)}")
        print(f"print pegando a img: {type(img)}\n")
        if size == None:
            img = ctk.CTkImage(light_image = img)
        else:
            img = ctk.CTkImage(light_image = img, size=size)

        print(f"print pos CTkImage : {(img)}")
        print(f"print pos CTkImage : {type(img)}\n")
        return img

def get_image(image_url, size = (200,200)):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img.resize(size)