from tkinter import Menu
from interface_notebook import FrameNotebook
from PIL import Image,ImageTk
class NavigationBar(Menu):
    def __init__(self,root):
        super().__init__()
        #Root reference
        self.root = root
        #Frame Notebook
        self.notebook = FrameNotebook(self.root)
        #Options
        self.options_menu = Menu(self,tearoff=0)
        #Options-submenus
        self.resolution_menu = Menu(self,tearoff=0)
        self.theme_menu = Menu(self,tearoff=0)

        #Add to options menu
        self.options_menu.add_cascade(label="Resolution",menu=self.resolution_menu)
        self.options_menu.add_cascade(label="Theme",menu=self.theme_menu)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Exit",command=lambda: self.exit(self.root))

        #Options-resolution

        self.resolution_menu.add_command(
            label="1280x720",
            command=lambda: self.change_resolution(self.root,resolution=(1280,720)))
        self.resolution_menu.add_command(
            label="800x600",
            command=lambda: self.change_resolution(self.root,resolution=(800,600)))
        #Options-theme
        self.theme_menu.add_command(
            label="Light",
            command=lambda: self.change_theme(self.root,color_code="white")
        )
        self.theme_menu.add_command(
            label="Dark",
            command=lambda: self.change_theme(self.root,color_code="black")
        )

        #Add to navigation bar
        self.add_cascade(label="Options",menu=self.options_menu)


    def change_resolution(self,root,resolution):
        window_width,window_height = resolution[0],resolution[1]
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        canvas_width = int((70 / 100) * window_width)
        canvas_height = int(window_height)
        for tab,tab_data in self.notebook.image_tabs.items():
            image,canvas = tab_data
            canvas.configure(width=canvas_width,
                             height=canvas_height)
            canvas.delete("all")

            image = self.notebook.scale_image(image=image,canvas_res=(canvas_width,canvas_height))
            photo_image = ImageTk.PhotoImage(image)
            canvas.create_image(canvas_width / 2, canvas_height / 2,
                                image=photo_image,
                                anchor="center")
            canvas.image = photo_image
            self.notebook.image_tabs[tab] = [image,canvas]

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2) - 60
        root.geometry(f"{window_width}x{window_height}"
                      f"+{x}"
                      f"+{y}")
        root.after(1, self.resize_notebook)

    def resize_notebook(self):
        self.notebook.resize_image_buttons(self.root)

    @staticmethod
    def change_theme(root,color_code):
        root.configure(bg=color_code)

    @staticmethod
    def exit(root):
        root.destroy()

