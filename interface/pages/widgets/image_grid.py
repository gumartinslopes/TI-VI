import customtkinter as ctk
from ...utils import file_handle

class ImageGrid(ctk.CTkScrollableFrame):
    def __init__(self, master, paths, num_cols):
        super().__init__(master=master)
        self.paths = paths
        self.num_cols = num_cols
        self.image_labels = []
        self.imgs = []
        j = 0
        i = 0
        for path in self.paths[1:]:
            pil_img = file_handle.get_image(path)
            self.imgs.append(pil_img)
            img = ctk.CTkImage(light_image=pil_img,
                               dark_image=pil_img, size=(200, 200))
            image_label = ctk.CTkLabel(self, image=img, text='')
            image_label.grid(row=i, column=j % num_cols, padx=20, pady=10)
            self.image_labels.append(image_label)
            j = j + 1
            if j % num_cols == 0:
                i = (i + 1) % num_cols

    def get_imgs(self):
        return self.imgs