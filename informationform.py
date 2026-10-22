import tkinter as tk

from tkinter import ttk

from tkinter import messagebox

import openpyxl

import os


def entry_data():
    checkterms=termstatus.get()
    if checkterms=="Accepted":
        firstname=firstnameentry.get()
        lastname=lastnameentry.get()
        title=titlecombobox.get()
        age=agespinbox.get()
        nationnality=nationentry.get()
        degree=educombobox.get()
        grade=gradespin.get()
        year=yearspin.get()
        if firstname and lastname and title and nationnality and degree:
            print(f"First Name: {firstname} | Last Name: {lastname} | Title: {title}")
            print(f"Age: {age} | Nationality: {nationnality} ")
            print(f"Degree: {degree} | Grade: {grade} | Passing Year: {year}")


            filepath="D:\Python\Project\data.xlsx"

            if not os.path.exists(filepath):
                workbook=openpyxl.Workbook()
                sheet=workbook.active
                heading=["First Name","Last Name","Title","Age","Nationality","Degree","Grade","Passing Year"]
                sheet.append(heading)
                workbook.save(filepath)

            workbook=openpyxl.load_workbook(filepath)
            sheet=workbook.active
            data=[firstname,lastname,title,age,nationnality,degree,grade,year]
            sheet.append(data)
            workbook.save(filepath)


        else:
            messagebox.showerror(title="Error",message="Some Information is missing!")
    else:
        messagebox.showwarning(title="Warning",message="Accept the terms and Condition to enter the data")






window=tk.Tk()
window.title("Data Entry Form")

frame=tk.Frame(window)
frame.pack()

#user information 
userinfo_frame=tk.LabelFrame(frame,text="User Information")
userinfo_frame.grid(row=0,column=0,padx=20,pady=20)

#first name collect
firstnamelabel=tk.Label(userinfo_frame,text="First Name")
firstnamelabel.grid(row=0,column=0)
firstnameentry=tk.Entry(userinfo_frame)
firstnameentry.grid(row=1,column=0)


#last name collect
lastnamelabel=tk.Label(userinfo_frame,text="Last Name")
lastnamelabel.grid(row=0,column=1)
lastnameentry=tk.Entry(userinfo_frame)
lastnameentry.grid(row=1,column=1)

#title
titlelabel=tk.Label(userinfo_frame,text="Title")
titlelabel.grid(row=0,column=2)
titlecombobox=ttk.Combobox(userinfo_frame,values=["Mr","Mrs"])
titlecombobox.grid(row=1,column=2)


#age
agelabel=tk.Label(userinfo_frame,text="Age")
agelabel.grid(row=2,column=0)
agespinbox=tk.Spinbox(userinfo_frame,from_=18, to=100,state="readonly")
agespinbox.grid(row=3,column=0)


#Nationality
nationlabel=tk.Label(userinfo_frame,text="Nationality")
nationlabel.grid(row=2,column=1)
nationentry=tk.Entry(userinfo_frame)
nationentry.grid(row=3,column=1)


for widgets in userinfo_frame.winfo_children():
    widgets.grid_configure(padx=10,pady=5)

#education information
eduinfo_frame=tk.LabelFrame(frame,text="Education")
eduinfo_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)


#degee collect
edulabel=tk.Label(eduinfo_frame,text="Degree Name")
edulabel.grid(row=0,column=0)
educombobox=ttk.Combobox(eduinfo_frame,values=["HSC","SSC","JSC"])
educombobox.grid(row=1,column=0)


#grade collect
gradelabel=tk.Label(eduinfo_frame,text="Grade")
gradelabel.grid(row=0,column=1)
gradespin=tk.Spinbox(eduinfo_frame,values=["A+","A","A-","B","C","D"],state="readonly")
gradespin.grid(row=1,column=1)


#passyeara
yearlabel=tk.Label(eduinfo_frame,text="Passing Year")
yearlabel.grid(row=0,column=2)
yearspin=tk.Spinbox(eduinfo_frame,from_="2000",to="2026",state="readonly")
yearspin.grid(row=1,column=2)

for widgets in eduinfo_frame.winfo_children():
    widgets.grid_configure(padx=10,pady=5)


#terms and condition
terms_frame=tk.LabelFrame(frame,text="Terms and Condition")
terms_frame.grid(row=3,column=0,padx=20,pady=20,sticky="news")

#termscheckbox
termstatus=tk.StringVar(value="Not Accepted")
termscheckbox=tk.Checkbutton(terms_frame,text="I accept the terms and conditions",variable=termstatus,onvalue="Accepted",offvalue="Not Accepted")
termscheckbox.grid(row=1,column=0)


#enterbutton
enterdata=tk.Button(frame,text="Enter Data",command=entry_data)
enterdata.grid(row=4,column=0,padx=20,pady=20,sticky="news")


window.mainloop()