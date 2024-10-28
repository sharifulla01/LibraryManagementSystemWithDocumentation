import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import mysql.connector as mysql
from datetime import date



#start new students page class---------------------------------------------------------

class NewStudent(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)


        self.geometry('700x620')
        self.title('New Student')
        self.resizable(width=0, height=0)


        self.label = Label(self, text="New Student Registration ",  # text
                           font=('Arial', 24, 'bold'),  # font ->
                           pady=20,  # padding
                           compound='top')  # add photo
        self.label.pack()  # position

        #id
        self.label1 = Label(self, text="Student ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=20, y=100)  # position
        self.id = Entry(self,
                           font=("Arial", 18),width=35

                           )
        self.id.place(x=150, y=120)

        self.label2 = Label(self, text="Name:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=20, y=170)  # position
        self.name = Entry(self,
                           font=("Arial", 18),width=35

                           )
        self.name.place(x=150, y=190)

        # email
        self.label3 = Label(self, text="Email:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label3.place(x=20, y=240)  # position
        self.email = Entry(self,
                           font=("Arial", 18),width=35

                           )
        self.email.place(x=150, y=260)

        # mobile
        self.label4 = Label(self, text="Mobile:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label4.place(x=20, y=310)  # position
        self.mobile = Entry(self,
                              font=("Arial", 18),width=35

                              )
        self.mobile.place(x=150, y=330)

        #department
        self.label5 = Label(self, text="Department :",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')
        self.label5.place(x=20, y=370)
        # Adding combobox drop down list
        self.choosen= ("CSE", "EEE", "BBA", "CIVIL", "NFE", "SWE", "Textile")
        self.selected_de = tk.StringVar()

        self.cb = ttk.Combobox(self, textvariable=self.selected_de,font=("Arial", 18), width=33)
        self.cb['values'] =self.choosen
        self.cb['state'] = 'readonly'  # normal
        self.cb.place(x=150,y=390)


        #radio button
        self.x = StringVar()

        self.label6 = Label(self, text="Gender:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')
        self.label6.place(x=20, y=430)
        self.radioButton = Radiobutton(self,
                                  text="Male",
                                  font=('Arial', 16),
                                  variable=self.x,
                                  value="male"
                                  )
        self.radioButton.place(x=150,y=450)
        self.radioButton2 = Radiobutton(self,
                                   text="Female",
                                   font=('Arial', 16),
                                   variable=self.x,
                                   value="female"
                                   )
        self.radioButton2.place(x=300,y=450)
        self.radioButton3 = Radiobutton(self,
                                   text="Others",
                                   font=('Arial', 16),
                                   variable=self.x,
                                   value="others"
                                   )
        self.radioButton3.place(x=450, y=450)
        self.x.set("male")

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

        self.name.delete(0, END)
        self.email.delete(0, END)
        self.mobile.delete(0, END)
        self.selected_de.set("")
        self.x.set("male")
        stid = self.id.get()

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")

            cursor = con.cursor()
            cursor.execute("SELECT * FROM `studentlist` WHERE `Student_ID` LIKE '%" + stid + "%'")
            results = cursor.fetchall()

            con.close();
            i = 0
            if results:
                for i in results:
                    sname=i[1]
                    semail=i[2]
                    smobile=i[3]
                    sde=i[4]
                    sge=i[5]


                self.name.insert(0, sname)
                self.email.insert(0,semail)
                self.mobile.insert(0, smobile)
                self.selected_de.set(sde)
                self.x.set(sge)




            else:
                messagebox.showinfo("Status", "Data is not found!");

        except:
            cursor.set("Database error")

        return

    def Bclear(self):
        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.mobile.delete(0, END)
        self.selected_de.set("")
        self.x.set("male")


    def Bdelete(self):
        stid = self.id.get()
        if(stid==""):
            messagebox.showinfo("Insert Status", "Record is not found.")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("DELETE FROM studentlist WHERE Student_ID='" + stid + "'")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Deleted successfully");
                con.close();

            except:
                cursor.set("Database error")
        self.id.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.mobile.delete(0, END)
        self.selected_de.set("")
        self.x.set("male")
        return

    def Bsubmit(self):
        stid=self.id.get()
        stname = self.name.get()
        stemail = self.email.get()
        stmobile = self.mobile.get()
        stde = self.selected_de.get()
        stgender=self.x.get()

        if (stid =="" or stname == "" or stemail == "" or stmobile == "" or stde == "" or stgender==""):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("insert into studentlist values('" + stid + "','" + stname + "','" + stemail + "','" + stmobile + "','" + stde + "','" + stgender + "')")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "added successfully");
                con.close();

            except:
                messagebox.showinfo("Status", "You are already registered");
                cursor.set("Database error")

            self.id.delete(0, END)
            self.name.delete(0, END)
            self.email.delete(0, END)
            self.mobile.delete(0, END)
            self.selected_de.set("")
            self.x.set("male")


        return




    def Bupdate(self):
        stid = self.id.get()
        stname = self.name.get()
        stemail = self.email.get()
        stmobile = self.mobile.get()
        stde = self.selected_de.get()
        stgender = self.x.get()

        if (stid == "" or stname == "" or stemail == "" or stmobile == "" or stde == "" or stgender == ""):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("UPDATE studentlist SET student_id='" + stid + "',name='" + stname + "',email='" + stemail + "',mobile='" + stmobile + "',department='" + stde + "',gender='" + stgender + "' WHERE Student_ID='" + stid + "';")
                cursor.execute("commit");
                messagebox.showinfo("Insert Status", "Update successfully");
                con.close();

            except:
                cursor.set("Database error")

        return


#end new student page class---------------------------------------------------------