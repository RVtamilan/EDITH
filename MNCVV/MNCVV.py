import webbrowser
def book11():
    webbrowser.open("https://drive.google.com/drive/folders/1Ic9bsjF4n3Ilhu_CHpciNplfDZbOI3q9?usp=share_link")
def phy11():
    webbrowser.open("https://drive.google.com/drive/folders/1ixSvbhpYRW5kSr_BQP4RPudCwotIi1rV?usp=share_link")
def chem11():
    webbrowser.open("https://drive.google.com/drive/folders/1jl829_G2vcEncBUJQZgbid6YZ1ql4aVq?usp=share_link")
def bio11():
    webbrowser.open("https://drive.google.com/drive/folders/1dP9fVEHwqrCS08gRlpzD9oWobhDOlg27?usp=share_link")
def science10():
    webbrowser.open("https://drive.google.com/drive/folders/1Qt9wyoEvjmWxQZTBBtMUIV3Io03OEFxO?usp=share_link")
def eng10():
    webbrowser.open("https://drive.google.com/drive/folders/1er_CZAxogAbahHuIrLF-6yPdKdLuuzRv?usp=share_link")
def social10():
    webbrowser.open("https://drive.google.com/drive/folders/17zF_kgS1Af8ATjvZspTf9QMLs3RyVwgB?usp=share_link")
def phy12():
    webbrowser.open("https://drive.google.com/drive/folders/1paWUxeIPInJ55bGgdJi-A1DpUCleK9H6?usp=share_link")
def chem12():
    webbrowser.open("https://drive.google.com/drive/folders/1M9OoqP7jf-UMJ30Q963eiDertlKY0i4O?usp=share_link")
def bio12():
    webbrowser.open("https://drive.google.com/drive/folders/1iE_tDOOb5g1JXmTZbdYcnCKBkI0Lq-g-?usp=share_link")
from tkinter import*
rv =Tk()
rv.geometry('384x682')
rv.title("MNCVV PROTAL")
rv.resizable(False,False)

#CLASS 12 PCB
def PCB12():
    root6 = Toplevel()
    root6.title("12TH SUBJECT NOTES")
    root6.geometry("550x300")
    root6.config(bg="#F2E7D5")
    l10 =Label(root6,text="Get Your Notes Here",font=("Harlow Solid Italic",15),fg="black",bg="#F2E7D5")
    l10.pack(pady=20)
    bt10 =Button(root6,text="PHYSICS",command=phy12).place(relx=0.2,rely=0.5,anchor=CENTER)
    bt11 =Button(root6,text="CHEMISTRY",command=chem12).place(relx=0.5,rely=0.5,anchor=CENTER)
    bt12 =Button(root6,text="BIOLOGY",command=bio12).place(relx=0.8,rely=0.5,anchor=CENTER)

#CLASS 11 PCB
def PCB11():
    root5 = Toplevel()
    root5.title("11TH SUBJECT NOTES")
    root5.geometry("550x300")
    root5.config(bg="#6D9886")
    l10 =Label(root5,text="Get Your Notes Here",font=("Harlow Solid Italic",15),fg="black",bg="#6D9886")
    l10.pack(pady=20)
    bt10 =Button(root5,text="PHYSICS",command=phy11).place(relx=0.2,rely=0.5,anchor=CENTER)
    bt11 =Button(root5,text="CHEMISTRY",command=chem11).place(relx=0.5,rely=0.5,anchor=CENTER)
    bt12 =Button(root5,text="BIOLOGY",command=bio11).place(relx=0.8,rely=0.5,anchor=CENTER)

#class 10 PCB
def PCB10():
    root4 = Toplevel()
    root4.title("10TH SUBJECT NOTES")
    root4.geometry("550x300")
    root4.config(bg="#393E46")
    l10 =Label(root4,text="Get Your Notes Here",font=("Harlow Solid Italic",15),fg="black",bg="#393E46")
    l10.pack(pady=20)
    bt10 =Button(root4,text="SCIENCE",command=science10).place(relx=0.2,rely=0.5,anchor=CENTER)
    bt11 =Button(root4,text="SOCIAL SCIENCE",command=social10).place(relx=0.5,rely=0.5,anchor=CENTER)
    bt12 =Button(root4,text="ENGLISH",command=eng10).place(relx=0.8,rely=0.5,anchor=CENTER)

#class 10 portal 
def branch1():
    root1 = Toplevel()
    root1.title("CLASS 10 PORTAL")
    root1.geometry("550x300")
    root1.config(bg="#31E1F7")
    l4 = Label(root1,text="Mukkala Nammalwar Chetty Vivekananda Vidyalaya",font=("Harlow Solid Italic",15),fg="black",bg="#31E1F7")
    l4.pack(pady=20)
    bt4 = Button(root1,text="CLASS 10 BOOKS")
    bt4.place(relx=0.5,rely=0.4,anchor=CENTER)
    bt5 = Button(root1,text="CLASS 10 NOTES",command=PCB10)
    bt5.place(relx=0.5,rely=0.6,anchor=CENTER)
#class 11 portal
def branch2():

    root2 = Toplevel()
    root2.title("CLASS 11 PORTAL")
    root2.geometry("550x300")
    root2.config(bg="#37E2D5")
    l5 = Label(root2,text="Mukkala Nammalwar Chetty Vivekananda Vidyalaya",font=("Harlow Solid Italic",15),fg="black",bg="#37E2D5")
    l5.pack(pady=20)
    bt6 = Button(root2,text="CLASS 11 BOOKS",command=book11)
    bt6.place(relx=0.5,rely=0.4,anchor=CENTER)
    bt7 = Button(root2,text="CLASS 11 NOTES",command=PCB11)
    bt7.place(relx=0.5,rely=0.6,anchor=CENTER)
#class 12 portal
def branch3():
    root3 = Toplevel()
    root3.title("CLASS 12 PORTAL")
    root3.geometry("550x300")
    root3.config(bg="#7900FF")
    l6 = Label(root3,text="Mukkala Nammalwar Chetty Vivekananda Vidyalaya",font=("Harlow Solid Italic",15),fg="black",bg="#7900FF")
    l6.pack(pady=20)
    bt8 = Button(root3,text="CLASS 12 BOOKS")
    bt8.place(relx=0.5,rely=0.4,anchor=CENTER)
    bt9 = Button(root3,text="CLASS 12 NOTES",command=PCB12)
    bt9.place(relx=0.5,rely=0.6,anchor=CENTER) 
bg = PhotoImage(file="v2.png")
ig = Label(rv,image=bg)
ig.place(x=0,y=0,relwidth=1,relheight=1)
#click me image 
ig2 = PhotoImage(file="click1.png")
#class 10 lable and button
l1 =Label(rv,text="class 10:-",font=('Courier New',10,"bold"),fg= 'white',bg= '#3E80FD')
l1.place(x=25,y=300)
bt = Button(rv,image=ig2,borderwidth=0,command= branch1)
bt.place(x=100,y=330)
#class 11 lable and button
l2 = Label(rv,text="class 11:- ",font=("Courier New",10),fg="white",bg="#3E80FD").place(x=25,y=380)
bt2= Button(rv,image=ig2,borderwidth=0,command=branch2).place(x=100,y=410)
#class 12 lable and button
l3 =Label(rv,text="Class 12:-",font=('Courier New',10),fg="white",bg="#3E80FD").place(x=25,y=450)
bt3 = Button(rv,image=ig2,borderwidth=0,command=branch3).place(x=100,y=480)
#exir button of main window 
exit = Button(rv,text="EXIT",font=('Courier New',15),command=rv.destroy).place(x=150,y=600)
rv.mainloop()