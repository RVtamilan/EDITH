from tkinter import*
from cv2 import *
from sketchpy import*
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
root = Tk()
root.title("IMAGE DEDECTION GUI")
root.geometry("700x450")
root.resizable(False,False)

def file():
    global imge
    imglink = askopenfilename(initialdir="D:/",title="CHOOSE THE FILE",filetypes=(("png",'*.png'),("jpg","*.jpg"),("allfile","*.*")))
    imge = imglink
def cc():
    import cv2
    global imge
    image = cv2.imread(imge)
    grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert,(21,21),0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img,invertedblur,scale=260)
    name = "SKETCH"
    cv2.imshow(name,sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def imgtosketch():

    root1 = Toplevel()
    root1.title("IMAGE TO SKETCH")
    root1.geometry("550x300")
    iob = Image.open("bird.png")
    ib = ImageTk.PhotoImage(iob)
    bg = Label(root1,image=ib)
    bg.image = ib
    bg.place(x=0,y=0,relheight=1,relwidth=1)
    bt =Button(root1,text="CHOOSE A FILE",font=("arial black",10),command=file)
    bt.place(relx=0.65,rely=0.25,anchor=CENTER)
    bt1 = Button(root1,text="PROCESS IT",font=("arial black",10),command=cc)
    bt1.place(relx=0.5,rely=0.7,anchor=CENTER)
def draw():
    from sketchpy import canvas
    import cv2
    global imge
    image = cv2.imread(imge)
    grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('image.png',grey_img)
    img = canvas.sketch_from_image('image.png')
    img.draw()

def img2draw():
    root2 = Toplevel()
    root2.title("IMAGE TO DRAWING")
    root2.geometry("550x300")
    root.resizable(False,False)
    iob = Image.open("tiger.png")
    ib = ImageTk.PhotoImage(iob)
    bg = Label(root2,image=ib)
    bg.image = ib
    bg.place(x=0,y=0,relheight=1,relwidth=1)
    bt =Button(root2,text="CHOOSE A FILE",font=("arial black",10),command=file)
    bt.place(relx=0.45,rely=0.7,anchor=CENTER)
    bt1 = Button(root2,text="PROCESS IT",font=("arial black",10),command= draw)
    bt1.place(relx=0.45,rely=0.9,anchor=CENTER)

def facededect():
     import cv2
     global imge
     imgcascade = cv2.CascadeClassifier("face.xml")
     image = cv2.imread(imge)
     grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     face = imgcascade.detectMultiScale(grey_img,scaleFactor =1.05,minNeighbors = 5)
     for x,y,w,h in face:
        img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
     rs = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
     name = "SKETCH"
     cv2.imshow(name,rs)
     cv2.waitKey(0)
     cv2.destroyAllWindows()


def dedector():
    root3 = Toplevel()
    root3.title("IMAGE TO SKETCH")
    root3.geometry("550x300")
    iob = Image.open("get.png")
    ib = ImageTk.PhotoImage(iob)
    bg = Label(root3,image=ib)
    bg.image = ib
    bg.place(x=0,y=0,relheight=1,relwidth=1)
    bt =Button(root3,text="CHOOSE A FILE",font=("arial black",10),command=file)
    bt.place(relx=0.4,rely=0.3,anchor=CENTER)
    bt1 = Button(root3,text="PROCESS IT",font=("arial black",10),command= facededect)
    bt1.place(relx=0.4,rely=0.7,anchor=CENTER)


im = PhotoImage(file="nature.png")
bg = Label(root,image=im).place(x=0,y=0,relheight=1,relwidth=1)
lable1 = Label(root,text="WELCOME YOU FOR THE RV TECH FACTORY",font=("arial black",15))
lable1.pack(padx=20)
im2 = PhotoImage(file="bt1.png")
bt1 =Button(root,image=im2,borderwidth=0,command= imgtosketch).place(relx=0.15,rely=0.6,anchor=CENTER)
bt2 = Button(root,image=im2,borderwidth=0,command= img2draw).place(relx=0.5,rely=0.6,anchor=CENTER)
bt3 = Button(root,image=im2,borderwidth=0,command=dedector).place(relx=0.85,rely=0.6,anchor=CENTER)
l1 = Label(root,text= "PENCILE SKETCH",font=("arial black",10)).place(relx=0.15,rely=0.68,anchor=CENTER)
l2 = Label(root,text="LIVE PENCILE SHADE",font=("arial black",10)).place(relx=0.5,rely=0.68,anchor=CENTER)
l3 = Label(root,text="FACE DETECTION",font=("arial blak",10)).place(relx=0.85,rely=0.68,anchor=CENTER)

root.mainloop()