from tkinter import *
from tkinter.font import *


class StudentRegistration(Tk):
    def __init__(self):
        super().__init__()

        self.title("Entry Test Registration form!")
        self.geometry("650x400")
        self.config(bg="black")

        font1 = Font(family="Poppins", size=19, weight="bold")
        font2 = Font(family="Poppins", size=19, weight="normal")
        font3= Font(family="Poppins", size=10)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        for i in range(0, 8):
            self.rowconfigure(i, weight=1)

        self.lblTitle = Label(self, text="Student Registration form!", font=font1, bg="black", fg="white")
        self.roll = Label(self, text="CNIC/ B-FORM:", anchor="e", font=font2, bg="black", fg="white")
        self.name = Label(self, text="Name: ", anchor="e", font=font2, bg="black", fg="white")
        self.gender = Label(self, text="Gender:", anchor="e", font=font2, bg="black", fg="white")
        self.email = Label(self, text="Email:", anchor="e", font=font2, bg="black", fg="white")
        self.Phone = Label(self, text="Phone:", anchor="e", font=font2, bg="black", fg="white")

        self.e_roll = Entry(self, font=font2)
        self.e_name = Entry(self,font=font2)
        self.e_email = Entry(self,font=font2)
        self.e_phone = Entry(self,font=font2)

        self.lblTitle.grid(row=0, column=1,sticky=W)
        self.roll.grid(row=1, column=1, sticky=W)
        self.name.grid(row=2, column=1, sticky=W)
        self.gender.grid(row=3, column=1, sticky=W)
        self.email.grid(row=5, column=1, sticky=W)
        self.Phone.grid(row=6, column=1, sticky=W)
        self.e_roll.grid(row=1, column=2, padx=30)
        self.e_name.grid(row=2, column=2)
        self.e_email.grid(row=5, column=2)
        self.e_phone.grid(row=6, column=2)

        self.male = Radiobutton(self, text="Male", value=1,font=font3, bg="black", fg="white")
        self.female = Radiobutton(self, text="Female", value=2, font=font3, bg="black", fg="white")
        self.male.grid(row=3, column=2)
        self.female.grid(row=4, column=2)

        submit = Button(self, text="submit", font=font2, bd=2)
        submit.grid(row=7, column=2)

    def run(self):
        window.mainloop()




window = StudentRegistration()
window.run()
