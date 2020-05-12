from tkinter import *
from tkinter import Tk, ttk
import tkinter as tk
import PIL 
# from PIL import ImageTk,Image


class Example(Frame):

    def __init__(self, parent):
        # bg = Image.open("bg.jpg")
        # background_image=ImageTk.PhotoImage(bg)
        # background_label = Label(parent, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("NLP Avratech7")
        self.style = ttk.Style(parent)
        self.style.theme_use("alt")
        self.style.configure("Label", background="black", 
                fieldbackground="black", foreground="white")
        self.centreWindow()
        self.pack(fill=tk.BOTH, expand=1)
        
       
   
        host = Label(self, text="Host")
        host.grid(row=0, column=0, sticky=W+E)
        dbName = Label(self, text="DB Name")
        dbName.grid(row=1, column=0, sticky=W+E)
        user = Label(self, text="User")
        user.grid(row=2, column=0, sticky=W+E)
        passowrd = Label(self, text="Passowrd")
        passowrd.grid(row=3, column=0, pady=10, sticky=W+E+N)
        url = Label(self, text="URL")
        url.grid(row=4, column=0, pady=10, sticky=W+E+N)
        label = Label(self, text="Label")
        label.grid(row=5, column=0, pady=10, sticky=W+E+N)
        
        hostText = Entry(self, width=20)
        hostText.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        dbnameText = Entry(self, width=20)
        dbnameText.grid(row=1, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        userText = Entry(self, width=20)
        userText.grid(row=2, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        passowrdText = Entry(self, width=20)
        passowrdText.grid(row=3, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        urlText = Entry(self, width=20)
        urlText.grid(row=4, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        labelText = Entry(self, width=40)
        labelText.grid(row=5, column=1, padx=5, pady=5, ipady=2, sticky=W+E)
        
       
        okBtn = Button(self, text="OK", width=10, command=self.onConfirm)
        okBtn.grid(row=6, column=0, padx=5, pady=3, sticky=W+E)
        closeBtn = Button(self, text="Close", width=10, command=self.onExit)
        closeBtn.grid(row=6, column=1, padx=5, pady=3, sticky=W+E)
    
    def centreWindow(self):
        w = 450
        h = 295
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onExit(self):
        self.quit()
  

  
    
    def onConfirm(self):
        box.showinfo("Information", "Thank you!")

def main():
    root = Tk()
    
    root.resizable(width=TRUE, height=TRUE)
    # resizable
    root.configure(background='black')
    app = Example(root)

    

    root.mainloop()

if __name__ == '__main__':
    main()