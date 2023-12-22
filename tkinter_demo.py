from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def loging_handle():
    email = email_input.get()
    password = password_input.get()
    if(email=="sanjayjustforyou123@gmail.com" and password=="12345"):
        messagebox.showinfo("yahhh","Loging sucessful")
    else:
        messagebox.showerror("error","loging failed")
root = Tk()

root.title("Login id")
# root.minsize(500,500)
root.geometry('350x500')
root.configure(background='#0096DC')
img = Image.open("C:\\Users\\sanja\\Downloads\\flipkart.jpg")
resized_img = img.resize((70,70))
img1 = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img1)
img_label.pack(pady=(10,10))

text_label = Label(root,text="Flipkart",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana",24))

email_label = Label(root,text="Enter Email",fg="white",bg="#0096DC")
email_label.pack(pady=(10,5))
email_label.config(font=("verdana",12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1,15))

password_label = Label(root,text="Enter Password",fg="white",bg="#0096DC")
password_label.pack(pady=(10,5))
password_label.config(font=("verdana",12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))

login = Button(root, text="Login",fg="black", bg="white",width=20,height=3,command=loging_handle )
login.pack(pady=(10,20))
login.config(font=("verdana",10))
root.mainloop()  
