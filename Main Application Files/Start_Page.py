import tkinter as tk
import Text_steganography
import Image_steganography
import Resize

BACKGROUND = '#444400'

class Start_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=BACKGROUND)
        main_frame = tk.Frame(self, bg=BACKGROUND)
        main_frame.pack(expand=True, fill=tk.BOTH)
        label = tk.Label(main_frame, text='STEGANOGRAPHY APPLICATION', font=('Helvetica', 16, 'bold'), bg=BACKGROUND)
        label.pack(side='top', fill='x', pady=30)
        self.text_stg_btn = tk.Button(main_frame, text="HIDING TEXT INSIDE IMAGE", bg='#00aaaa',
                                      font=('Helvetica', 16, 'bold'), overrelief=tk.RAISED,
                                      command=lambda: controller.show_frame(Text_steganography.Text_steganography))
        self.text_stg_btn.pack(side='top', fill='x', pady=10)
        self.img_stg_btn = tk.Button(main_frame, text="HIDING IMAGE INSIDE IMAGE", bg='#aa0000',
                                     font=('Helvetica', 16, 'bold'), overrelief=tk.RAISED,
                                     command=lambda: controller.show_frame(Image_steganography.Image_steganography))
        self.img_stg_btn.pack(side='top', fill='x', pady=10)
        self.resize_btn = tk.Button(main_frame, text="RESIZE IMAGE", bg='#888800',
                                    font=('Helvetica', 16, 'bold'), overrelief=tk.RAISED,
                                    command=lambda: controller.show_frame(Resize.Resize))
        self.resize_btn.pack(side='top', fill='x', pady=10)
