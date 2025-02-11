from tkinter.ttk import Notebook,Style,Frame

class FrameNotebook:
    def __init__(self,root):
        # Root reference
        self.root = root
        # Style
        self.style = Style()
        self.style.theme_use("default")
        # Notebook style
        self.notebook_style()
        # Frames notebook
        self.notebook = Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')
        # Notebook tabs
        self.image_tab = self.create_new_tab()
        self.image_tab.pack_propagate(False)
        self.sample = self.create_new_tab()
        self.sample.pack_propagate(False)

        # Add to notebook
        self.notebook.add(self.image_tab, text="Images")
        self.notebook.add(self.sample, text="sample")

        self.style.configure("TNotebook")

    def create_new_tab(self):
        tab = Frame(self.notebook)
        return tab

    def notebook_style(self):
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
            font=('Adobe Ming Std L', '11', 'italic'),
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