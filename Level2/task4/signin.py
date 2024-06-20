from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
from signup import SignUp
import credentials as cr

class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Log In PySeek")
        # Set the window size
        # Here 0,0 represents the starting point of the window 
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="white")

        #============================================================================
        #==============================DESIGN PART===================================
        #============================================================================

        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=0, y=0, width=450, relheight=1)

        label1 = Label(self.frame1, text="Py", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=100, y=300)
        label2 = Label(self.frame1, text="Seek", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=162, y=300)
        label3 = Label(self.frame1, text="It's all about Python", font=("times new roman", 13, "bold"), bg="yellow", fg="brown4").place(x=100, y=360)

        #=============Entry Field & Buttons============

        self.frame2 = Frame(self.window, bg="gray95")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=450)

        self.email_label = Label(self.frame3, text="Email Address", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50, y=40)
        self.email_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3, text="Password", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50, y=120)
        self.password_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show="*")
        self.password_entry.place(x=50, y=160, width=300)

        #================Buttons===================
        self.login_button = Button(self.frame3, text="Log In", command=self.login_func, font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="blue", fg="white").place(x=50, y=220, width=300)
        self.register_button = Button(self.frame3, text="Create New Account", command=self.create_account, font=("times new roman", 15), bd=0, cursor="hand2", bg="white", fg="blue").place(x=50, y=300, width=300)

    def login_func(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "":
            messagebox.show_error("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()

                cur.execute("select * from student_register where email=%s and password=%s",
                            (self.email_entry.get(), self.password_entry.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.window)

                else:
                    messagebox.showinfo("Success!", "Welcome", parent=self.window)
                    self.window.destroy()
                    os.system("python dashboard.py")

            except Exception as es:
                messagebox.showerror("Error!", f"Error due to {es}", parent=self.window)

    def create_account(self):
        self.window.destroy()
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()
