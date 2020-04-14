import tkinter as tk
from tkfilebrowser import askopenfilename
from tkinter import messagebox
import cv2

BACKGROUND = 'cyan'


class Resize(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.config(bg=BACKGROUND)

        self.file_name_var = tk.StringVar()
        self.width_var = tk.IntVar()
        self.height_var = tk.IntVar()
        self.save_var = tk.StringVar()

        self.top_frame = tk.Frame(self, bg=BACKGROUND, bd=10, height=20)
        self.top_frame.pack(expand=True, fill=tk.X, anchor='n')

        self.upper_frame = tk.Frame(self, bg=BACKGROUND, bd=10)
        self.upper_frame.pack(side='top', expand=True, fill=tk.BOTH, anchor='n')

        main_label = tk.Label(self.top_frame, text='{}IMAGE RESIZING WINDOW{}'.format(60 * '-', 60 * '-'), bg='yellow',
                              font=('Times new roman', 16, 'bold'), relief='solid')
        main_label.grid(row=0, column=0, sticky=tk.E, padx=50)

        self.text2_label = tk.Label(self.upper_frame, text="Choose Image to resize :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 14, 'bold'))
        self.text2_label.grid(row=1, column=0, sticky=tk.E, pady=20)
        self.file_name_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.file_name_var, bg='white',
                                        bd=3, relief='sunken')
        self.file_name_entry.grid(row=1, column=1, pady=20, padx=10, sticky='w')

        self.choose_btn = tk.Button(self.upper_frame, text="Choose file", bg='red', command=self.take_file)
        self.choose_btn.grid(row=1, column=2, pady=20, padx=10)

        self.text3_label = tk.Label(self.upper_frame, text="Width of new image :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 14, 'bold'))
        self.text3_label.grid(row=2, column=0, sticky=tk.E, pady=20)
        self.width_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.width_var, bg='white',
                                    bd=3, relief='sunken')
        self.width_entry.grid(row=2, column=1, pady=20, padx=10, sticky='w')

        self.text4_label = tk.Label(self.upper_frame, text="Height of new image :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 14, 'bold'))
        self.text4_label.grid(row=3, column=0, sticky=tk.E, pady=20)
        self.height_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.height_var, bg='white',
                                     bd=3, relief='sunken')
        self.height_entry.grid(row=3, column=1, pady=20, padx=10, sticky='w')

        self.text5_label = tk.Label(self.upper_frame, text="Save file name :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 14, 'bold'))
        self.text5_label.grid(row=4, column=0, sticky=tk.E, pady=20)
        self.save_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.save_var, bg='white',
                                   bd=3, relief='sunken')
        self.save_entry.grid(row=4, column=1, pady=20, padx=10, sticky='w')

        self.resize_btn = tk.Button(self.upper_frame, text="RESIZE", bg='red',
                                    command=self.resize)
        self.resize_btn.grid(row=5, column=0, pady=20)

    def take_file(self):
        file_name = askopenfilename(defaultextension=".png", title='Choose image file', initialdir='C:/Pictures',
                                    filetypes=[("All Files", "*.*"), ("PNG", "*.png"), ("JPEG", "*.jpg")])
        self.file_name_var.set(file_name)

    def resize(self):
        image = str(self.file_name_var.get())
        width = int(self.width_var.get())
        height = int(self.height_var.get())
        save_file = 'Resized Images/' + str(self.save_var.get())
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(save_file, resized)
        messagebox.showinfo('Resize Done', 'Image is successfully resized\nName : {}'.format(save_file))
