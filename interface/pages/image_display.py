import customtkinter as ctk
import pandas as pd

from .utils import image_handle
from . widgets.result_tabview import ResultTabview
from PIL import Image
import os
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications import resnet50
from io import BytesIO
import requests


class ImageDisplay(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path, knn, df_test):
        self.parent = parent
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)
        self.main_image_path = img_path
        self.df_teste = df_test
        self.setup_grid()
        self.setup_sidebar()

        self.model = ResNet50(
            weights='imagenet', include_top=False, pooling='avg', input_shape=(224, 224, 3))
        self.knn = knn

        self.img_label_title = ctk.CTkLabel(self.sidebar_frame, fg_color="#1C1B1B", text='Imagem Original', font=ctk.CTkFont(
            family='roboto', weight='bold', size=15))
        self.img_label_title.grid(row=0, column=0)

        # inicialização do label de imagem
        self.img_label = ctk.CTkLabel(self.sidebar_frame, text='')
        self.img_label.grid(row=1, column=0, padx=20)
        self.configure_main_img(self.main_image_path)

        self.btn_load = ctk.CTkButton(
            self, text='Nova Imagem', command=self.controller.new_image_display)
        self.btn_load.grid(row=2, column=1, pady=10)

        self.btn_save = ctk.CTkButton(self, text='Salvar Resultados')
        self.btn_save.grid(row=3, column=1, pady=5)

        dist, paths = self.get_nearest_features()

        # setup da tabview
        self.tabview = ResultTabview(self, dist, paths)
        self.tabview.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

        self.test_path = self.df_teste.sample(1).img_path.values[0]

        # self.theme_img = ctk.CTkImage(Image.open(
        #     os.getcwd() + '/imgs/moon.png'))
        # self.theme_btn = ctk.CTkButton(
        #     self, image=self.theme_img, text='', fg_color="transparent")
        # self.theme_btn.grid(row=3, column=0, sticky="sw", padx=10, pady=10)

    def setup_grid(self):
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    # Criação da sidebar e todos os seus frames
    def setup_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

    # processamento da imagem

    def image_preprocessing(self, return_body=True):
        print(f"img_label: {self.img_label}")
        print(f"img_label type: {type(self.img_label)}\n")
        try:
            img = Image.open(self.main_image_path).convert("RGB")
            image = tf.image.resize(img, [224, 224])
            image = tf.expand_dims(image, axis=0)
            image = resnet50.preprocess_input(image)
            if return_body:
                #             body = img.tolist()
                return image
            else:
                return image
        except Exception as e:
            print(e)
            return None

    # obtem a lista de embeddings das imgs

    def get_features(self):
        res = self.image_preprocessing(return_body=False)
        print(f"res: {res}")
        if res is not None:
            preds = self.model.predict(res, verbose=0)
            print(f"FEATURES: {preds}")
            return preds
        else:
            return list(list())

    def get_nearest_features(self):
        nearest = self.nearest
        dists_neigh = nearest[0]
        show_indexes = nearest[1]

        path_list = []
        for index in show_indexes:
            path_list.append(self.controller.df_treino.iloc[index].img_path)

        for path in path_list:
            list_img_path = path.to_list()

        return dists_neigh, list_img_path

    def getNearer(self):
        features = self.get_features()
        print(f"FEATURES Nearer: {features}")
        found_neighbors = self.knn.kneighbors(features)
        self.nearest = found_neighbors

    def configure_main_img(self, file_path):
        self.img_label.configure(
            image=image_handle.open_ctk_img(file_path, (400, 500)))

        self.getNearer()

    def update_main_img(self):
        self.configure_main_img(image_handle.select_file())
