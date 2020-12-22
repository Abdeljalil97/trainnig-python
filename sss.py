from tkinter import *
from random import randrange
def drawline():
      global x1 ,y1, x2, y2, coul
      can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
      y2, y1 = y2+10, y1-10
      
def changecolor():
      global coul
      pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
      c=randrange(8)
      coul=pal[c]
      
x1=10
y1=190
x2=190
y2=10

coul='dark green'
fen=Tk()
can1=Canvas(fen,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1=Button(fen,text='Quitter',command=fen.destroy)
bou1.pack(side=BOTTOM)
bou2=Button(fen,text='tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen,text='Autre couleur',command=changecolor)
bou3.pack()
fen.mainloop()

fen.destroy()
