class CanvasModifier:
    def __init__(self,canvas,canvas_size,image_size):
        self.canvas_size = (int(canvas_size[0]),int(canvas_size[1]))
        self.offset_x = canvas_size[0]/2
        self.offset_y = canvas_size[1]/2
        self.image_left_border = (canvas_size[0]/2 - image_size[0]/2)
        self.image_right_border = (canvas_size[0]/2 + image_size[0]/2)
        self.image_top_border = (canvas_size[1]/2 - image_size[1]/2)
        self.image_bottom_border = (canvas_size[1]/2 + image_size[1]/2)
        self.text = ""
        self.fill= "#FFFFFF"
        self.font = "Verdana"
        self.font_size = 11
        self.rotation = 0
        self.spacing = 11
        self.canvas_texts = {}
        self.canvas = canvas
        self.create_untiled_text()

    def create_untiled_text(self):
        self.delete_current_texts()
        canvas_text = self.canvas.create_text(
            self.offset_x,
            self.offset_y,
            text=self.text,
            fill=self.fill,
            font=(self.font, self.font_size),
            angle=self.rotation
        )
        self.canvas_texts[canvas_text] = [self.offset_x,self.offset_y]

    def create_repeating_grid_text(self):
        self.delete_current_texts()

        y_grid_length = (self.image_bottom_border - self.image_top_border)
        y_step = y_grid_length / self.spacing
        y_start_point = y_step/2

        y_end_point = y_grid_length

        x_grid_length = (self.image_right_border - self.image_left_border)
        x_step = x_grid_length / self.spacing

        while y_start_point <= y_end_point:
            x_start_point = x_step / 2

            x_end_point = x_grid_length
            while x_start_point <= x_end_point:
                x_point = self.image_left_border + x_start_point
                y_point = self.image_top_border + y_start_point
                canvas_text = self.canvas.create_text(
                    x_point,
                    y_point,
                    text=self.text,
                    fill=self.fill,
                    font=(self.font, self.font_size),
                    angle=self.rotation
                )
                self.canvas_texts[canvas_text] = [x_point,y_point]
                x_start_point += x_step
            y_start_point += y_step



    def delete_current_texts(self):
        for text in self.canvas_texts:
            self.canvas.delete(text)
        self.canvas_texts.clear()

    def update_spacing(self,spacing):
        self.spacing = spacing
        self.create_repeating_grid_text()

    def update_text(self,params):
        old_offset_x = self.offset_x
        old_offset_y = self.offset_y

        self.offset_x = params[0]
        self.offset_y = params[1]

        displacement_x = -(old_offset_x - self.offset_x)
        displacement_y = -(old_offset_y - self.offset_y)

        self.text = params[2]
        self.fill = params[3]
        self.font = params[4]
        self.font_size = params[5]
        self.rotation = params[6]

        for text,items in self.canvas_texts.items():
            new_x_coord = items[0] + displacement_x
            new_y_coord = items[1] + displacement_y

            if new_x_coord < self.image_left_border:
                new_x_coord = new_x_coord + self.image_right_border - (self.canvas_size[0]-self.image_right_border)
            elif new_x_coord > self.image_right_border:
                new_x_coord = new_x_coord - self.image_right_border + (self.canvas_size[0]-self.image_right_border)

            if new_y_coord < self.image_top_border:
                new_y_coord = new_y_coord + self.image_bottom_border - (self.canvas_size[1]-self.image_bottom_border)
            elif new_y_coord > self.image_bottom_border:
                new_y_coord = new_y_coord - self.image_bottom_border + (self.canvas_size[1]-self.image_bottom_border)

            self.canvas.coords(
                text,
                new_x_coord,
                new_y_coord
            )

            self.canvas_texts[text] = [new_x_coord,new_y_coord]

            self.canvas.itemconfig(
                text,
                text=self.text,
                fill=self.fill,
                font=(self.font,self.font_size),
                angle=self.rotation
            )


