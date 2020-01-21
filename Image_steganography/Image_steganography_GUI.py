import tkinter as tk
import Text_steganography
import Image_steganography
import Resize
import Start_Page


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        icon = tk.PhotoImage(file='Crypto.ico')
        self.call('wm', 'iconphoto', self._w, icon)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.MenuBar = tk.Menu(self)
        self.Home_menu = tk.Menu(self.MenuBar, tearoff=0, bg='pink', activebackground='grey')
        self.MenuBar.add_cascade(label="Home", menu=self.Home_menu)
        self.Home_menu.add_command(label='Go To Home', foreground='black', command=self.go_to_home)
        self.config(menu=self.MenuBar)

        self.frames = {}
        for Frame in (Text_steganography.Text_steganography, Image_steganography.Image_steganography, Resize.Resize,
                      Start_Page.Start_Page):
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Start_Page.Start_Page)

    def show_frame(self, con):
        frame = self.frames[con]
        frame.tkraise()

    def go_to_home(self):
        self.show_frame(Start_Page.Start_Page)


app = Application()
app.minsize(width=1080, height=720)
app.title('Image Steganography')
app.mainloop()
