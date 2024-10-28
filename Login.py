import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mysql
from Sign_UP import SignUp
from HomePage import Home
#Loginpage class
class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1166x720')
        self.title('Library Management System')
        self.maxsize(1166, 720)
        self.resizable(width=0, height=0)

        # setbackground
        self.image = Image.open("Photo/back1.png")
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.username = Entry(self,
                         font=("Arial", 21)

                         )
        self.username.place(x=425, y=370)
        self.password = Entry(self,
                         font=("Arial", 21),
                         show="*"

                         )
        self.password.place(x=425, y=443)
        button1 = Button(self, text=" Login ", font=("Arial", 12, "bold"), fg="white", bg="#2E4369", width=8,
                         command=self.login).place(x=460, y=515)
        button2 = Button(self, text="Sign Up", font=("Arial", 12, "bold"), fg="white", bg="#2E4369", width=8,
                         command=self.sign).place(x=610, y=515)

    def login(self):
        user = self.username.get()
        passw = self.password.get()

        con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM `admin_registration` WHERE `Username` LIKE '%" + user + "%' AND `Password` LIKE '%" + passw + "%'")
        results = cursor.fetchall()

        con.close();
        i = 0
        if results:
            for i in results:
               userD=i[2]
               passD=i[3]
            if(user==userD and passw==passD):

                self.withdraw()
                window = Home(self)
                window.grab_set()


            elif(user=="" or passw==""):
                messagebox.showinfo("Empty", "Please enter your username and password!");
        else:
            messagebox.showinfo("Incorrect", "Incorrect Password");
            self.username.delete(0, END)
            self.password.delete(0, END)



    def sign(self):

        window = SignUp(self)
        window.grab_set()



#main method----------------------------------
if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()