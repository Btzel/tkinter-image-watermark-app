from tkinter.ttk import Frame,Label,Style,Entry,Button,Combobox,Scale
from tkinter import Canvas,StringVar,colorchooser,font

class ImagePanel:
    def __init__(self,tab,image_number,canvas_size,image_size,canvas_modifier):
        #parent tab
        self.tab = tab
        self.color = "#FFFFFF"
        self.unique_style_name = "_" + str(image_number)
        self.image_size = image_size
        self.canvas_size = canvas_size
        self.canvas_modifier = canvas_modifier
        self.current_text = ""
        #panel style
        self.style = Style()
        self.panel_style()
        #canvas
        self.canvas = Canvas(self.tab,highlightthickness=0)
        self.canvas.pack(side="right", fill="both", expand=True,padx=(5,0))

        #main frame
        self.main_frame = Frame(self.canvas,style="Main.TFrame")
        ####### on_canvas_resize
        self.canvas_window = self.canvas.create_window(2, 2, window=self.main_frame, anchor="nw")
        self.main_frame.pack_propagate(False)
        self.canvas.bind('<Configure>', self.on_canvas_resize)
        #features frame
        self.features_frame = Frame(self.main_frame,style="Features.TFrame")
        self.features_frame.pack(side="top",fill="x",expand=False)
        self.features_frame.grid_columnconfigure(0, weight=1)
        self.features_text = Label(self.features_frame,
                                   text="Features",
                                   font=("Verdana", 15, "bold"),
                                   style= "Features.TLabel")
        self.features_text.grid(column=0, row=0,pady=10)
        # text frame
        self.text_frame = Frame(self.main_frame, style="Text.TFrame")
        self.text_frame.pack(side="top", fill="x", expand=False, pady=(15, 5),padx=(10,10))
        self.text_frame.grid_columnconfigure(index=1, weight=1)
        self.text_text = Label(self.text_frame,
                               text="Text",
                               font=("Verdana", 10,"bold"),
                               style="Text.TLabel")
        self.text_text.grid(column=0, row=0,sticky="w",padx=(10,10),pady=(10,10))
        self.text_input = StringVar()
        self.text_input.trace_add("write", self.on_text_change)
        self.text_entry = Entry(self.text_frame,
                                textvariable=self.text_input,
                                justify="left")
        self.text_entry.focus()
        self.text_entry.grid(column=1, row=0,sticky="we",padx=(10,10))
        # color frame
        self.color_frame = Frame(self.main_frame,style="Color.TFrame")
        self.color_frame.pack(side="top",fill="x",expand=False,pady=(5,5),padx=(10,10))
        self.color_frame.grid_columnconfigure(index=1,weight=1)
        self.color_frame.grid_columnconfigure(index=2,weight=2)
        self.color_text = Label(self.color_frame,
                                text="Color",
                                font=("Verdana",10,"bold"),
                                style="Color.TLabel")
        self.color_text.grid(column=0,row=0,sticky="w",padx=(10,10),pady=(10,10))

        self.color_preview = Label(self.color_frame,
                                   text="",
                                   style=f"ColorPrev{self.unique_style_name}.TLabel",
                                   font=("",15),
                                   width=2)
        self.color_preview.grid(column=1,row=0,sticky="we",padx=(5,5))
        self.color_button = Button(self.color_frame,
                                   text="Pick Color",
                                   style="Color.TButton",
                                   command=self.choose_color)
        self.color_button.grid(column=2,row=0,sticky="we",padx=(10,10))
        #font frame
        self.font_frame = Frame(self.main_frame,style="Font.TFrame")
        self.font_frame.pack(side="top",fill="x",expand=False,pady=(5,5),padx=(10,10))
        self.font_frame.grid_columnconfigure(index=1,weight=1)
        self.font_text = Label(self.font_frame,
                               text="Font",
                               font=("Verdana",10,"bold"),
                               style="Font.TLabel")
        self.font_text.grid(column=0,row=0,sticky="w",padx=(10,10),pady=(10,10))
        self.fonts = sorted(list(font.families()))
        self.font_combobox = Combobox(self.font_frame,
                                      values=self.fonts,
                                      state="readonly",
                                      style="Font.TCombobox")
        self.font_combobox.set(self.fonts[0])
        self.selected_font = self.fonts[0]
        self.text_entry.configure(font=(self.selected_font,11))
        self.font_combobox.bind('<<ComboboxSelected>>',self.on_font_change)
        self.font_combobox.grid(column=1,row=0,sticky="we",padx=10)
        #font size
        self.font_size_frame = Frame(self.main_frame,style="FontSize.TFrame")
        self.font_size_frame.pack(side="top",fill="x",expand=False,pady=(5,5),padx=(10,10))
        self.font_size_frame.grid_columnconfigure(index=1,weight=1)
        self.font_size_text = Label(self.font_size_frame,
                                    text="Size",
                                    font=("Verdana",10,"bold"),
                                    style="FontSize.TLabel")
        self.font_size_text.grid(column=0,row=0,sticky="w",padx=10,pady=10)
        self.font_size_value = 11
        self.font_size_slider = Scale(self.font_size_frame,
                                      from_=6,
                                      to=100,
                                      orient="horizontal",
                                      length=200,
                                      value=self.font_size_value, )
        self.font_size_slider.bind('<B1-Motion>', self.on_font_size_slider_move)
        self.font_size_slider.grid(column=1, row=0, sticky="we", padx=10, pady=10)
        self.font_size_value_text = Label(self.font_size_frame,
                                         text=f"{self.font_size_value:3d}",
                                         font=("Verdana",10,"bold"),
                                         style="FontSize.TLabel")
        self.font_size_value_text.grid(column=2,row=0,sticky="we",padx=(5,10),pady=10)
        #Pivot Point Offset X
        self.offset_x_frame = Frame(self.main_frame,style="OffsetX.TFrame")
        self.offset_x_frame.pack(side="top",fill="x",expand=False,pady=5,padx=10)
        self.offset_x_frame.grid_columnconfigure(index=1,weight=1)
        self.offset_x_text = Label(self.offset_x_frame,
                                   text="Offset X",
                                   font=("Verdana",10,"bold"),
                                   style="OffsetX.TLabel")
        self.offset_x_text.grid(column=0,row=0,sticky="w",padx=10,pady=10)
        self.offset_x_value = self.canvas_size[0]/2

        self.offset_x_slider = Scale(self.offset_x_frame,
                                     from_=self.offset_x_value - self.image_size[0]/2,
                                     to=self.offset_x_value + self.image_size[0]/2,
                                     orient="horizontal",
                                     length=200,
                                     value=self.offset_x_value)
        self.offset_x_slider.bind('<B1-Motion>',self.on_offset_x_slider_move)
        self.offset_x_slider.grid(column=1,row=0,sticky="we",padx=10,pady=10)
        #Pivot Point Offset Y
        self.offset_y_frame = Frame(self.main_frame, style="OffsetY.TFrame")
        self.offset_y_frame.pack(side="top", fill="x", expand=False, pady=5, padx=10)
        self.offset_y_frame.grid_columnconfigure(index=1, weight=1)
        self.offset_y_text = Label(self.offset_y_frame,
                                   text="Offset Y",
                                   font=("Verdana", 10, "bold"),
                                   style="OffsetY.TLabel")
        self.offset_y_text.grid(column=0, row=0, sticky="w", padx=10, pady=10)
        self.offset_y_value = self.canvas_size[1]/2
        self.offset_y_slider = Scale(self.offset_y_frame,
                                     from_=self.offset_y_value - self.image_size[1]/2,
                                     to=self.offset_y_value + self.image_size[1]/2,
                                     orient="horizontal",
                                     length=200,
                                     value=self.offset_y_value)
        self.offset_y_slider.bind('<B1-Motion>', self.on_offset_y_slider_move)
        self.offset_y_slider.grid(column=1, row=0, sticky="we", padx=10, pady=10)
        #Rotation
        self.rotation_frame = Frame(self.main_frame,style="Rotation.TFrame")
        self.rotation_frame.pack(side="top",fill="x",expand=False,pady=5,padx=10)
        self.rotation_frame.grid_columnconfigure(index = 1,weight=1)
        self.rotation_text = Label(self.rotation_frame,
                                   text="Rotation",
                                   font=("Verdana",10,"bold"),
                                   style="Rotation.TLabel")
        self.rotation_text.grid(column=0,row=0,sticky="w",padx=10,pady=10)
        self.rotation_value = 360
        self.rotation_slider = Scale(self.rotation_frame,
                                     from_=360,
                                     to=0,
                                     orient="horizontal",
                                     length=200,
                                     value=self.rotation_value)
        self.rotation_slider.bind('<B1-Motion>',self.on_rotation_slider_move)
        self.rotation_slider.grid(column=1,row=0,sticky="we",padx=10,pady=10)
        #Tile, spacing, back button and forward button will be developed after canvas parts are done
        #Tile

        #Spacing

        #Back Button

        #Forward Button

        #Save Button
        self.save_frame = Frame(self.main_frame,style="Save.TFrame")
        self.save_frame.pack(side="top",fill="x",expand=False,pady=5,padx=10)
        self.save_frame.grid_columnconfigure(index=0, weight=1)
        self.save_button = Button(self.save_frame,
                                  text="Save Image",
                                  style="Save.TButton",
                                  command=self.save_image)
        self.save_button.grid(column=0,row=0,sticky="we",pady=10)

        self.params = [self.offset_x_value,
                       self.offset_y_value,
                       self.current_text,
                       self.color,
                       self.font_combobox.get(),
                       self.font_size_value,
                       self.rotation_value]


        
    def update_canvas_modifier(self):
        self.canvas_modifier.update_text(params=self.params)

    def on_offset_x_slider_move(self,event):
        self.offset_x_value = float(self.offset_x_slider.get())
        self.params[0] = self.offset_x_value
        print(self.offset_x_value)
        self.update_canvas_modifier()

    def on_offset_y_slider_move(self,event):
        self.offset_y_value = float(self.offset_y_slider.get())
        self.params[1] = self.offset_y_value
        print(self.offset_y_value)
        self.update_canvas_modifier()

    def on_text_change(self, var_name, var_index, var_mode):
        self.current_text = self.text_input.get()
        self.params[2] = self.current_text
        print(self.current_text)
        self.update_canvas_modifier()

    def choose_color(self):
        self.color = colorchooser.askcolor(title="Choose color")[1]
        self.style.configure(
            style=f"ColorPrev{self.unique_style_name}.TLabel",
            background=self.color
        )
        self.params[3] = self.color
        self.update_canvas_modifier()


    def on_font_change(self,event):
        self.selected_font = self.font_combobox.get()
        self.text_entry.configure(font=(self.selected_font,11))
        self.params[4] = self.selected_font
        self.update_canvas_modifier()

    def on_font_size_slider_move(self,event):
        self.font_size_value = int(float(self.font_size_slider.get()))
        self.font_size_value_text.configure(text=f"{self.font_size_value:3d}")
        self.params[5] = self.font_size_value
        self.update_canvas_modifier()

    def on_rotation_slider_move(self,event):
        self.rotation_value = int(float(self.rotation_slider.get()))
        print(self.rotation_value) 
        self.params[6] = self.rotation_value
        self.update_canvas_modifier()

    def save_image(self):
        # will be developed after canvas modifier
        pass

        #also change canvas text after canvas modifier
    def on_canvas_resize(self, event):
        width = event.width - 4
        height = event.height - 4
        self.canvas.itemconfig(self.canvas_window, width=width, height=height)

    def panel_style(self):
        self.style.configure(
            style="Main.TFrame",
            background="#383938"
        )
        self.style.configure(
            style="Features.TLabel",
            background="#212121",
            foreground="#FFFFFF",
        )
        self.style.configure(
            style="Features.TFrame",
            background="#212121"
        )

        self.style.configure(
            style="Text.TLabel",
            background="#383938",
            foreground="#FFFFFF",
        )
        self.style.configure(
            style="Text.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="Text.TEntry",
            background="#383938",
            focuscolor="red"
        )

        self.style.configure(
            style="Color.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="Color.TLabel",
            background="#383938",
            foreground="#FFFFFF"
        )

        self.style.configure(
            style=f"ColorPrev{self.unique_style_name}.TLabel",
            background="#FFFFFF"
        )
        self.style.configure(
            style="Color.TButton",
            background="#212121",
            focuscolor="#212121",
            foreground="#FFFFFF",
            borderwidth=1,
            relief="flat"
        )

        self.style.map(
            style='Color.TButton',
            background=[
                ('active', '#313131'),
                ('hover', '#212121'),
                ('pressed', '#212121'),
            ]
        )

        self.style.configure(
            style="Save.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="Save.TButton",
            background="#212121",
            focuscolor="#212121",
            foreground="#FFFFFF",
            borderwidth=1,
            relief="flat"
        )

        self.style.map(
            style='Save.TButton',
            background=[
                ('active', '#313131'),
                ('hover', '#212121'),
                ('pressed', '#212121'),
            ]
        )

        self.style.configure(
            style="Font.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="Font.TLabel",
            background="#383938",
            foreground="#FFFFFF"
        )

        self.style.configure(
            style="Font.TCombobox",
            fieldbackground="#FFFFFF",
            background="#FFFFFF",
            foreground="#000000"
        )
        self.style.map(
            'Font.TCombobox',
            fieldbackground=[('readonly', '#FFFFFF')],
            selectbackground=[('readonly', '#FFFFFF')],
            selectforeground=[('readonly', '#000000')]
        )

        self.style.configure(
            style="FontSize.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="FontSize.TLabel",
            background="#383938",
            foreground="#FFFFFF"
        )

        self.style.configure(
            style="OffsetX.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="OffsetX.TLabel",
            background="#383938",
            foreground="#FFFFFF"
        )

        self.style.configure(
            style="OffsetY.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="OffsetY.TLabel",
            background="#383938",
            foreground="#FFFFFF"
        )
        self.style.configure(
            "TScale",
            background="#383938",
            troughcolor="#2a2b2a",
            borderwidth=1,
            lightcolor="#383938",
            darkcolor="#383938"
        )

        self.style.configure(
            style="Rotation.TFrame",
            background="#383938"
        )

        self.style.configure(
            style="Rotation.TLabel",
            background="#383938",
            foreground="#FFFFFF"
        )











