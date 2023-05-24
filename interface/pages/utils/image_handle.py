from tkinter import filedialog as fd
from PIL import Image
import customtkinter as ctk
import requests
from io import BytesIO
from PIL import Image
from fpdf import FPDF
import os


def select_file():
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt'),
    )

    file_path = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    return file_path


def open_ctk_img(file_path, size=None):
    # Cria um objeto de imagem
    img = Image.open(file_path)
    print(f"print pegando a img: {(img)}")
    print(f"print pegando a img: {type(img)}\n")
    if size == None:
        img = ctk.CTkImage(light_image=img)
    else:
        img = ctk.CTkImage(light_image=img, size=size)

    print(f"print pos CTkImage : {(img)}")
    print(f"print pos CTkImage : {type(img)}\n")
    return img


def get_image(image_url, size=(200, 200), resize=True):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    if (resize == False):
        return img

    return img.resize(size)


def savePDF(image_paths):

    # Get the path to the user's Downloads folder
    downloads_path = os.path.expanduser("~") + "/Downloads"

    # Specify the name of the folder you want to create
    folder_name = "Results_CIICAM"

    # Create the full path by joining the downloads path and folder name
    parent_folder_path = os.path.join(downloads_path, folder_name)

    # Create the folder
    if not os.path.exists(parent_folder_path):
        os.makedirs(parent_folder_path)

    print("Folder created at:", parent_folder_path)

    for i, page in enumerate(image_paths):

        # Specify the name of the folder you want to create
        folder_name = "Image_"+str(i+1)

        # Create the full path by joining the parent folder path and folder name
        folder_path = os.path.join(parent_folder_path, folder_name)

        # Create the folder
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for j, list_path in enumerate(page):

            if (j == 0):
                image = Image.open(list_path)
                image_name = 'original_'+str(i+1)+'.jpg'
            else:
                image = get_image(list_path, resize=False)
                image_name = 'similarity'+str(j)+'.jpg'

            image.save(os.path.join(folder_path, image_name))

    print("Images saved in:", parent_folder_path)
