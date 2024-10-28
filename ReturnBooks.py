import tkinter as tk

from tkinter.ttk import Label
from tkinter import *

from tkinter import messagebox
import mysql.connector as mysql
from datetime import date

class ReturnBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('710x620')
        self.title('Return Book')
        self.resizable(width=0, height=0)

        self.label = Label(self, text="Return Book ",  # text
                           font=('Arial', 24, 'bold'),  # font ->
                           pady=20,  # padding
                           compound='top')  # add photo
        self.label.pack()  # position
        self.label1 = Label(self, text="Book ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=20, y=100)  # position
        self.BookID = Entry(self,
                           font=("Arial", 18), width=35

                           )
        self.BookID.place(x=150, y=120)

        self.label2 = Label(self, text="Student ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=20, y=170)  # position
        self.StudentID = Entry(self,
                           font=("Arial", 18), width=35

                           )
        self.StudentID.place(x=150, y=190)


        self.label5 = Label(self, text="Issue Date:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')
        self.label5.place(x=20, y=240)
        # Adding combobox drop down list
        self.issuedate = Entry(self,
                              font=("Arial", 18), width=35

                              )
        self.issuedate.place(x=150, y=260)




        self.label6 = Label(self, text="Return Date:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label6.place(x=20, y=310)   # position

        today = date.today()
        self.d1 = today.strftime("%d/%m/%Y")
        self.label8 = Label(self, text=self.d1,fg="#1B2631",  # text
                            font=('Arial', 18),  # padding
                            compound='top')
        self.label8.place(x=170, y=330)





        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.search).place(x=620, y=120)
        self.button1 = Button(self, text=" Submit ", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B", width=8,
                              command=self.submit).place(x=120, y=535)

        self.button3 = Button(self, text=" Clear ", font=("Arial", 12, "bold"), fg="white", bg="#000080", width=8,
                              command=self.ex).place(x=300, y=535)
        self.button4 = Button(self, text=" Exit ", font=("Arial", 12, "bold"), fg="white", bg="#FA8072", width=8,
                              command=self.ex).place(x=480, y=535)



    def search(self):

        Bid = self.BookID.get()

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")

            cursor = con.cursor()
            cursor.execute("SELECT * FROM `issuebook` WHERE `BookID` LIKE '%" + Bid + "%'")
            results = cursor.fetchall()

            con.close();
            i = 0
            if results:
                for i in results:
                    stid=i[1]
                    idate=i[2]
                self.StudentID.insert(0, stid)
                self.issuedate.insert(0,idate)


            else:
                messagebox.showinfo("Incorrect", "Data is not found");

        except:
            cursor.set("Database error")

        return

    def submit(self):
        Bid = self.BookID.get()

        stuId = self.StudentID.get()

        iDate = self.issuedate.get()

        rDate=self.d1


        if (Bid == "" or stuId == "" or iDate == "" or rDate == ""):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("insert into returnbook values('" + Bid + "','" + stuId + "','" + iDate + "','" + rDate + "')")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Added successfully");
                con.close();

            except:
                messagebox.showinfo("Status", "Book Is Already exits");
                cursor.set("Database error")

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("DELETE FROM issuebook WHERE BookID='" + Bid + "'")

                cursor.execute("commit");
                con.close();

            except:
                cursor.set("Database error")

            self.BookID.delete(0, END)
            self.StudentID.delete(0, END)
            self.issuedate.delete(0,END)


    def clear(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.username.delete(0, END)
        self.phone.delete(0, END)
        self.password.delete(0, END)

    def ex(self):
        self.destroy()

