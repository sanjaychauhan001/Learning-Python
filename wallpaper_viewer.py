from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_image():
    global counter
    img_label.config(image=img_arr[counter%len(img_arr)])
    counter = counter + 1


counter = 1
root = Tk()
root.configure(background="black")
root.title("Wallpaper")
root.geometry("250x400")


files = os.listdir("C:\\Users\\sanja\\OneDrive\\Pictures\\wallpaper")
img_arr = []
for file in files:
    img = Image.open(os.path.join("C:\\Users\\sanja\\OneDrive\\Pictures\\wallpaper",file))
    resized_image = img.resize((200,300))
    img_arr.append(ImageTk.PhotoImage(resized_image))

img_label = Label(root,image=img_arr[0])
img_label.pack(pady=(20,10))

next_btn = Button(root,text="Next", bg="white", fg="black",width=28,height=2,command=rotate_image)
next_btn.pack()


root.mainloop()