from tkinter.ttk import Style
class NotebookStyle:
    def __init__(self):
        self.style = Style()
        self.style.theme_use("default")

    def change_style(self,style_name):
        if style_name=="dark":
            self.notebook_dark_style()

    def notebook_dark_style(self):
        self.style.configure(
            style='FooterAddImage.TButton',
            background="#383938",
            focuscolor="#505050",
            borderwidth=0,
            font=('Verdana', '20')
        )
        self.style.map(
            style='FooterAddImage.TButton',
            background=[
                ('active', '#404040'),
            ]
        )
        self.style.configure(
            style='AddImage.TButton',
            background="#505050",
            focuscolor="#505050",
            borderwidth=0,
        )
        self.style.map(
            style='AddImage.TButton',
            background=[
                ('active', '#505050'),
                ('hover', '#505050'),
                ('pressed', '#505050'),
            ]
        )
        self.style.configure(
            style='TNotebook',
            background='#212121',
            padding=(5, 5),
            borderwidth=0
        )
        self.style.configure(
            style='TNotebook.Tab',
            background='#383938',
            foreground='#FFFFFF',
            focuscolor="#505050",
            font=('Verdana', '11', 'italic'),
            padding=(15, 3),
            borderwidth=0,
        )
        self.style.configure(
            style='TFrame',
            background="#505050",

        )
        self.style.map(
            style="TNotebook.Tab",
            background=[("selected", "#505050")]
        )