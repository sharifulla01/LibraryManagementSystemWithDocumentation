import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *

from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import mysql.connector as mysql
from datetime import date
#IssueBook class
class IssueBook(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('750x650')
        self.title('Issue Book')
        self.resizable(width=0, height=0)
        #book id
        self.label = Label(self, text="Issue Book ",  # text
                           font=('Arial', 24, 'bold'),  # font ->
                           pady=20,  # padding
                           compound='top')  # add photo
        self.label.pack()  # position
        self.label1 = Label(self, text="Book ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=40, y=100)  # position
        self.BookId = Entry(self,
                           font=("Arial", 18), width=35

                           )
        self.BookId.place(x=170, y=120)


        # student id
        self.label4 = Label(self, text="Student ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label4.place(x=40, y=170)  # position
        self.studentId = Entry(self,
                              font=("Arial", 18), width=35

                              )
        self.studentId.place(x=170, y=190)

        self.label5 = Label(self, text="Issue Date:",  # text
                            font=('Arial', 17),  # font ->
                            pady=20,  # padding
                            compound='top')
        self.label5.place(x=40, y=225)


        # Adding combobox drop down list

        today = date.today()
        self.d1 = today.strftime("%d/%m/%Y")

        self.label8 = Label(self, text=self.d1,  # text
                            font=('Arial', 18),  # font ->
                            pady=20,  # padding
                            compound='top')
        self.label8.place(x=170, y=229)




        # Create a Calendar using DateEntry
        self.cal = DateEntry(self, width=16, background="magenta3", foreground="white", bd=2,font=('Arial', 16),date_pattern='dd/MM/yyyy')

        self.cal.place(x=150, y=305)

        self.label6 = Label(self, text="Due Date:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label6.place(x=40, y=285)  # position

        self.label9 = Label(self, text="Book Details",  # text
                            font=('Arial', 16,'bold','underline'),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label9.place(x=131, y=370)  # position

        self.label10 = Label(self, text="Student Details",  # text
                            font=('Arial', 16, 'bold', 'underline'),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label10.place(x=483, y=370)  # position



        #bookdetails table
        self.tree1 = ttk.Treeview(self, height="3")
        self.tree1['show'] = 'headings'

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview.Heading", font=(None, 12, 'bold'), background='#117A65', foreground='white')
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11), rowheight=30)

        # column
        self.tree1["columns"] = ("FullName", "Department")

        self.tree1.column("FullName", width=200, minwidth=50,)
        self.tree1.column("Department", width=150, minwidth=50,)


        # heading

        self.tree1.heading("FullName", text="Full Name")
        self.tree1.heading("Department", text="Department")

        self.tree1.place(x=380, y=435)






        #student Details table
        self.tree = ttk.Treeview(self, height="3")
        self.tree['show'] = 'headings'

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview.Heading", font=(None, 12, 'bold'), background='#117A65', foreground='white')
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11), rowheight=30)


        # column
        self.tree["columns"] =("BookName","Author")
        self.tree.column("BookName", width=200, minwidth=50)
        self.tree.column("Author", width=150, minwidth=50)



        # heading
        self.tree.heading("BookName", text="Book Name")
        self.tree.heading("Author", text="Author")




        self.tree.place(x=15, y=435)


        #buttons


        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.Booksearch).place(x=640, y=120)
        self.button = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.Booksearch1).place(x=640, y=190)

        self.button1 = Button(self, text=" Submit ", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B", width=8,command=self.Isubmit).place(x=140, y=585)

        self.button3 = Button(self, text=" Clear ", font=("Arial", 12, "bold"), fg="white", bg="#000080", width=8,
                              command=self.ex).place(x=320, y=585)
        self.button4 = Button(self, text=" Exit ", font=("Arial", 12, "bold"), fg="white", bg="#FA8072", width=8,
                              command=self.ex).place(x=500, y=585)

    def Booksearch1(self):

        stid = self.studentId.get()
        for row in self.tree1.get_children():
            self.tree1.delete(row)
        if (stid == ""):
            messagebox.showinfo("Insert Status", "please enter your id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `studentlist` WHERE `Student_ID` LIKE '%" + stid + "%'")
            except:
                cursor.set("Database error")

            i = 0

            for ro in cursor:
                if i % 2 == 0:
                    self.tree1.insert('', i, text="", values=(ro[1], ro[4]), tags=('even',))
                else:
                    self.tree1.insert('', i, text="", values=(ro[1], ro[4]), tags=('odd',))

                i = i + 1
            self.tree1.tag_configure('even', background='#D0ECE7', foreground='black')
            self.tree1.tag_configure('odd', background='#F2F3F4', foreground='black')


    def Isubmit(self):
        Bid = self.BookId.get()

        stuId = self.studentId.get()

        iDate = self.d1

        dDate = self.cal.get()


        if (Bid == "" or stuId == "" or iDate == "" or  dDate == "" ):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("insert into issuebook values('" + Bid + "','" + stuId + "','" + iDate + "','" +dDate + "')")
                cursor.execute("insert into issuebookstatics values('" + Bid + "','" + stuId + "','" + iDate + "','" + dDate + "')")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Added successfully");
                con.close();

            except:

                cursor.set("Database error")

            self.BookId.delete(0, END)
            self.studentId.delete(0, END)


        return

    def Booksearch(self):
        Bid=self.BookId.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        if(Bid==""):
            messagebox.showinfo("Insert Status", "please enter your id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `booklist` WHERE `Book_ID` LIKE '%" + Bid + "%'")
            except:
                cursor.set("Database error")

            i = 0

            for ro in cursor:
                if i % 2 == 0:
                    self.tree.insert('', i, text="", values=(ro[1], ro[2]), tags=('even',))
                else:
                    self.tree.insert('', i, text="", values=(ro[1], ro[2]), tags=('odd',))


                i = i + 1
            self.tree.tag_configure('even', background='#D0ECE7', foreground='black')
            self.tree.tag_configure('odd', background='#F2F3F4', foreground='black')



            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")

                cursor = con.cursor()
                cursor.execute("SELECT * FROM `issuebook` WHERE `BookID` LIKE '%" + Bid + "%'")
                results = cursor.fetchall()

                con.close();
                i = 0
                if results:

                    for i in results:
                        messagebox.showinfo("Issue Book", "Book is already issued.")


            except:
                cursor.set("Database error")




    def clear(self):
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.username.delete(0, END)
        self.phone.delete(0, END)
        self.password.delete(0, END)

    def ex(self):
        self.destroy()
