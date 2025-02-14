from PIL import Image, ImageDraw, ImageTk,ImageFont

class CanvasModifier:
    def __init__(self,canvas,canvas_size):
        self.canvas_size = (int(canvas_size[0]),int(canvas_size[1]))
        self.offset_x = canvas_size[0]/2
        self.offset_y = canvas_size[1]/2
        self.text = "Merhaba"
        self.fill= "#FFFFFF"
        self.font = "Verdana"
        self.font_size = 11
        self.rotation = 0

        self.canvas = canvas
        self.canvas_text = self.canvas.create_text(
            self.offset_x,
            self.offset_y,
            text=self.text,
            fill=self.fill,
            font = (self.font,self.font_size),
            angle = self.rotation
        )



    def update_text(self,params):
        self.offset_x = params[0]
        self.offset_y = params[1]
        self.text = params[2]
        self.fill = params[3]
        self.font = params[4]
        self.font_size = params[5]
        self.rotation = params[6]

        self.canvas.coords(
            self.canvas_text,
            self.offset_x,
            self.offset_y
        )

        self.canvas.itemconfig(
            self.canvas_text,
            text=self.text,
            fill=self.fill,
            font=(self.font,self.font_size),
            angle=self.rotation
        )
