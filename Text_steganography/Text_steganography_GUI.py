import tkinter as tk
import tkinter.scrolledtext as st
from tkfilebrowser import askopenfilename
import cv2
import Text_steganography_logic
from tkinter import messagebox

BACKGROUND = 'yellow'


class Text_steganography(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=BACKGROUND)

        self.file_name_var = tk.StringVar()
        self.save_file_var = tk.StringVar()

        self.top_frame = tk.Frame(self, bg=BACKGROUND, bd=10, height=20)
        self.top_frame.pack(expand=True, fill=tk.X, anchor='n')

        self.upper_frame = tk.Frame(self, bg=BACKGROUND, bd=10)
        self.upper_frame.pack(side='top', expand=True, fill=tk.BOTH, anchor='n')

        self.lower_frame = tk.Frame(self, bg='pink', bd=10, height=100)
        self.lower_frame.pack(side='top', expand=True, fill=tk.BOTH, anchor='n')

        main_label = tk.Label(self.top_frame, text='{}TEXT STEGANOGRAPHY{}'.format(60*'-', 60*'-'), bg='yellow',
                              font=('Times new roman', 16, 'bold'), relief='solid')
        main_label.grid(row=0, column=0, sticky=tk.E, padx=50)

        self.text_label = tk.Label(self.upper_frame, text="Text to Encrypt :", fg='black', bg=BACKGROUND,
                                   relief='solid', font=('consolas', 16, 'bold'))
        self.text_label.grid(row=1, column=0, sticky=tk.E, pady=10)
        self.text = st.ScrolledText(self.upper_frame, height=10, relief='solid')
        self.text.grid(row=1, column=1, padx=10)

        self.text2_label = tk.Label(self.upper_frame, text="Choose the File name :", fg="black", bg=BACKGROUND,
                                    relief='solid', font=('consolas', 16, 'bold'))
        self.text2_label.grid(row=2, column=0, sticky=tk.E, pady=20)
        self.file_name_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.file_name_var, bg='white',
                                        bd=3, relief='sunken')
        self.file_name_entry.grid(row=2, column=1, pady=20, padx=10, sticky='w')
        self.choose_btn = tk.Button(self.upper_frame, text="Choose file", bg='red', command=self.take_file)
        self.choose_btn.grid(row=2, column=2, pady=20, padx=10)

        self.save_label = tk.Label(self.upper_frame, text='Save file name :', fg='black', bg=BACKGROUND,
                                   relief='solid', font=('consolas', 16, 'bold'))
        self.save_label.grid(row=3, column=0, sticky=tk.E, pady=10)
        self.save_file_name_entry = tk.Entry(self.upper_frame, width=100, textvariable=self.save_file_var, bg='white',
                                             bd=3, relief='sunken')
        self.save_file_name_entry.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        self.encrypt_btn = tk.Button(self.upper_frame, text="ENCRYPT", bg='red',
                                     command=self.encrypt)
        self.encrypt_btn.grid(row=4, column=0, pady=20)

        self.decrypt_btn = tk.Button(self.upper_frame, text="DECRYPT", bg='red', command=self.decrypt)
        self.decrypt_btn.grid(row=4, column=1, pady=20, padx=10)

        self.label1 = tk.Label(self.lower_frame, text='Details about Image..', bg='black', fg='white', anchor='n')
        self.label1.pack(expand=True, fill=tk.BOTH, anchor='n')

    def take_file(self):
        self.file_name = askopenfilename(defaultextension=".png", title='Choose image file', initialdir='C:\Pictures',
                                         filetypes=[("All Files", "*.*"),
                                                    ("PNG", "*.png"),
                                                    ("JPEG", "*.jpg")])
        self.file_name_var.set(self.file_name)

        w, h = self.get_dimension_of_original_img()
        max_let = self.image_characters(w, h)
        text = 'Details about Image\nFile name : {}\t\tImage Dimension : {}x{}\
        \t\tMaximum letters encoded : {}\t\t'.format(self.file_name, w, h, max_let)
        self.label1.config(text=text)

    def get_text(self):
        text = str(self.text.get('1.0', tk.END))
        length = len(text)
        return [text, length]

    def get_save_fname(self):
        return str(self.save_file_var.get())

    def get_dimension_of_original_img(self):
        file = str(self.file_name_var.get())
        image = cv2.imread(file, cv2.IMREAD_UNCHANGED)
        self.width = int(image.shape[1])
        self.height = int(image.shape[0])
        return self.width, self.height

    def image_characters(self, width, height):
        total_pixels = width * height
        total_rgb_vals = total_pixels * 3
        max_letters_encoded = int(total_rgb_vals/9)
        return max_letters_encoded

    def encrypt(self):
        text, length = self.get_text()
        img = self.file_name_var.get()
        new_img = self.get_save_fname()
        if length == 0:
            messagebox.showerror("Encryption error", 'Data is not entered\n Please enter data in the TEXT widget')
        elif self.file_name_var.get() == "":
            messagebox.showerror("File error", 'Source Image has not chosen\n Please select the Image file')
        else:
            data = Text_steganography_logic.encode(img=str(img), data=text, new_img_name=new_img, save_flag=1)
            print(data)
            print(length)
            print(text)
            messagebox.showinfo("Encryption Done", 'Data is encrypted inside the image\n{}'.format(new_img))

    def decrypt(self):
        image = str(self.file_name_var.get())
        decoded_data = Text_steganography_logic.decode(image)
        if decoded_data == 0:
            messagebox.showerror("File not found", "File with given name does not exist\nGive valid name")
        self.text.delete('1.0', tk.END)
        text = '..............DECODED DATA..............\n' + decoded_data
        self.text.insert('1.0', text)
