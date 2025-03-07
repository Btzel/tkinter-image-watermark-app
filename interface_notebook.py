from tkinter import Canvas
from tkinter.ttk import Notebook,Frame,Button,Scrollbar
from tkinter import filedialog
from PIL import Image,ImageTk
import os
from notebook_style import NotebookStyle

class FrameNotebook:
    def __init__(self,root):
        # Root reference
        self.root = root
        # Notebook style
        self.notebook_style = NotebookStyle()
        self.notebook_style.change_style("dark")
        # Frames notebook
        self.notebook = Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')
        # Images tab
        self.image_tab = self.create_new_tab("Images")
        # Main Container
        self.main_container = Frame(self.image_tab)
        self.main_container.pack(side="top", fill="both", expand=True)
        # Canvas
        self.canvas = Canvas(self.main_container, bg="#505050",highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand=True)
        #Scrollbar
        self.y_scrollbar = Scrollbar(self.canvas, orient='vertical', command=self.canvas.yview)
        self.y_scrollbar.pack(side='right', fill='y')
        #Configure Canvas
        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.update_scroll())
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        #Scrollable frame
        self.scrollable_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')

        # Image Buttons
        self.images_current_col = 0
        self.images_current_row = 0
        self.image_list = []
        self.image_buttons = []
        self.button_images = {}
        self.photo_images = {}

        self.image = Image.open("add_image.png")
        self.image = self.image.resize((200, 200), Image.Resampling.LANCZOS)
        self.add_button_image = ImageTk.PhotoImage(self.image)
        self.add_image_button = Button(
            self.image_tab,
            image=self.add_button_image,
            command=lambda: self.get_images(root),
            style="AddImage.TButton"
        )

        self.add_image_button.place(relx=0.5, rely=0.5, anchor="center")
        self.add_image_footer_button = Button(
            self.image_tab,
            command=lambda: self.get_images(root),
            text="Add Images",
            style="FooterAddImage.TButton",

        )

        #image tab
        self.image_tab_count = 0
        self.image_tabs = {}


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 90)), "units")

    def update_scroll(self):
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def create_new_tab(self,name):
        tab = Frame(self.notebook)
        tab.pack_propagate(False)
        self.notebook.add(tab, text=name)
        return tab

    def get_images(self,root):
        initial_dir = os.path.expanduser("~/Desktop")
        path_list = filedialog.askopenfilenames(
            initialdir=initial_dir,
            title='Choose your image files',
            filetypes=[
                ('All Images', '*.jpeg;*.jpg;*.png;*.webp;*.ico'),
                ('JPEG', '*.jpeg;*.jpg'),
                ('PNG', '*.png'),
                ('WEBP', '*.webp'),
                ('ICO', '*.ico'),
            ]
        )
        if not path_list:
            return
        for path in path_list:
            try:
                with Image.open(path) as img:
                        img_copy = img.copy()
                        self.image_list.append(img_copy)
            except Exception as e:
                print(f"Error loading image {path}: {str(e)}")
                continue

        self.add_images(root)

    @staticmethod
    def calc_image_b_resolution(root):
        res = (200,200)
        if root.winfo_width() == 1280:
            res = (300,300)
        elif root.winfo_width() == 800:
            res = (180,180)
        return res

    def resize_image_buttons(self,root):
        res = self.calc_image_b_resolution(root)
        for button in self.button_images:
            image = self.button_images[button]
            button_image = image.resize(res, Image.Resampling.LANCZOS)
            photo_image = ImageTk.PhotoImage(button_image)
            button.configure(image=photo_image)
            button.image = photo_image

    def create_image_tab(self,button_index):
        from image_tab import ImageTab

        self.image_tab_count += 1
        image_number = self.image_tab_count
        self.image_buttons[button_index].state(["disabled"])

        tab=ImageTab(root=self.root,
                 notebook=self,
                 image_number=image_number,
                 button_index=button_index)


    def create_image_button_command(self,index):
        return lambda: self.create_image_tab(button_index=index)

    def add_images(self,root):
        self.add_image_button.place_forget()
        self.add_image_footer_button.pack(side="bottom",fill="x",padx=10,pady=10)
        res = self.calc_image_b_resolution(root)
        for image in self.image_list:
            img = image.resize(res, Image.Resampling.LANCZOS)
            photo_image = ImageTk.PhotoImage(img)

            image_button = Button(
                self.scrollable_frame,
                image=photo_image,
                style="AddImage.TButton",
            )
            image_button.configure(command=self.create_image_button_command(len(self.image_buttons)))
            image_button.grid(
                column=self.images_current_col,
                row=self.images_current_row,
                sticky="nsew",
                padx=2.3,
                pady=2.3
            )
            self.images_current_col += 1
            if self.images_current_col > 3:
                self.images_current_row += 1
                self.images_current_col = 0
            image_button.image = photo_image
            self.image_buttons.append(image_button)
            self.button_images[image_button] = image
        self.image_list.clear()
        self.update_scroll()




