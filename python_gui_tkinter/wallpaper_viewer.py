from tkinter import *
from PIL import ImageTk,Image
import os


def rotate_image():
    global counter
    img_label.config(image = img_array[counter%len(img_array)])
    counter = counter + 1

counter = 1
root = Tk()
root.title("Wallpaper Viewer")

root.geometry("350x400")
root.configure(background="#1E90FF")

files = os.listdir("wallpapers")
#print(files)

img_array = []
for file in files:
    img = Image.open(os.path.join("wallpapers",file))
    resized_img = img.resize((440,340))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image = img_array[0])
img_label.pack(pady=(3,5))

next_btn = Button(root, text="Next", bg="white",fg="#FF4500",width=28,height=2,command=rotate_image)
next_btn.pack()


root.mainloop()

