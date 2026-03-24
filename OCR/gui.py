import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
from tesseract import getText


class GUI():

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("1200x1000")
        self.root.title("Image to Text")
        
        self.label = tk.Label(self.root, text="Image to Text", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.browserframe = tk.Frame(self.root)
        self.browserframe.columnconfigure(0, weight=1)
        self.browserframe.columnconfigure(1, weight=1)

        self.browsetext = tk.Text(self.browserframe, height=1, font=('Arial', 12))
        self.browsetext.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.browsebtn = tk.Button(self.browserframe, text="Browse", font=('Arial', 12), command=self.getimage)
        self.browsebtn.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.browserframe.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=30, font=('Arial', 14))
        self.textbox.pack(padx=10, pady=50)


        self.saveframe = tk.Frame(self.root)
        self.saveframe.columnconfigure(0, weight=1)
        self.saveframe.columnconfigure(1, weight=1)
        self.saveframe.columnconfigure(2, weight=1)
        self.saveframe.columnconfigure(3, weight=1)

        self.savelabel = tk.Label(self.saveframe, text="Save Location:", font=('Arial', 12))
        self.savelabel.grid(row=0, column=0, sticky=tk.W+tk.E)  
        self.savetext = tk.Text(self.saveframe, height=1, font=('Arial', 12))
        self.savetext.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.savetype = ttk.Combobox(self.saveframe, values=["Append", "Overwrite"], font=('Arial', 12))
        self.savetype.set("Append")
        self.savetype.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.savebutton = tk.Button(self.saveframe, text="Save", font=('Arial', 12), command=self.save)
        self.savebutton.grid(row=0, column=3, sticky=tk.W+tk.E)

        self.saveframe.pack(padx=5, pady=5)
        
        self.clearbutton = tk.Button(self.root, text="Clear", font=('Arial', 12), command=self.clear)
        self.clearbutton.pack()

        self.root.mainloop()


    def getimage(self):

        file = filedialog.askopenfile(mode='r', filetypes=[('Images', '*.png *.jpg')])

        if file:
            filepath = os.path.abspath(file.name)
            self.browsetext.insert('1.0', filepath)

            returned_text = getText(filepath)
            self.textbox.insert('1.0', returned_text)


    def clear(self):
        self.browsetext.delete('1.0', tk.END)
        self.textbox.delete('1.0', tk.END)
        self.savetext.delete('1.0', tk.END)


    def save(self):

        text_to_save = self.textbox.get('1.0', tk.END)

        file = filedialog.askopenfile(mode='r', filetypes=[('Plain Text', '*.txt'), ('Open Document Text', '*.odt'), ('Markdown', '*.md')])


        if file:
            filepath = os.path.abspath(file.name)
            self.savetext.insert('1.0', filepath)

            savetype = self.savetype.get()
            if savetype == "Append": savetype = "a" 
            elif savetype == "Overwrite": savetype = "w"

            with open(filepath, savetype) as txt:
                txt.write(text_to_save)

            if messagebox.askyesno(title="Clear Text?", message="Saved Successfully! Do you want to clear all existing texts?"):
                self.clear()
        
        else:
            messagebox.showinfo(title="Error!", text="Invalid File..")
        
    
            
GUI()





