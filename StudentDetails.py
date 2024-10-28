import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *

from tkinter import messagebox
import mysql.connector as mysql
from datetime import date
class StudentDetail(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)


        self.geometry('1366x760')
        self.title('Student Details')
        self.resizable(width=0, height=0)

        #search box create
        self.label1 = Label(self, text="Student ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=50, y=10)  # position
        self.studentid = Entry(self,
                            font=("Arial", 18), width=26

                            )

        self.studentid.place(x=170, y=30)

        self.label2 = Label(self, text="Department:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=610, y=10)  # position

        # Adding combobox drop down list
        self.choosen = ("CSE", "EEE", "BBA", "CIVIL", "NFE", "SWE", "Textile")
        self.selected_de = tk.StringVar()

        self.cb = ttk.Combobox(self, textvariable=self.selected_de, font=("Arial", 18), width=26)
        self.cb['values'] = self.choosen
        self.cb['state'] = 'readonly'  # normal
        self.cb.place(x=730, y=30)

        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",command=self.searchBook1).place(x=526, y=29)
        self.button1 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",command=self.searchBook2).place(x=1100,y=29)
        self.button2 = Button(self, text="Refresh", font=("Arial", 12, "bold"), fg="white", bg="#6495ED",command=self.refresh).place(x=1230,
                                                                                                               y=29)

        #add

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM studentlist")
        except:
            cursor.set("Database error")

        self.tree=ttk.Treeview(self, height="19")
        self.tree['show']='headings'

        style = ttk.Style()
        style.theme_use("clam")


        style.configure("Treeview.Heading", font=(None,16,'bold'),background='#117A65', foreground='white')
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 16),rowheight=30)


        #column
        self.tree["columns"]=("StudentID","FullName","Email","MobileNo","Department","Gender")
        self.tree.column("StudentID",width=150,minwidth=50,anchor="center")
        self.tree.column("FullName", width=250, minwidth=50)
        self.tree.column("Email", width=350, minwidth=50)
        self.tree.column("MobileNo", width=170, minwidth=50,anchor="center")
        self.tree.column("Department", width=170, minwidth=50,anchor="center")
        self.tree.column("Gender", width=170, minwidth=50,anchor="center")

            #heading
        self.tree.heading("StudentID",text="Student ID")
        self.tree.heading("FullName", text="Full Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("MobileNo", text="Mobile No",)
        self.tree.heading("Department", text="Department")
        self.tree.heading("Gender", text="Gender")
        self.tree.place(x=50, y=100)

        i = 0

        for ro in cursor:
            if i%2==0:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('even',))
            else:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('odd',))

            i=i+1
        self.tree.tag_configure('even', background='#D0ECE7' ,foreground='black')
        self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')






    def searchBook1(self):
        stid = self.studentid.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        if (stid == ""):
            messagebox.showinfo("Insert Status", "please enter Book id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `studentlist` WHERE `student_Id` LIKE '%" + stid + "%'")
            except:
                cursor.set("Database error")

            i = 0

            for ro in cursor:
                if i % 2 == 0:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('even',))
                else:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('odd',))

                i = i + 1
            self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
            self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')

            self.studentid.delete(0,END)

    def searchBook2(self):
        de = self.selected_de.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        if (de == ""):
            messagebox.showinfo("Insert Status", "please enter Book id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `studentlist` WHERE `department` LIKE '%" + de + "%'")
            except:
                cursor.set("Database error")

            i = 0

            for ro in cursor:
                if i % 2 == 0:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('even',))
                else:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('odd',))

                i = i + 1
            self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
            self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')

            self.selected_de.set("")


    def refresh(self):

        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM studentlist")
        except:
            cursor.set("Database error")

        i = 0

        for ro in cursor:
            if i % 2 == 0:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('even',))
            else:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('odd',))

            i = i + 1
        self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
        self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')






