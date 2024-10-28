import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
from PIL import Image, ImageTk
from NewStudents import NewStudent
from NewBooks import NewBook
from StudentDetails import StudentDetail
from Statics_ import Statics
from IssueBooks import IssueBook
from ReturnBooks import ReturnBook
from SearchBooks import SearchBook
from Contacts import Contact

#HomePage
class Home(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('1300x760')
        self.title('Home')
        self.resizable(width=0, height=0)


        icon = tk.PhotoImage(file='Photo/icon.png')

        self.iconphoto(True, icon)

        # set maximum window size value
        self.maxsize(1300,760)
        # setbackground
        self.image = Image.open("Photo/back.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        #heading
        self.label0 = Label(self, text="Library Management System", font=("Algerian", 30), bg='#708090', fg="orange").place(x=350, y=60)
        #new student
        self.image1 = Image.open("Photo/student.png")
        self.img_copy1 = self.image1.copy()
        self.background_image1 = ImageTk.PhotoImage(self.image1)
        self.background1 = Label(self, image=self.background_image1)
        self.background1.place(x=150,y=180)
        self.background1.bind("<Button>",self.OpenStudent)
        self.label1 = Label(self, text="New Student",font=("Arial",14),bg= '#708090',fg="white").place(x=150,y=310)

        #new book
        self.image2 = Image.open("Photo/book.png")
        self.img_copy2 = self.image2.copy()
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=450, y=180)
        self.background2.bind("<Button>", self.OpenBook)
        self.label2 = Label(self, text="New Book", font=("Arial", 14), bg='#708090',fg="white").place(x=460, y=310)
        # Student Details
        self.image3 = Image.open("Photo/stu.png")
        self.img_copy3 = self.image3.copy()
        self.background_image3 = ImageTk.PhotoImage(self.image3)
        self.background3 = Label(self, image=self.background_image3)
        self.background3.place(x=730, y=180)
        self.background3.bind("<Button>", self.OpenDetails)
        self.label3 = Label(self, text="Student Details", font=("Arial", 14), bg='#708090',fg="white").place(x=720, y=310)

        # Statics
        self.image4 = Image.open("Photo/static.png")
        self.img_copy4 = self.image4.copy()
        self.background_image4 = ImageTk.PhotoImage(self.image4)
        self.background4 = Label(self, image=self.background_image4)
        self.background4.place(x=1000, y=180)
        self.background4.bind("<Button>", self.OpenStatics)
        self.label4 = Label(self, text="Statics", font=("Arial", 14), bg='#708090', fg="white").place(x=1025,y=310)
        # issueBook
        self.image5 = Image.open("Photo/issue.png")
        self.img_copy5 = self.image5.copy()
        self.background_image5 = ImageTk.PhotoImage(self.image5)
        self.background5 = Label(self, image=self.background_image5)
        self.background5.place(x=150, y=500)
        self.background5.bind("<Button>", self.OpenIssue)
        self.label5 = Label(self, text="Issue Book", font=("Arial", 14), bg='#708090', fg="white").place(x=157,y=632)

        # RetuenBook
        self.image6 = Image.open("Photo/re.png")
        self.img_copy6 = self.image6.copy()
        self.background_image6 = ImageTk.PhotoImage(self.image6)
        self.background6 = Label(self, image=self.background_image6)
        self.background6.place(x=450, y=500)
        self.background6.bind("<Button>", self.OpenReturn)
        self.label6 = Label(self, text="Return Book", font=("Arial", 14), bg='#708090', fg="white").place(x=450, y=632)
        # SearchBook
        self.image7 = Image.open("Photo/search.png")
        self.img_copy7 = self.image7.copy()
        self.background_image7 = ImageTk.PhotoImage(self.image7)
        self.background7 = Label(self, image=self.background_image7)
        self.background7.place(x=730, y=500)
        self.background7.bind("<Button>", self.OpenSearch)
        self.label7 = Label(self, text="Search Book", font=("Arial", 14), bg='#708090', fg="white").place(x=730, y=632)
        # contact
        self.image8 = Image.open("Photo/contact.png")
        self.img_copy8 = self.image8.copy()
        self.background_image8 = ImageTk.PhotoImage(self.image8)
        self.background8 = Label(self, image=self.background_image8)
        self.background8.place(x=1000, y=500)
        self.background8.bind("<Button>", self.OpenContract)
        self.label8 = Label(self, text="Contact", font=("Arial", 14), bg='#708090', fg="white").place(x=1024, y=632)

    def OpenStudent(self, event):

        window = NewStudent(self)
        window.grab_set()
    def OpenBook(self, event):

        window = NewBook(self)
        window.grab_set()
    def OpenDetails(self, event):

        window = StudentDetail(self)
        window.grab_set()
    def OpenStatics(self, event):

        window = Statics(self)
        window.grab_set()
    def OpenIssue(self, event):

        window = IssueBook(self)
        window.grab_set()
    def OpenReturn(self, event):

        window = ReturnBook(self)
        window.grab_set()
    def OpenSearch(self, event):

        window = SearchBook(self)
        window.grab_set()
    def OpenContract(self, event):

        window = Contact(self)
        window.grab_set()





