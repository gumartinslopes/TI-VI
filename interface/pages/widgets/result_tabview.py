import customtkinter as ctk
from ..utils import image_handle
import os
from PIL import Image
import requests
from io import BytesIO


class ResultTabview(ctk.CTkTabview):
    def __init__(self, parent, dist, paths):
        self.parent = parent
        ctk.CTkTabview.__init__(self, parent)

        self.dist = dist
        self.paths = paths

        self.tabname1 = 'Maiores Semelhanças'
        self.tabname2 = 'Informações'

        self.add(self.tabname1)
        self.add(self.tabname2)

        self.tab(self.tabname1).grid_columnconfigure(0, weight=1)
        self.tab(self.tabname1).grid_rowconfigure(0, weight=1)
        self.tab(self.tabname2).grid_columnconfigure(0, weight=1)
        self.tab(self.tabname2).grid_rowconfigure(0, weight=1)

        self.setup_image_grid()
        self.setup_infotab()

    def setup_image_grid(self):
        self.image_grid = ctk.CTkScrollableFrame(self.tab(self.tabname1))
        self.image_grid.grid(row=0, column=0, sticky='nsew')

        self.image_labels = []
        j = 0
        i = 0
        num_cols = 3
        for path in self.paths[1:]:
            pil_img = image_handle.get_image(path)
            img = ctk.CTkImage(light_image=pil_img,
                               dark_image=pil_img, size=(200, 200))
            image_label = ctk.CTkLabel(self.image_grid, image=img, text='')
            image_label.grid(row=i, column=j % num_cols, padx=20, pady=10)
            self.image_labels.append(image_label)
            print(i, j % num_cols)
            j = j + 1
            if j % num_cols == 0:
                i = (i+1) % num_cols

    def setup_infotab(self):
        self.info_grid = ctk.CTkFrame(self.tab(self.tabname2))
        self.info_grid.grid(row=0, column=0, sticky='nsew')

        self.info1 = ctk.CTkLabel(
            self.info_grid, text='Info 1: Result', font=('roboto bold', 20))
        self.info1.grid(row=1, column=0, padx=20, pady=10)

        self.info2 = ctk.CTkLabel(
            self.info_grid, text='Info 2: Result', font=('roboto bold', 20))
        self.info2.grid(row=2, column=0, padx=20, pady=10)

        self.info3 = ctk.CTkLabel(
            self.info_grid, text='Info 3: Result', font=('roboto bold', 20))
        self.info3.grid(row=3, column=0, padx=20, pady=10)

        self.info4 = ctk.CTkLabel(
            self.info_grid, text='Info 4: Result', font=('roboto bold', 20))
        self.info4.grid(row=4, column=0, padx=20, pady=10)
