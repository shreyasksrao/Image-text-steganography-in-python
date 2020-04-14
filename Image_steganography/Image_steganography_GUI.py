import tkinter as tk
from tkfilebrowser import askopenfilename
import cv2
from tkinter import messagebox
import Image_steganography_logic

BACKGROUND = '#669966'


def resize_img(img, width, height, ip=cv2.INTER_CUBIC):
    image = cv2.imread(img, 1)
    r_width = width
    r_height = height
    resized_dimension = (r_width, r_height)
    resized = cv2.resize(image, resized_dimension, interpolation=ip)
    return resized


class Image_steganography(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.config(bg=BACKGROUND)

        self.file_name_var = tk.StringVar()
        self.file_name2_var = tk.StringVar()
        self.save_file_var = tk.StringVar()
        self.dim_var = tk.StringVar()

        self.top_frame = tk.Frame(self, bg=BACKGROUND, bd=10, height=20)
        self.top_frame.pack(expand=True, fill=tk.X, anchor='n')

        self.upper_frame = tk.Frame(self, bg=BACKGROUND, bd=10)
        self.upper_frame.pack(side='top', expand=True, fill=tk.BOTH, anchor='n')

        main_label = tk.Label(self.top_frame, text='{}IMAGE STEGANOGRAPHY{}'.format(60 * '-', 60 * '-'), bg='yellow',
                              font=('Times new roman', 16, 'bold'), relief='solid')
        main_label.grid(row=0, column=0, sticky=tk.E, padx=50)

        self.text2_label = tk.Label(self.upper_frame, text="Choose the source image :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 14, 'bold'))
        self.text2_label.grid(row=1, column=0, sticky=tk.E, pady=20)
        self.file_name_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.file_name_var, bg='white',
                                        bd=3, relief='sunken')
        self.file_name_entry.grid(row=1, column=1, pady=20, padx=10, sticky='w')

        self.choose_btn = tk.Button(self.upper_frame, text="Choose file", bg='red',
                                    command=lambda: self.take_file(flag=0))
        self.choose_btn.grid(row=1, column=2, pady=20, padx=10)

        self.text1_label = tk.Label(self.upper_frame, text="Choose the image to encrypt :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 14, 'bold'))
        self.text1_label.grid(row=2, column=0, sticky=tk.E, pady=20)
        self.file_name2_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.file_name2_var, bg='white',
                                         bd=3, relief='sunken')
        self.file_name2_entry.grid(row=2, column=1, pady=20, padx=10, sticky='w')
        self.choose_btn2 = tk.Button(self.upper_frame, text="Choose file", bg='red',
                                     command=lambda: self.take_file(flag=1))
        self.choose_btn2.grid(row=2, column=2, pady=20, padx=10)

        self.save_label = tk.Label(self.upper_frame, text='Save file name :', fg='black', bg=BACKGROUND,
                                   relief='solid', font=('consolas', 14, 'bold'))
        self.save_label.grid(row=3, column=0, sticky=tk.E, pady=10)
        self.save_file_name_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.save_file_var, bg='white',
                                             bd=3, relief='sunken')
        self.save_file_name_entry.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        self.dim_label = tk.Label(self.upper_frame, text='Enter dimension of image(width x height) :', fg='black',
                                  bg=BACKGROUND, relief='solid', font=('consolas', 14, 'bold'))
        self.dim_label.grid(row=4, column=0, sticky=tk.E, pady=10)
        self.dim_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.dim_var, bg='white',
                                  bd=3, relief='sunken')
        self.dim_entry.grid(row=4, column=1, pady=10, padx=10, sticky='w')

        self.encrypt_btn = tk.Button(self.upper_frame, text="ENCRYPT", bg='red',
                                     command=self.encrypt)
        self.encrypt_btn.grid(row=5, column=0, pady=20)

        self.decrypt_btn = tk.Button(self.upper_frame, text="DECRYPT", bg='red', command=self.decrypt)
        self.decrypt_btn.grid(row=5, column=1, pady=20, padx=10)

    def take_file(self, flag):
        file_name = askopenfilename(defaultextension=".png", title='Choose image file', initialdir='C:/Pictures',
                                    filetypes=[("All Files", "*.*"), ("PNG", "*.png"), ("JPEG", "*.jpg")])
        if flag == 0:
            self.file_name_var.set(file_name)
        else:
            self.file_name2_var.set(file_name)

    def encrypt(self):
        src = str(self.file_name_var.get())
        img = str(self.file_name2_var.get())
        new_name = str(self.save_file_var.get())
        ret = Image_steganography_logic.encode_driver(src, img, new_name)
        if ret == -1:
            messagebox.showerror('Encryption error', 'Image size is too big to encrypt\nResize the image and try....')
        else:
            messagebox.showinfo('Encryption Done', 'Image is successfully encrypted inside the source image')

    def decrypt(self):
        dim = str(self.dim_var.get())
        wid, hei = list(dim.split('x'))
        width = int(wid)
        height = int(hei)
        dec_img = str(self.save_file_var.get())
        img = str(self.file_name_var.get())
        lst = Image_steganography_logic.decode(img)
        Image_steganography_logic.weight_2_grey(lst, dec_img, width, height)
        messagebox.showinfo('Decryption Done', 'Image is successfully decrypted')
