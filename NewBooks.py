import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *

from tkinter import messagebox
import mysql.connector as mysql

#newBook page class
class NewBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('700x620')
        self.title('New Book')
        self.resizable(width=0, height=0)


        self.label = Label(self, text="New Book Registration ",  # text
                           font=('Arial', 24, 'bold'),  # font ->
                           pady=20,  # padding
                           compound='top')  # add photo
        self.label.pack()  # position
        self.label1 = Label(self, text="Book ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=20, y=100)  # position
        self.bookid = Entry(self,
                           font=("Arial", 18), width=35

                           )
        self.bookid.place(x=150, y=120)

        self.label2 = Label(self, text="Title:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=20, y=170)  # position
        self.BookName = Entry(self,
                           font=("Arial", 18), width=35

                           )
        self.BookName.place(x=150, y=190)

        # phone
        self.label3 = Label(self, text="Author",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label3.place(x=20, y=240)  # position
        self.author = Entry(self,
                           font=("Arial", 18), width=35

                           )
        self.author.place(x=150, y=260)

        # username
        self.label4 = Label(self, text="Edition:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label4.place(x=20, y=310)  # position
        self.edition = Entry(self,
                              font=("Arial", 18), width=35

                              )
        self.edition.place(x=150, y=330)

        self.label5 = Label(self, text="Category:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')
        self.label5.place(x=20, y=370)
        # Adding combobox drop down list
        self.choosen = ("Civil Engineering", "English", "Computer Science", "Electrical Engineering", "Novel", "Mathematics", "Philosophy", "Business Administration", "Poetry", "Action And adventure", "History", "Comic Book", "Drama", "Graphic novel", "Mystery")
        self.selected_Cate = tk.StringVar()

        cb = ttk.Combobox(self, textvariable=self.selected_Cate, font=("Arial", 18), width=33)
        cb['values'] = self.choosen
        cb['state'] = 'readonly'  # normal
        cb.place(x=150, y=390)



        # radio button
        self.label6 = Label(self, text="Price:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label6.place(x=20, y=430)  # position
        self.price = Entry(self,
                              font=("Arial", 18), width=35

                              )
        self.price.place(x=150, y=450)

        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.Bsearch).place(x=620, y=120)
        self.button1 = Button(self, text=" Submit ", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B", width=8,
                              command=self.Bsubmit).place(x=90, y=535)
        self.button2 = Button(self, text=" Update ", font=("Arial", 12, "bold"), fg="white", bg="#2874A6", width=8,
                              command=self.Bupdate).place(x=230, y=535)
        self.button3 = Button(self, text=" Delete ", font=("Arial", 12, "bold"), fg="white", bg="#FA8072", width=8,
                              command=self.Bdelete).place(x=370, y=535)
        self.button4 = Button(self, text=" Clear ", font=("Arial", 12, "bold"), fg="white", bg="#9FE2BF", width=8,
                              command=self.Bclear).place(x=510, y=535)

    def Bsearch(self):
        self.BookName.delete(0, END)
        self.author.delete(0, END)
        self.edition.delete(0, END)
        self.selected_Cate.set("")
        self.price.delete(0, END)
        Bid = self.bookid.get()

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")

            cursor = con.cursor()
            cursor.execute("SELECT * FROM `booklist` WHERE `Book_ID` LIKE '%" + Bid + "%'")
            results = cursor.fetchall()

            con.close();
            i = 0
            if results:
                for i in results:
                    Bname = i[1]
                    Bauthor = i[2]
                    Bedition = i[3]
                    Bcategory = i[4]
                    Bprice = i[5]

                self.BookName.insert(0, Bname)
                self.author.insert(0,Bauthor)
                self.edition.insert(0, Bedition)
                self.selected_Cate.set(Bcategory)
                self.price.insert(0,Bprice )


            else:
                messagebox.showinfo("Incorrect", "Data is not found");

        except:
            cursor.set("Database error")

        return

    def Bclear(self):
        self.bookid.delete(0, END)
        self.BookName.delete(0, END)
        self.author.delete(0, END)
        self.edition.delete(0, END)
        self.selected_Cate.set("")
        self.price.delete(0,END)

    def Bdelete(self):
        Bid = self.bookid.get()
        if (Bid == ""):
            messagebox.showinfo("Insert Status", "Record is not found.")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("DELETE FROM booklist WHERE Book_ID='" + Bid + "'")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Deleted successfully");
                con.close();

            except:
                cursor.set("Database error")
        self.bookid.delete(0, END)
        self.BookName.delete(0, END)
        self.author.delete(0, END)
        self.edition.delete(0, END)
        self.selected_Cate.set("")
        self.price.delete(0, END)
        return

    def Bsubmit(self):

        Bid=self.bookid.get()
        Bname=self.BookName.get()
        Bauthor=self.author.get()
        Bedition=self.edition.get()
        Bcategory=self.selected_Cate.get()
        Bprice=self.price.get()


        if(Bid == "" or Bname == "" or Bauthor == "" or Bedition == "" or Bcategory == "" or Bprice == ""):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute(
                    "insert into booklist values('" + Bid + "','" + Bname + "','" + Bauthor + "','" + Bedition + "','" +Bcategory + "','" +Bprice + "')")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Added successfully");
                con.close();

            except:
                messagebox.showinfo("Status", "Book Is Already exits");
                cursor.set("Database error")

            self.bookid.delete(0, END)
            self.BookName.delete(0, END)
            self.author.delete(0, END)
            self.edition.delete(0, END)
            self.selected_Cate.set("")
            self.price.delete(0, END)

        return

    def Bupdate(self):
        Bid = self.bookid.get()
        Bname = self.BookName.get()
        Bauthor = self.author.get()
        Bedition = self.edition.get()
        Bcategory = self.selected_Cate.get()
        Bprice = self.price.get()

        if (Bid == "" or Bname == "" or Bauthor == "" or Bedition == "" or Bcategory == "" or Bprice == ""):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute( "UPDATE booklist SET Book_ID='" + Bid + "',Book_Name='" + Bname + "',Author='" + Bauthor + "',Edition='" + Bedition + "',Category='" +Bcategory+ "',Price='" + Bprice + "' WHERE Book_ID='" + Bid + "';")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Update successfully");
                con.close();

            except:
                cursor.set("Database error")

            self.bookid.delete(0, END)
            self.BookName.delete(0, END)
            self.author.delete(0, END)
            self.edition.delete(0, END)
            self.selected_Cate.set("")
            self.price.delete(0, END)

        return
