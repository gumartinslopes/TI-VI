from .parquets import getparquets
import pickle
from PIL import Image
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications import resnet50
import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

class Processor():
    def __init__(self):
        self.model = ResNet50(
            weights='imagenet', include_top=False, pooling='avg', input_shape=(224, 224, 3))
        self.setKNN()
    
    def get_nearest_features(self, nearest):

        dist_path_per_img = []

        for nearest in nearest:
            dists_neigh = nearest[0]
            show_indexes = nearest[1]

            path_list = []
            for index in show_indexes:
                path_list.append(
                    self.df_treino.iloc[index].img_path)

            for path in path_list:
                list_img_path = path.to_list()

            dist_path_per_img.append([dists_neigh, list_img_path])

        return dist_path_per_img
    
    def image_preprocessing(self, image_path, return_body=True):
        # print(f"img_label: {self.img_label}")
        # print(f"img_label type: {type(self.img_label)}\n")
        try:
            img = Image.open(image_path).convert("RGB")
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

    # obtem a lista de embeddings das imgss
    def get_features(self, path):
        res = self.image_preprocessing(path, return_body=False)
        #print(f"res: {res}")
        if res is not None:
            # PARALELIZAR
            preds = self.model.predict(res, verbose=0)
         #   print(f"FEATURES: {preds}")
            return preds
        else:
            return list(list())
        
    def getNearer(self, paths):
        nearest = []
        for path in paths:
            one_img_features = self.get_features(path)
            #print(f"FEATURES Nearer: {one_img_features}")
            found_neighbors = self.knn.kneighbors(one_img_features)
            nearest.append(found_neighbors)
        return nearest
    
    def setKNN(self):
        dfs = getparquets.getParquets()
        # print(dfs)
        self.dfs = dfs
        self.df_treino = dfs[0]

        # X = np.vstack(self.df_treino["embedding"].values)
        # y = self.df_treino['img_path'].values

        # neigh = KNeighborsClassifier(n_neighbors=10, metric="cosine")
        # neigh.fit(X, y)

        self.knn = pickle.load(open('knnpickle_file', 'rb'))

    def get_nearest_urls(self, paths):
        nearest = self.getNearer(paths)
        nearest_features_list = self.get_nearest_features(nearest)
        return nearest_features_list