import customtkinter as ctk
from ...utils import file_handle
from .image_grid import ImageGrid
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
        self.image_grid = ImageGrid(master = self.tab(self.tabname1), paths = self.paths, num_cols=3)
        self.image_grid.grid(row=0, column=0, sticky='nsew')

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
    
    def get_imgs(self):
        return self.image_grid.get_imgs()