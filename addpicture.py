

from PIL import image 
import tkinter as tk 

image = image.open("addpicture/image.jpg")


 
root= tk.Tk()

photo= image.Tk.photoimage(image)

label =  tk.Label(root, image=photo)

label.pack()


root.mainloop()












