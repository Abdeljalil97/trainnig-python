from tkinter import*
def dessineCercle(i):
       x1, y1 = coord[i][0], coord[i][1]
       can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =coul[i])
def a1():
      dessineCercle(0)
def a2():
      dessineCercle(1)
def a3():
      dessineCercle(2)
def a4():
      dessineCercle(3)
def a5():
      dessineCercle(4)

coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
coul = ["red", "yellow", "blue", "green", "black"]
base=Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
bou=Button(base,text="quitter",command=base.quit)
bou.pack(side=RIGHT)
i=0
while i<5:
      x1,y1=coord[i][0],coord[i][1]
      can.create_oval(x1,y1,x1+100,y1+100,width=2,outline=coul[i])
      i=i+1
Button(base, text='1', command = a1).pack(side =LEFT)
Button(base, text='2', command = a2).pack(side =LEFT)
Button(base, text='3', command = a3).pack(side =LEFT)
Button(base, text='4', command = a4).pack(side =LEFT)
Button(base, text='5', command = a5).pack(side =LEFT)
base.mainloop()
      
