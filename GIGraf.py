

from  math import *
from tkinter import *

class  Rmaxplus :       
    def __init__ ( self ,   x ) :
        self .x=x   
    def __pow__( self , x ) :
        return  Rmaxplus ( self . x*x )
    def __mul__( self , other ) :
        if  isinstance ( other ,  Rmaxplus ) :
            return  Rmaxplus ( self . x+other . x )
        return  Rmaxplus ( self . x+other )
    def __rmul__( self ,    other ) :
        return  self . __mul__( other )
    def __add__( self , other ) :
        if  isinstance ( other ,  Rmaxplus ) :
             return  Rmaxplus (max( self . x ,  other . x ) )
        return  Rmaxplus (max( self . x ,  other ) )
    def __radd__( self ,    other ) :
        return  self . __add__( other )

def    drawAll ( xmin , xmax , f ) :

        h=500
        w=1000

        canv=Canvas(root,	width=w,	height=h,	bg="white")

        canv.grid(row=2,column=0,columnspan=4)

        canv.create_line(w/2,h,w/2,0,width=2,arrow=LAST)

        canv.create_line(0,h/2,w,h/2,width=2,arrow=LAST)

        xold=xmin

        yold=0

        for	i in range(w):

            if	(i%(float(w)/20)==0):

                k = xmin + i/5

                canv.create_line(5*k+w/2, 3+h/2, 5*k+w/2, 3+h/2, width = 0.5, fill= 'black' )
                canv.create_text(5*k + w/2+15, -10+h/2, text=str(k), fill="purple",	font=("Helvectica","10"))

                if	(k!=0):

                    canv.create_line(3+w/2,5*k+h/2,3+w/2,5*k+h/2,width=0.5,fill='black')

                    canv.create_text(20+w/2,5*k+h/2,text=str(-k),fill="purple",font=("Helvectica","10"))

            try:
                x=Rmaxplus(xmin+i/5)

                y= -5*eval(f).x+h/2

                x= 5*x.x+w/2

                canv.create_line(xold,yold,x,y,width=1,fill='black')


                yold=y

                xold=x

            except:

                pass


def drawSR(e):
    drawAll(-100,100,funk.get())
root=Tk()
root.title("Grafs constructor")
var = 1
funk=Entry(root,width=100)
label = Label(text=u'Enter equation!')
label.grid()

funk.grid(row=0,column=3,columnspan=4)

btn=Button(root,text=" Draw ", width=10,height=3)
btn.grid(row=4, column=7)           
btn.bind('<1>', drawSR)
R1=Radiobutton(root,    text="(R,   max,    +)",variable=var,
value=1)                        
R1.grid(row=1,  column=3)
# label1 = Label(text="ymax = 50", fg="#eee", bg="#333")
# label1.grid(row=3,  column=1)
lxmin=Label(root,   text="x min")       
lxmin.grid(row=3,column=0)          
Xmin=Entry(root,    width=10)       
Xmin.grid(row=4,column=0)           
lxmax=Label(root,   text="x max")       
lxmax.grid(row=3,column=2)          
Xmax=Entry(root,    width=10)       
Xmax.grid(row=4,column=2)           
lymin=Label(root,   text="y min")       
lymin.grid(row=3,   column=3)
Ymin=Entry(root,    width=10)
Ymin.grid(row=4,    column=3)
lymax=Label(root,   text="ymax")
lymax.grid(row=3,   column=4)
Ymax=Entry(root,    width=10)
Ymax.grid(row=4,    column=4)
Ymax.insert(0, "50")
Ymin.insert(0, "-50")
Xmax.insert(0, "100")
Xmin.insert(0, "-100")
root.mainloop()
 