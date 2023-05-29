from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
import requests
from io import BytesIO
from PIL import Image
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
    if size == None:
        img = ctk.CTkImage(light_image=img)
    else:
        img = ctk.CTkImage(light_image=img, size=size)
    return img


def get_image(image_url, size=(200, 200), resize=True):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    if (resize == False):
        return img

    return img.resize(size)


def saveResults(image_paths):
    save_path = fd.askdirectory()
    folder_name = "Results_CIICAM"

    # Create the full path by joining the downloads path and folder name
    parent_folder_path = os.path.join(save_path, folder_name)

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


def save_images(images, save_path = '', names = None, ask_path = False):
    save_path = fd.askdirectory() if ask_path else save_path
    if save_path != '':
        names = names if names != None else [i for i in range(len(images))]
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for i in range(len(images)):
            caminho_imagem = os.path.join(save_path, f"{names[i]}.png")
            images[i].save(caminho_imagem)
    else:
         messagebox.showinfo("Alerta", "Nenhum diretório foi selecionado!")