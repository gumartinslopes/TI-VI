import customtkinter as ctk
from ...utils import file_handle
from .image_grid import ImageGrid
import os
from PIL import Image
import requests
from io import BytesIO


class ResultTabview(ctk.CTkTabview):
    def __init__(self, parent, dist, imgs, num_cols = 3):
        self.parent = parent
        self.num_cols = num_cols
        ctk.CTkTabview.__init__(self, parent)

        self.dists = dist
        self.imgs = imgs

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

    def update_info(self, imgs, dists):
        self.dists = dists
        self.image_grid.update_info(imgs)
        self.update_infotab(dists)

    def setup_image_grid(self):
        self.image_grid = ImageGrid(master = self.tab(self.tabname1), imgs = self.imgs, num_cols=self.num_cols)
        self.image_grid.grid(row=0, column=0, sticky='nsew')

    def setup_infotab(self):
        self.info_grid = ctk.CTkFrame(self.tab(self.tabname2))
        self.info_grid.grid(row=0, column=0, sticky='nsew')
        self.infos = []
        
        for i in range(len(self.dists)):
            info = ctk.CTkLabel(self.info_grid, text=f'Distância para a Imagem {i + 1}: {self.dists[i]:.2f}', 
                                                                                font=('roboto bold', 20))
            info.grid(row=i, column=0, padx=10, pady=10)
            self.infos.append(info)
    def update_infotab(self, dists):
        for i in range(len(self.dists)):
            self.infos[i].configure(text=f'Distância para a Imagem {i + 1}: {self.dists[i]:.2f}')

    def get_imgs(self):
        return self.image_grid.get_imgs()