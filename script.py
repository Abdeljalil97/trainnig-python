from tkinter import *
app=Tk()
champ_label=Label(app,text="salut SIMO")
champ_label.pack()
var_texte=StringVar()
ligne_texte=Entry(app,textvariable=var_texte,width=25)
ligne_texte.pack()
bouton_quitter=Button(app,text="Quitter",command=app.quit)
bouton_quitter.pack()
app.mainloop()

