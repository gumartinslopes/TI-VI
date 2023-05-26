import customtkinter as ctk
from ...utils import image_handle

class MultipleImageResult(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path_list, nearest_paths_list, dist_list):
        self.parent = parent
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)

        self.img_path_list = img_path_list,
        self.nearest_paths_list = nearest_paths_list,
        self.dist_list = dist_list
    
    def savePDF(self):
        paths_for_pdf = []
        for i, original_path in enumerate(self.main_image_path):
            # somente 9 imagens
            self.dist_path_per_img[i][1] = self.dist_path_per_img[i][1][1:-1]
            paths_for_pdf.append(
                [original_path] + self.dist_path_per_img[i][1])

        for path_list in paths_for_pdf:
            print(path_list)
            print('')
        image_handle.savePDF(paths_for_pdf)