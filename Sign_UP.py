import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
# SignUp class
class SignUp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('500x650')
        self.maxsize(500, 650)
        self.title('Registration')

        self.label = Label(self, text="Registration Form",  # text
                           font=('Arial', 24, 'bold'),  # font ->
                           pady=20,  # padding
                           compound='top')  # add photo
        self.label.pack()  # position
        self.label1 = Label(self, text="First Name :",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=20, y=100)  # position
        self.fname = Entry(self,
                           font=("Arial", 18), width=24

                           )
        self.fname.place(x=150, y=120)

        self.label2 = Label(self, text="Last Name :",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=20, y=170)  # position
        self.lname = Entry(self,
                           font=("Arial", 18), width=24

                           )
        self.lname.place(x=150, y=190)

        # phone
        self.label3 = Label(self, text="Phone :",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label3.place(x=20, y=240)  # position
        self.phone = Entry(self,
                           font=("Arial", 18), width=24

                           )
        self.phone.place(x=150, y=260)

        # username
        self.label4 = Label(self, text="Username :",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label4.place(x=20, y=310)  # position
        self.username = Entry(self,
                              font=("Arial", 18), width=24

                              )
        self.username.place(x=150, y=330)

        self.label5 = Label(self, text="Password :",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label5.place(x=20, y=380)  # position
        self.password = Entry(self,
                              font=("Arial", 18), show="*", width=24

                              )
        self.password.place(x=150, y=400)

        self.button1 = Button(self, text=" Create ", font=("Arial", 12, "bold"), fg="white", bg="#2E8B57", width=10,
                              command=self.create).place(x=50, y=515)
        self.button2 = Button(self, text=" Clear ", font=("Arial", 12, "bold"), fg="white", bg="#33FFBD", width=10,
                              command=self.clear).place(x=190, y=515)
        self.button3 = Button(self, text=" Exit ", font=("Arial", 12, "bold"), fg="white", bg="#FA8072", width=10,
                              command=self.ex).place(x=330, y=515)

    def create(self):
        fn = self.fname.get()
        ln = self.lname.get()
        name = fn + " " + ln
        phn = self.phone.get()
        usern = self.username.get()
        passN = self.password.get()

        if (fn == "" or ln == "" or phn == "" or usern == "" or passN == ""):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute(
                    "insert into Admin_Registration values('" + name + "','" + phn + "','" + usern + "','" + passN + "')")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Created successfully");
                con.close();
                # self.fname.set(0,"aaaa")
                self.fname.delete(0, END)
                # self.fname.insert(0,"alamin")

                self.lname.delete(0, END)
                # self.lname.insert(0,"alamin")

                self.phone.delete(0, END)
                # self.phone.insert(0, "alamin")

                self.username.delete(0, END)
                # self.username.insert(0, "alamin")
                self.password.delete(0, END)
                # self.password.insert(0, "alamin")
            except:
                cursor.set("Database error")

        return

    def clear(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.username.delete(0, END)
        self.phone.delete(0, END)
        self.password.delete(0, END)

    def ex(self):
        self.destroy()

