from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title('abc')
#root.iconbitmap()
root.geometry("800x600")

#w=600
#h=400
#x=w/2
#y=h/2
#my_canvas=Canvas(root,width=w,heigh=h,bg="white")
my_canvas=Canvas(root,width=800,height=600,bg="white")
my_canvas.pack(fill="both",expand=True)

#add image to canvas

image_file = filedialog.askopenfilename(title="select your image", filetypes= [("image files",".png"),("image files",'.jpg')])
img = ImageTk.PhotoImage(Image.open(image_file))

my_image=my_canvas.create_image(0,0,anchor=NW,image=img)

def move(e):
    #e.x
    #e.y
    global img,image_file
    img = ImageTk.PhotoImage(Image.open(image_file))
    my_canvas.delete()
    my_image=my_canvas.create_image(e.x,e.y,image=img)

    my_label.config(text="Coordonates: x "+str(e.x)+ " y "+str(e.y))


def resizer(ev):
    global img1,resized,new_img
    #e.width
    #e.height
    global img,image_file
    #open our image
    img1 = Image.open(image_file)
    #resize the image
    resized=img1.resize((ev.width,ev.height),Image.ANTIALIAS)
    #define our image
    new_img=ImageTk.PhotoImage(resized)
    #add it back to the canvas
    my_canvas.create_image(260,125,anchor=NW,image=new_img)


my_label=Label(root,text="")
my_label.pack(pady=20)

my_canvas.bind('<B1-Motion>',move)
my_canvas.bind('<Configure>',resizer)

root.mainloop()