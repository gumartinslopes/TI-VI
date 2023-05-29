import customtkinter as ctk
from ...utils import file_handle

class MultipleImageResult(ctk.CTkFrame):
    def __init__(self,  parent, controller, img_path_list, result_dict):
        self.parent = parent
        self.controller = controller
        ctk.CTkFrame.__init__(self, parent)

        self.img_path_list = img_path_list
        self.result_dict = result_dict
        self.setup_grid()
        self.tabview = ctk.CTkTabview(self)
        self.setup_optionmenu()
        self.setup_result_frame()

    
    def setup_grid(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
  
    def setup_optionmenu(self):
        value_list = [f"image {i + 1}" for i in range(len(self.img_path_list))]
        optionmenu = ctk.CTkOptionMenu(self, values=value_list,
                                                command=self.optionmenu_callback)
        optionmenu.set("image 1")
        optionmenu.grid(column = 1, row = 0, pady = 10)

    def setup_result_frame(self):
        self.result_frame = ctk.CTkFrame(self, bg_color="#232b33")
        self.result_frame.grid(column = 1, row = 1, sticky = 'nsew')

    def optionmenu_callback(self,choice):
        print("optionmenu dropdown clicked:", choice)
        
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
        file_handle.savePDF(paths_for_pdf)