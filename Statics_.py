import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *

from tkcalendar import Calendar, DateEntry

import mysql.connector as mysql

#Statics class
class Statics(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('1366x760')
        self.title('Statics')
        self.resizable(width=0, height=0)

        # Create a Calendar using DateEntry
        self.cal = DateEntry(self, width=16, background="magenta3", foreground="white", bd=2, font=('Arial', 16),
                             date_pattern='dd/MM/yyyy')

        self.cal.place(x=110, y=30)


        self.label = Label(self, text="Date:",  # text
                            font=('Arial', 16),  # font ->
                              # padding
                            compound='top')  # add photo
        self.label.place(x=50, y=30)  # position

        #heading

        self.label1 = Label(self, text="Issues Book",  # text
                           font=('Arial',24,'bold','underline'),  # font ->
                           # padding
                           compound='top')  # add photo
        self.label1.place(x=594, y=65)  # position

        self.label2 = Label(self, text="Return Book",  # text
                            font=('Arial', 24, 'bold','underline'),  # font ->
                            # padding
                            compound='top')  # add photo
        self.label2.place(x=594, y=395)  # position

        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",command=self.searchBook).place(x=340, y=29)

        # add


        d=self.cal.get()
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM `issuebookstatics` WHERE `IssueDate` LIKE '%" + d + "%'")
        except:
            cursor.set("Database error")

        self.tree = ttk.Treeview(self, height="8")
        self.tree['show'] = 'headings'
        self.tree1 = ttk.Treeview(self, height="8")
        self.tree1['show'] = 'headings'

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview.Heading", font=(None, 16, 'bold'), background='#117A65', foreground='white')
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 16), rowheight=30)


        # column
        self.tree["columns"] = ("BookID","StudentID", "IssueDate", "DueDate")
        self.tree.column("BookID", width=280, minwidth=50, anchor="center")
        self.tree.column("StudentID", width=280, minwidth=50, anchor="center")
        self.tree.column("IssueDate", width=350, minwidth=50, anchor="center")
        self.tree.column("DueDate", width=350, minwidth=50, anchor="center")


        # heading
        self.tree.heading("BookID", text="Book ID")
        self.tree.heading("StudentID", text="Student ID")
        self.tree.heading("IssueDate", text="Issue Date")
        self.tree.heading("DueDate", text="Due Date", )


        i = 0

        for ro in cursor:
            if i % 2 == 0:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('even',))
            else:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('odd',))

            i = i + 1
        self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
        self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')

        self.tree.place(x=50,y=115)



        #tree2
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM `returnbook` WHERE `ReturnDate` LIKE '%" + d + "%'")
        except:
            cursor.set("Database error")

        self.tree1["columns"] = ("BookID", "StudentID", "IssueDate", "ReturnDate")
        self.tree1.column("BookID", width=280, minwidth=50, anchor="center")
        self.tree1.column("StudentID", width=280, minwidth=50, anchor="center")
        self.tree1.column("IssueDate", width=350, minwidth=50, anchor="center")
        self.tree1.column("ReturnDate", width=350, minwidth=50, anchor="center")

        # heading
        self.tree1.heading("BookID", text="Book ID")
        self.tree1.heading("StudentID", text="Student ID")
        self.tree1.heading("IssueDate", text="Issue Date")
        self.tree1.heading("ReturnDate", text="Return Date", )

        i = 0

        for ro in cursor:
            if i % 2 == 0:
                self.tree1.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('even',))
            else:
                self.tree1.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('odd',))

            i = i + 1
        self.tree1.tag_configure('even', background='#D0ECE7', foreground='black')
        self.tree1.tag_configure('odd', background='#F2F3F4', foreground='black')

        self.tree1.place(x=50,y=440)

    def searchBook(self):
        #issue book
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.tree1.get_children():
            self.tree1.delete(row)
        d = self.cal.get()
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM `issuebookstatics` WHERE `IssueDate` LIKE '%" + d + "%'")
        except:
            cursor.set("Database error")
        i = 0

        for ro in cursor:
            if i % 2 == 0:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('even',))
            else:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('odd',))

            i = i + 1
        self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
        self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')


        #return

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM `returnbook` WHERE `ReturnDate` LIKE '%" + d + "%'")
        except:
            cursor.set("Database error")
        i = 0

        for ro in cursor:
            if i % 2 == 0:
                self.tree1.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('even',))
            else:
                self.tree1.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]), tags=('odd',))

            i = i + 1
        self.tree1.tag_configure('even', background='#D0ECE7', foreground='black')
        self.tree1.tag_configure('odd', background='#F2F3F4', foreground='black')

