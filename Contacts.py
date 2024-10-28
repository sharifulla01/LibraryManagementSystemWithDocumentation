import tkinter as tk
from tkinter import ttk, BOTH, YES
from tkinter.ttk import Label
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from Developers import developer
import smtplib
#Contact
class Contact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('1100x770')
        self.title('Contact')
        self.maxsize(1100,770)
        self.resizable(width=0, height=0)




        self.label = Label(self, text="Contact with students",  # text
                           font=('Arial', 24, 'bold','underline'),  # font ->
                           pady=50,  # padding
                           compound='top')  # add photo
        self.label.pack()  # position

        self.labelTeam = Label(self, text="Contact with developer",  # text
                           font=('Arial',18, 'bold'),bg="#008B8B",fg="white", # font ->
                           compound='top')  # add photo
        self.labelTeam.place(x=395,y=720)  # position

        self.labelTeam.bind("<Button>",self.Opendeveloper)#mouse event

        # search box create
        self.label1 = Label(self, text="Student ID:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label1.place(x=50, y=110)  # position
        self.studentid = Entry(self,
                               font=("Arial", 18), width=18

                               )

        self.studentid.place(x=165, y=130)

        self.label2 = Label(self, text="Department:",  # text
                            font=('Arial', 16),  # font ->
                            pady=20,  # padding
                            compound='top')  # add photo
        self.label2.place(x=530, y=110)  # position

        # Adding combobox drop down list
        self.choosen = ("CSE", "EEE", "BBA", "CIVIL", "NFE", "SWE", "Textile")
        self.selected_de = tk.StringVar()

        self.cb = ttk.Combobox(self, textvariable=self.selected_de, font=("Arial", 18), width=18)
        self.cb['values'] = self.choosen
        self.cb['state'] = 'readonly'  # normal
        self.cb.place(x=650, y=130)
        #student name
        self.label0 = Label(self, text="Name:",  # text
                            font=('Arial', 16),  # font ->

                            compound='top')  # add photo
        self.label0.place(x=110, y=250)  # position

        self.name = Entry(self,
                             font=("Arial", 18), width=30

                             )
        self.name.place(x=200, y=250)
        # search box create
        self.label3 = Label(self, text="Email:",  # text
                            font=('Arial', 16),  # font ->

                            compound='top')  # add photo
        self.label3.place(x=110, y=310)  # position
        self.emailId = Entry(self,
                            font=("Arial", 16), width=34

                            )
        self.emailId.place(x=200, y=310)


        #email subject

        self.label4 = Label(self, text="Subject:",  # text
                            font=('Arial', 16),  # font ->

                            compound='top')  # add photo
        self.label4.place(x=110, y=370)  # position
        self.sub = Entry(self,
                             font=("Arial",18), width=34

                             )
        self.sub.place(x=200, y=370)


        #body
        self.label5 = Label(self, text="Body:",  # text
                            font=('Arial', 16),  # font ->

                            compound='top')  # add photo
        self.label5.place(x=110, y=430)  # position

        #text area

        self.body = Text(self,font =("Courier", 14), height=12, width=70)

        self.body.place(x=200,y=430)

        self.button0 = Button(self, text="Search", font=("Arial", 12, "bold"), fg="white", bg="#2A6A3B",
                              command=self.Search).place(x=420, y=129)
        self.button4 = Button(self, text="   Send  ", font=("Arial", 12, "bold"), fg="white", bg="#4863A0",
                              command=self.sentIn).place(x=620, y=248)
        self.button1 = Button(self, text="  Send  ", font=("Arial", 12, "bold"), fg="white", bg="#4863A0",
                              command=self.SentDe).place(x=920, y=129)
        self.button2 = Button(self, text="Send All", font=("Arial", 12, "bold"), fg="white", bg="#008080",
                              command=self.sentAll).place(x=1000,y=129)
        self.button3 = Button(self, text=" Clear ", font=("Arial", 12, "bold"), fg="white", bg="#DE3163",
                              command=self.Clear).place(x=1000,y=430)





    def Search(self):
        self.name.config(state='normal')
        stid = self.studentid.get()

        if (stid == ""):
            messagebox.showinfo("Insert Status", "please enter student id!")
        else:

            try:
                con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
                cursor = con.cursor()
                cursor.execute("SELECT * FROM `studentlist` WHERE `student_Id` LIKE '%" + stid + "%'")

            except:
                cursor.set("Database error")

        i = 0
        for ro in cursor:
            em=ro[2]
            nm=ro[1]
            i = i + 1

        self.emailId.insert(0,em)
        self.name.insert(0,nm)


        self.studentid.delete(0, END)

    def sentIn(self):

        s=self.sub.get()

        b=self.body.get("1.0","end")

        e=self.emailId.get()



        try:
            # login into gmail
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("opp.project234@gmail.com", password="project.demo")
            msg = b
            subject = s
            body = "Subject: {}\nFrom:{}\n\n{} ".format(subject,"OOP-II Project<opp.project234@gmail.com>", msg)
            server.sendmail("opp.project234@gmail.com", e, body)
            server.quit()
            messagebox.showinfo("Mail Status", "Send mail successfully!")
        except:
            server.set("Server error")

        #end


    def SentDe(self):
        self.name.config(state='disabled')
        de=self.selected_de.get()

        msg1="Send mail all the " + de+ " department students"
        self.emailId.insert(0,msg1)
        msg = self.body.get("1.0", "end")
        subject = self.sub.get()
        body = "Subject: {}\nFrom:{}\n\n{} ".format(subject, "OOP-II Project<opp.project234@gmail.com>", msg)
        # login into gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("opp.project234@gmail.com", password="project.demo")
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM `studentlist` WHERE `department` LIKE '%" + de + "%'")
        except:
            cursor.set("Database error")

        for ro in cursor:
            server.sendmail("opp.project234@gmail.com", ro[2], body)
        server.quit()
        messagebox.showinfo("Mail Status", "Send mail successfully!")

        self.selected_de.set("")
        #----------------------------------------------------------------


    def sentAll(self):

        self.name.config(state='disabled')
        msg1 = "Send mail all the department students"
        self.emailId.insert(0, msg1)
        msg = self.body.get("1.0", "end")
        subject = self.sub.get()

        body = "Subject: {}\nFrom:{}\n\n{} ".format(subject, "OOP-II Project<opp.project234@gmail.com>", msg)

        # login into gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("opp.project234@gmail.com", password="project.demo")
        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="library-management-system")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM `studentlist`")
        except:
            cursor.set("Database error")

        for ro in cursor:
            server.sendmail("opp.project234@gmail.com", ro[2], body)
        server.quit()
        messagebox.showinfo("Mail Status", "Send mail successfully!")

        self.selected_de.set("")

    def Clear(self):
        self.body.delete("1.0","end")
        self.sub.delete(0,END)
        self.emailId.delete(0,END)
        self.sub.delete(0,END)
        self.name.delete(0,END)


    def Opendeveloper(self, event):

        window = developer(self)
        window.grab_set()





#end contact class---------------------------------------------------------------------
