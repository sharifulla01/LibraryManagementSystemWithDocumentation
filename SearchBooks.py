import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
# Search Book class
class SearchBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('1366x760')
        self.title('Book Details')
        self.resizable(width=0, height=0)

        # search box create
        self.label1 = Label(self, text="Book ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=50, y=10)  # position
        self.bookid = Entry(self,
                            font=("Arial", 18), width=26

                            )

        self.bookid.place(x=140, y=30)

        self.label2 = Label(self, text="Category:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=630, y=10)  # position

        # Adding combobox drop down list
        self.choosen = (
        "Civil Engineering", "English", "Computer Science", "Electrical Engineering", "Novel", "Mathematics",
        "Philosophy", "Business Administration", "Poetry", "Action And adventure", "History", "Comic Book", "Drama",
        "Graphic novel", "Mystery")
        self.selected_Cate = tk.StringVar()

        self.cb = ttk.Combobox(self, textvariable=self.selected_Cate, font=("Arial", 18), width=26)
        self.cb['values'] = self.choosen
        self.cb['state'] = 'readonly'  # normal
        self.cb.place(x=730, y=30)

        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.searchBook1).place(x=496, y=29)
        self.button1 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.searchBook2).place(x=1100, y=29)
        self.button2 = Button(self, text="Refresh", font=("Arial", 12, "bold"), fg="white", bg="#6495ED",
                              command=self.refresh).place(x=1230,
                                                          y=29)

        # add

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM booklist")
        except:
            cursor.set("Database error")

        self.tree = ttk.Treeview(self,height="19")
        self.tree['show'] = 'headings'

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview.Heading", font=(None, 16, 'bold'), background='#117A65', foreground='white')
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 16), rowheight=30)
        self.tree.tag_configure('gr', background='green')

        # column
        self.tree["columns"] = ("BookID", "BookName", "Author","Edition","Category", "Price")
        self.tree.column("BookID", width=150, minwidth=50, anchor="center")
        self.tree.column("BookName", width=350, minwidth=50)
        self.tree.column("Author", width=250, minwidth=50)
        self.tree.column("Edition", width=170, minwidth=50, anchor="center")
        self.tree.column("Category", width=170, minwidth=50, anchor="center")
        self.tree.column("Price", width=170, minwidth=50, anchor="center")

        # heading
        self.tree.heading("BookID", text="Book ID")
        self.tree.heading("BookName", text="Book Name")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Edition", text="Edition", )
        self.tree.heading("Category", text="Category")
        self.tree.heading("Price", text="Price")

        i = 0

        for ro in cursor:
            if i % 2 == 0:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('even',))
            else:
                self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]), tags=('odd',))

            i = i + 1
        self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
        self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')
        self.tree.place(x=50,y=100)

    def searchBook1(self):
        bid = self.bookid.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        if (bid == ""):
            messagebox.showinfo("Insert Status", "please enter Book id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `booklist` WHERE `Book_ID` LIKE '%" + bid + "%'")
            except:
                cursor.set("Database error")

            i = 0

            for ro in cursor:
                if i % 2 == 0:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]),
                                         tags=('even',))
                else:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]),
                                         tags=('odd',))

                i = i + 1
                self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
                self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')

                self.bookid.delete(0, END)

    def searchBook2(self):
        c = self.selected_Cate.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        if (c == ""):
            messagebox.showinfo("Insert Status", "please enter Book id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `booklist` WHERE `Category` LIKE '%" + c + "%'")
            except:
                cursor.set("Database error")

            i = 0

            for ro in cursor:
                if i % 2 == 0:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]),
                                         tags=('even',))
                else:
                    self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]),
                                         tags=('odd',))

                i = i + 1
            self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
            self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')

            self.selected_Cate.set("")

    def refresh(self):

        for row in self.tree.get_children():
            self.tree.delete(row)
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM booklist")
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



