from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def login_window():
    #print("click")
    email = email_input.get()
    password = password_input.get()

    if email == "sobhanmaity5@gmail.com" and password == "1234":
        messagebox.showinfo("Success","Login Successful")
    else:
        messagebox.showerror("Error","Login Failed")


root = Tk()

root.title("Jana Computer Application Form")

#root.iconbitmap("computer.ico")

#root.minsize(600,600)

#root.maxsize(600,600)

root.geometry("350x500")

root.configure(background= "#00BFFF")

img = Image.open("flipkart-logo.png")

img_resized = img.resize((100,100))

img = ImageTk.PhotoImage(img_resized)

img_label = Label(root, image=img)

img_label.pack(pady=(10,10))

text_label = Label(root, text = "Flipkart", fg = "white", bg = "#0096DC")
text_label.pack()
text_label.config(font=("verdana",25))


#name_label = Label(root, text = "Enter Username", fg = "white", bg = "#0096DC")
#name_label.pack(pady=(20,5))
#name_label.config(font=("verdana",12))

#name_input = Entry(root,width=50)
#name_input.pack(ipady=6,pady=(1,15))


email_label = Label(root, text = "Enter Email", fg = "white", bg = "#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root, text = "Enter Password", fg = "white", bg = "#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text = "Please Login", bg = "white", fg = "black", width = 20, height = 2, command = login_window)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",10))


root.mainloop()