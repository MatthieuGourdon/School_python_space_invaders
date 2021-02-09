# -*- coding: utf-8 -*-
"""

"""
import random as rd
import tkinter as Tk
Largeur = 750
Longueur = 550



w = Tk.Tk("SpaceInvaders")
c = Tk.Canvas(w, width=Largeur,height=Longueur)
def joker():
    pass
def deplacement():
    global dx,dy,DicoSpriteEnnemis,ListeTire,DicoEnnemis,ListeDeplacemntBas,vaisseau,LabelScore,ListeTireEnnemis1,ListeTireEnnemis2,ListeTireEnnemis3,hp,p

    dd=0

    rd1=rd.randint(0,100)
    rd2=rd.randint(0,100)
    rd3=rd.randint(0,100)
    
    if c.coords(balle12)[2]>550 or c.coords(balle11)[0]<20:
        dx=0
        if ListeDeplacemntBas==[]:
            ListeDeplacemntBas.append(c.coords(balle12)[1]+20)
        if c.coords(balle12)[1]<ListeDeplacemntBas[0]:
            dd=2
        else:
            if c.coords(balle12)[2]>550:
                dx=-2
            elif c.coords(balle11)[0]<20:
                dx=2
            ListeDeplacemntBas=[]
            dd=0

    for i in DicoEnnemis:
        if len(ListeTire)!=0:
            if c.coords(DicoEnnemis[i])[1]<(c.coords(ListeTire[0])[1]+5) and c.coords(DicoEnnemis[i])[3]>(c.coords(ListeTire[0])[1]+5):
                if c.coords(DicoEnnemis[i])[0]<(c.coords(ListeTire[0])[0]+5) and c.coords(DicoEnnemis[i])[2]>(c.coords(ListeTire[0])[0]+5):
                    c.delete(ListeTire[0])
                    ListeTire=[]
                    c.delete(DicoEnnemis[i])
                    c.delete(DicoSpriteEnnemis[i])
                    del DicoEnnemis[i]
                    break

    for i in DicoEnnemis:
        c.move(DicoEnnemis[i],dx,dd)
        c.move(DicoSpriteEnnemis[i],dx,dd)
    c.move(balle11,dx,dd)
    c.move(balle12,dx,dd)

    if len(ListeTire)>0:
        c.move(ListeTire[0],0,-dy*5)
        if c.coords(ListeTire[0])[1]<0:
            c.delete(ListeTire[0])
            ListeTire=[]

    for i in DicoEnnemis:
        if c.coords(DicoEnnemis[i])[3]>=500:
            dx=0
            dd=0
            c.delete(vaisseau)
            w.unbind('<Left>')
            w.unbind('<Right>')
            w.unbind('<space>')
            LabelGO=Tk.Label(w, text='Game Over =(')
            LabelGO_w=c.create_window(670,250,window=LabelGO)

    if rd1==19 and p!=-1:       
        if (ListeTireEnnemis1==[]) and ('balle3' in DicoEnnemis):
            bullet1=c.create_oval(c.coords(balle3)[0]+10,c.coords(balle3)[1]+10,c.coords(balle3)[2]-10,c.coords(balle3)[3]-10,fill="green")
            ListeTireEnnemis1.append(bullet1)

    if ListeTireEnnemis1!=[]:
        c.move(ListeTireEnnemis1[0],0,2)
        if c.coords(ListeTireEnnemis1[0])[3]>550:
            c.delete(ListeTireEnnemis1[0])
            ListeTireEnnemis1=[]
        elif c.coords(vaisseau)[1]<c.coords(ListeTireEnnemis1[0])[1]+5 and c.coords(vaisseau)[3]>c.coords(ListeTireEnnemis1[0])[1]+5:
                if c.coords(vaisseau)[0]<c.coords(ListeTireEnnemis1[0])[0]+5 and c.coords(vaisseau)[2]>c.coords(ListeTireEnnemis1[0])[0]+5:
                    hp-=1
                    c.delete(ListeTireEnnemis1[0])
                    ListeTireEnnemis1=[]

    if rd2==19 and p!=-1:       
        if (ListeTireEnnemis2==[]) and ('rect1' in DicoEnnemis):
            bullet2=c.create_oval(c.coords(rect1)[0]+10,c.coords(rect1)[1]+10,c.coords(rect1)[2]-10,c.coords(rect1)[3]-10,fill="green")
            ListeTireEnnemis2.append(bullet2)

    if ListeTireEnnemis2!=[]:
        c.move(ListeTireEnnemis2[0],0,2)
        if c.coords(ListeTireEnnemis2[0])[3]>550:
            c.delete(ListeTireEnnemis2[0])
            ListeTireEnnemis2=[]
        elif c.coords(vaisseau)[1]<c.coords(ListeTireEnnemis2[0])[1]+5 and c.coords(vaisseau)[3]>c.coords(ListeTireEnnemis2[0])[1]+5:
                if c.coords(vaisseau)[0]<c.coords(ListeTireEnnemis2[0])[0]+5 and c.coords(vaisseau)[2]>c.coords(ListeTireEnnemis2[0])[0]+5:
                    hp-=1
                    c.delete(ListeTireEnnemis2[0])
                    ListeTireEnnemis2=[]

    if rd3==19 and p!=-1:       
        if (ListeTireEnnemis3==[]) and ('balle10' in DicoEnnemis):
            bullet3=c.create_oval(c.coords(balle10)[0]+10,c.coords(balle10)[1]+10,c.coords(balle10)[2]-10,c.coords(balle10)[3]-10,fill="green")
            ListeTireEnnemis3.append(bullet3)

    if ListeTireEnnemis3!=[]:
        c.move(ListeTireEnnemis3[0],0,2)
        if c.coords(ListeTireEnnemis3[0])[3]>550:
            c.delete(ListeTireEnnemis3[0])
            ListeTireEnnemis3=[]
        elif c.coords(vaisseau)[1]<c.coords(ListeTireEnnemis3[0])[1]+5 and c.coords(vaisseau)[3]>c.coords(ListeTireEnnemis3[0])[1]+5:
                if c.coords(vaisseau)[0]<c.coords(ListeTireEnnemis3[0])[0]+5 and c.coords(vaisseau)[2]>c.coords(ListeTireEnnemis3[0])[0]+5:
                    hp-=1
                    c.delete(ListeTireEnnemis3[0])
                    ListeTireEnnemis3=[]

    if hp==0:
        dx=0
        dd=0
        if ListeTireEnnemis3!=[]:
            c.delete(ListeTireEnnemis3[0])
            ListeTireEnnemis3=[]
        if ListeTireEnnemis2!=[]:
            c.delete(ListeTireEnnemis2[0])
            ListeTireEnnemis2=[]
        if ListeTireEnnemis1!=[]:
            c.delete(ListeTireEnnemis1[0])
            ListeTireEnnemis1=[]
        c.delete(vaisseau)
        w.unbind('<Left>')
        w.unbind('<Right>')
        w.unbind('<space>')
        LabelGO=Tk.Label(w, text='Game Over =(')
        LabelGO_w=c.create_window(670,250,window=LabelGO)

    sv1=Tk.StringVar()
    sv1.set('score : '+str(10*(15-len(DicoEnnemis))))
    LabelScore=Tk.Label(w, textvariable=sv1)
    LabelScore_w=c.create_window(25,10,window=LabelScore)

    sv2=Tk.StringVar()
    sv2.set('Vie(s) restante(s) : '+str(hp))
    Hp=Tk.Label(w, textvariable=sv2)
    Hp_w=c.create_window(570,10,window=Hp)
                
        
        
    w.after(20,deplacement)

def droite(evt):        
    if c.coords(vaisseau)[0]<525:   
        c.move(vaisseau,25,0)    
        c.move(Vaisseaufinal,25,0)
def gauche(evt):    
    if c.coords(vaisseau)[2]>50:    
        c.move(vaisseau,-25,0)
        c.move(Vaisseaufinal,-25,0)
def tir(evt):
    global ListeTire
    if len(ListeTire)<1:
        bullet = c.create_oval(c.coords(vaisseau)[0]+20,470,c.coords(vaisseau)[2]-20,480, fill="red",width=4)
        ListeTire.append(bullet)


dx=2
dy=2
hp=3
p=1
imgfond = Tk.PhotoImage(file="./pictures/Fond_Si.gif")
a = c.create_image(290, 30,anchor=Tk.N, image=imgfond)

buttonQuit = Tk.Button(c,text="Quitter",command=w.destroy)
buttonQuit_w = c.create_window(670, 350, window=buttonQuit)

buttonNG = Tk.Button(c,text="New Game", command=joker())
buttonNG_w = c.create_window(670,150,window=buttonNG)
imShooter=Tk.PhotoImage(file="./pictures/Roberto2.gif")
imMiguel=Tk.PhotoImage(file="./pictures/Miguel2.gif")
balle1 = c.create_oval(70,60,100,90,fill="DarkOrchid1",width=4)
ennemi1=c.create_image(85,55,anchor=Tk.N,image=imMiguel)
balle2 = c.create_oval(170,60,200,90,fill="DarkOrchid2",width=4)
ennemi2=c.create_image(185,55,anchor=Tk.N,image=imMiguel)
balle3 = c.create_oval(270,60,300,90,fill="DarkOrchid3",width=4)
ennemitir1=c.create_image(285,55,anchor=Tk.N, image =imShooter)
balle4 = c.create_oval(370,60,400,90,fill="DarkOrchid4",width=4)
ennemi3=c.create_image(385,55,anchor=Tk.N,image=imMiguel)
balle5 = c.create_oval(470,60,500,90,fill="purple4",width=4)
ennemi4=c.create_image(485,55,anchor=Tk.N,image=imMiguel)

rect1 = c.create_rectangle(70,120,100,150,fill="medium spring green",width=4)
ennemitir2=c.create_image(85,115,anchor=Tk.N, image =imShooter)
rect2 = c.create_rectangle(170,120,200,150,fill="SeaGreen1",width=4)
ennemi5=c.create_image(185,115,anchor=Tk.N,image=imMiguel)
rect3 = c.create_rectangle(270,120,300,150,fill="SeaGreen2",width=4)
ennemi6=c.create_image(285,115,anchor=Tk.N,image=imMiguel)
rect4 = c.create_rectangle(370,120,400,150,fill="SeaGreen3",width=4)
ennemi7=c.create_image(385,115,anchor=Tk.N,image=imMiguel)
rect5 = c.create_rectangle(470,120,500,150,fill="dark green",width=4)
ennemi8=c.create_image(485,115,anchor=Tk.N,image=imMiguel)

balle6 = c.create_oval(70,180,100,210,fill="cyan",width=4)
ennemi9=c.create_image(85,175,anchor=Tk.N,image=imMiguel)
balle7 = c.create_oval(170,180,200,210,fill="turquoise",width=4)
ennemi10=c.create_image(185,175,anchor=Tk.N,image=imMiguel)
balle8 = c.create_oval(270,180,300,210,fill="medium turquoise",width=4)
ennemi11=c.create_image(285,175,anchor=Tk.N,image=imMiguel)
balle9 = c.create_oval(370,180,400,210,fill="dark turquoise",width=4)
ennemi12=c.create_image(385,175,anchor=Tk.N,image=imMiguel)
balle10 = c.create_oval(470,180,500,210,fill="DeepSkyBlue2",width=4)
ennemitir3=c.create_image(485,175,anchor=Tk.N, image =imShooter)

balle11 = c.create_oval(70,900,100,930,width=4)
balle12 = c.create_oval(470,900,500,930,width=4)
Bouclier1=c.create_rectangle(50,420,170,470,fill="Grey",width=8)
Bouclier2=c.create_rectangle(230,420,350,470,fill="Grey",width=8)
Bouclier3=c.create_rectangle(410,420,530,470,fill="Grey",width=8)
vaisseau = c.create_rectangle(260,520,290,530,fill="dark green",width=4)
imVaiss=Tk.PhotoImage(file="./pictures/FujiPolice3.gif")
Vaisseaufinal=c.create_image(275,500,anchor=Tk.N, image=imVaiss)

ListeTire=[]
ListeTireEnnemis1=[]
ListeTireEnnemis2=[]
ListeTireEnnemis3=[]
DicoEnnemis={'balle1':balle1,'balle2':balle2,'balle3':balle3,'balle4':balle4,'balle5':balle5,'rect1':rect1,'rect2':rect2,'rect3':rect3,'rect4':rect4,'rect5':rect5,'balle6':balle6,'balle7':balle7,'balle8':balle8,'balle9':balle9,'balle10':balle10}
DicoSpriteEnnemis={'balle1':ennemi1, 'balle2':ennemi2,'balle3':ennemitir1,'balle4':ennemi3, 'balle5':ennemi4,'rect1':ennemitir2,'rect2':ennemi5,'rect3':ennemi6,'rect4':ennemi7,'rect5':ennemi8,'balle6':ennemi9,'balle7':ennemi10,'balle8':ennemi11,'balle9':ennemi12,'balle10':ennemitir3}
ListeDeplacemntBas=[]

w.bind('<Left>', gauche)
w.bind('<Right>', droite)
w.bind('<space>',tir)


    

deplacement()
c.pack()
w.mainloop()

b=550