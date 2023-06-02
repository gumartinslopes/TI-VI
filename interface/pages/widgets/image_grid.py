import customtkinter as ctk
import math
from ...utils import file_handle

class ImageGrid(ctk.CTkScrollableFrame):
    def __init__(self, master, imgs, num_cols):
        super().__init__(master=master)
        self.imgs = imgs
        self.num_cols = num_cols
        self.quant_elements = len(imgs)
        self.num_rows = math.ceil(self.quant_elements / num_cols)
        self.image_labels = []
   
        self.setup_imgs(self.imgs)
    
    def update_info(self, imgs):
        self.imgs = imgs
        self.setup_imgs(imgs)

    def setup_imgs(self,imgs):
        j = 0
        i = 0
        for img in imgs:
                img = ctk.CTkImage(light_image=img,
                                dark_image=img, size=(200, 200))
                image_label = ctk.CTkLabel(self, image=img, text='')
                image_label.grid(row=i % self.num_rows, column=j % self.num_cols, padx=5, pady=5, sticky='nsew')
                self.image_labels.append(image_label)
                j = j + 1
                if j % self.num_cols == 0:
                    i = (i + 1) 

    def get_imgs(self):
        return self.imgs