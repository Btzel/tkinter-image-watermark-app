from tkinter import Tk
from interface_navbar import NavigationBar
from interface_notebook import FrameNotebook
class Interface:
    def __init__(self,resolution):
        #Main root
        self.root = Tk()
        self.root.title("Image Watermarking Desktop App")

        self.root.resizable(False,False)
        self.root.geometry(f"{resolution[0]}x{resolution[1]}"
                           f"+{(self.root.winfo_screenwidth()//2)-(resolution[0]//2)}"
                           f"+{(self.root.winfo_screenheight()//2)-(resolution[1]//2)-60}")

        #Navigation Bar
        self.navigation_bar = NavigationBar(self.root)
        self.root.config(menu=self.navigation_bar)

        self.root.mainloop()





