#tkinter
import  tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def sp(pg):
    pg.tkraise()

def register():
    print("Registered Data")
    print(rg_name.get())
    print(rg_phone.get())
    print(rg_email.get())
    print(rg_pass.get())
    messagebox.showinfo("Register","Register Successfully😊😊")


def login():
    print("Login Data")
    print(lg_email.get())
    print(lg_pass.get())
    messagebox.showinfo("Login", "Login Successfully😊😊")
    dg.tkraise()


main = tk.Tk()
main.geometry('1920x1080')
main.title('Demo GUI')
main.config(background='gray')

#Frame()
container = tk.Frame(main,bg='orange')
#pages
rg = tk.Frame(container,bg='#f48c06')
lg = tk.Frame(container,bg='#f48c06')
dg = tk.Frame(container,bg='#f48c06')

for page in (container,rg,lg,dg):
    page.place(x=0, y=0, width=1366,height=768)

# Register Page
title = tk.Label(rg,text="Register Form",bg='#f48c06',fg='#370617',font=("Arial bold",35))
title.place(x=620,y=130)

tk.Label(rg,text="User Name : ",bg='#f48c06',fg='#6a040f',font=("Arial bold",25)).place(x=560,y=220)
rg_name = tk.Entry(rg,bg='#f48c06',fg='#6a040f',font=("Arial bold",25),width=15)
rg_name.place(x=770,y=220)

tk.Label(rg,text="User Phone : ",bg='#f48c06',fg='#6a040f',font=("Arial bold",25)).place(x=560,y=290)
rg_phone = tk.Entry(rg,bg='#f48c06',fg='#6a040f',font=("Arial bold",25),width=15)
rg_phone.place(x=770,y=290)

tk.Label(rg,text="User Email : ",bg='#f48c06',fg='#6a040f',font=("Arial bold",25)).place(x=560,y=360)
rg_email = tk.Entry(rg,bg='#f48c06',fg='#6a040f',font=("Arial bold",25),width=15)
rg_email.place(x=770,y=360)

tk.Label(rg,text="Password : ",bg='#f48c06',fg='#6a040f',font=("Arial bold",25)).place(x=560,y=420)
rg_pass = tk.Entry(rg,bg='#f48c06',fg='#6a040f',font=("Arial bold",25),width=15,show='*')
rg_pass.place(x=770,y=420)

tk.Button(rg,bg='#03071e',fg='#ffba08',font=("Arial bold",25),text="Login Form",command=lambda:sp(lg)).place(x=600,y=500)
tk.Button(rg,bg='#03071e',fg='#ffba08',font=("Arial bold",25),text="Register",command=register).place(x=820,y=500)


# Login Page
title = tk.Label(lg,text="Login Form",bg='#f48c06',fg='#370617',font=("Arial bold",35))
title.place(x=640,y=250)

tk.Label(lg,text="User Email : ",bg='#f48c06',fg='#6a040f',font=("Arial bold",25)).place(x=560,y=360)
lg_email = tk.Entry(lg,bg='#f48c06',fg='#6a040f',font=("Arial bold",25),width=15)
lg_email.place(x=770,y=360)

tk.Label(lg,text="Password : ",bg='#f48c06',fg='#6a040f',font=("Arial bold",25)).place(x=560,y=420)
lg_pass = tk.Entry(lg,bg='#f48c06',fg='#6a040f',font=("Arial bold",25),width=15,show='*')
lg_pass.place(x=770,y=420)

tk.Button(lg,bg='#03071e',fg='#ffba08',font=("Arial bold",25),text="Register",command=lambda:sp(rg)).place(x=600,y=500)
tk.Button(lg,bg='#03071e',fg='#ffba08',font=("Arial bold",25),text="Login",command=login).place(x=790,y=500)


#Dashboard Page
title = tk.Label(dg,text="Welcome to Amazon",bg='#f48c06',fg='#370617',font=("Arial bold",35))
title.place(x=610,y=150)

img = Image.open(r"C:\Users\ELCOT\OneDrive\Pictures\richard-horvath-cPccYbPrF-A-unsplash (1).jpg")
img = img.resize((200,150))
sam25 = ImageTk.PhotoImage(img)
tk.Label(dg,image=sam25).place(x=250,y=250)
tk.Button(dg,image=sam25,command=lambda:sp(lg)).place(x=550,y=250)


dg.tkraise()
main.mainloop()