import customtkinter as ctk
from . . utils import image_handle
class ResultTabview(ctk.CTkTabview):
    def __init__(self, parent):
        self.parent = parent
        ctk.CTkTabview.__init__(self,parent)

        self.tabname1 = 'Maiores Semelhanças'
        self.tabname2 = 'Informações'

        self.add(self.tabname1)
        self.add(self.tabname2)

        self.setup_image_grid()
        self.tab(self.tabname1).grid_columnconfigure(0,weight=1)
        self.tab(self.tabname1).grid_rowconfigure(0,weight=1)
    

    def setup_image_grid(self):
        self.image_grid = ctk.CTkScrollableFrame(self.tab(self.tabname1))
        self.image_grid.grid(row = 0, column = 0, sticky = 'nsew')

        img1 = image_handle.open_ctk_img('C:/Users/gumar/faculdade/6oPeriodo/TIVI/TI-VI/interface/imgs/azul2.jpg', (200,200))
        self.image1 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image1.grid(row  = 0,column = 0)
        
        self.image2 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image2.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.image1 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image1.grid(row  = 0,column = 0)
        
        self.image2 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image2.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.image3 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image3.grid(row  = 1,column = 0)
        
        self.image4 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image4.grid(row = 1, column = 1, padx = 5, pady = 10)

        self.image5 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image5.grid(row  = 0, column = 2)
        
        self.image6 = ctk.CTkLabel(self.image_grid,image=img1, text='')
        self.image6.grid(row = 1, column = 2, padx = 5, pady = 10)
        