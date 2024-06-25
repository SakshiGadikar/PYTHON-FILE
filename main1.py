from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class login:
     def __init__(self, root):
          self.root = root
          self.root.title("Login System")
          self.root.geometry("1199x600+100+58")
          self.root.resizable(False, False)


          #background image
          self.bg=ImageTk.PhotoImage(file="Images/1.jpg")
          self.bg_image=Label(self.root, image=self.bg).place(x=20,y=20, relwidth=1, relheight=1)

          #login frame
          Frame_login = Frame(self.root, bg="white")
          Frame_login.place(x=330, y=150, width=500, height=400)

          #Title & Subtitle
          title= Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF",
                       bg="White").place(x=90, y=30)
          subtitle= Label(Frame_login, text="Members Login Area ", font=("Goudy Old Style", 15, "bold"), fg="#1d1d1d",
                       bg="White").place(x=90, y=100)
          
          #username
          lbl_user= Label(Frame_login, text="Username ", font=("Goudy Old Style", 15, "bold"), fg="Grey",
                       bg="White").place(x=90, y=140)
          self.username= Entry(Frame_login,  font=("Goudy Old Style", 15),  bg="#E7E6E6")
          self.username.place(x=90, y=170, width=320, height=35)
          
          #Password
          lbl_password= Label(Frame_login, text="Password", font=("Goudy Old Style", 15, "bold"), fg="Grey",
                       bg="White").place(x=90, y=210)
          self.password= Entry(Frame_login,  font=("Goudy Old Style", 15),  bg="#E7E6E6")
          self.password.place(x=90, y=240, width=320, height=35)
          
          #Button
          forget = Button(Frame_login, text="Forget Password",border="0",cursor="hand2" ,font=("Goudy Old Style", 12), fg="#6162FF",
                       bg="White").place(x=90, y=280)
          Submit = Button(Frame_login,cursor="hand2", text="login?", bd="0" ,font=("Goudy Old Style", 15), bg="#6162FF",
                       fg="White").place(x=90, y=320, width="180", height="40")
          
          def check_function(self):
                if self.username.get() =="" or self.password.get() =="":
                   messagebox.showerror("Error", "All Fields are Required", Parent=self.root)
                elif self.username.get() != "Tech2etc" or self.password.get() != "123456":
                   messagebox.showerror("Error", "Invalid Username or Password", Parent=self.root)
                else:
                   messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")



root = Tk()
obj = login(root)
root.mainloop()