from interface_notebook import Canvas,ImageTk,Image
from image_panel import ImagePanel
class ImageTab:
    def __init__(self,root,notebook,image_number,button_index):
        self.root = root
        self.notebook = notebook
        self.image_number = image_number
        self.button_index = button_index
        self.original_image = self.notebook.button_images[self.notebook.image_buttons[button_index]]
        self.tab = self.notebook.create_new_tab(name=("Image" + str(image_number)))

        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        canvas_width = int((70 / 100) * window_width)
        canvas_height = int(window_height)
        # canvas
        self.canvas = Canvas(self.tab,
                        bg="#505050",
                        width=canvas_width,
                        height=canvas_height)
        self.canvas.pack(side="left", fill="both", expand=False)
        self.canvas_image,self.image_size = self.update_canvas(canvas_width,canvas_height)

        #panel
        self.panel = ImagePanel(self.tab,image_number,self.image_size)


    @staticmethod
    def scale_image(image, canvas_res):
        image_width, image_height = image.size
        bigger_dimension = max(image_width, image_height)
        minor_dimension = min(image_width, image_height)
        if image_width == bigger_dimension:
            canvas_major_dimension = canvas_res[0]
            canvas_minor_dimension = canvas_res[1]
        elif image_height == bigger_dimension:
            canvas_major_dimension = canvas_res[1]
            canvas_minor_dimension = canvas_res[0]
        else:
            canvas_major_dimension = image_width
            canvas_minor_dimension = image_height
        scale_factor = canvas_major_dimension / bigger_dimension
        new_image_width = int(image_width * scale_factor)
        new_image_height = int(image_height * scale_factor)
        if new_image_width > canvas_res[0] or new_image_height > canvas_res[1]:
            scale_factor = canvas_minor_dimension / minor_dimension
            new_image_width = int(image_width * scale_factor)
            new_image_height = int(image_height * scale_factor)
        image = image.resize((new_image_width, new_image_height), Image.Resampling.LANCZOS)
        return image

    def update_canvas(self,canvas_width,canvas_height):
        self.canvas.configure(width=canvas_width,
                         height=canvas_height)
        self.canvas.delete("all")
        image = self.scale_image(image=self.original_image, canvas_res=(canvas_width, canvas_height))
        self.notebook.photo_images[self.button_index] = ImageTk.PhotoImage(image)
        self.canvas.create_image(canvas_width / 2, canvas_height / 2,
                                 image=self.notebook.photo_images[self.button_index],
                                 anchor="center")
        self.canvas.image = self.notebook.photo_images[self.button_index]
        self.notebook.image_tabs[self] = [self.original_image, self.canvas]
        return image,image.size