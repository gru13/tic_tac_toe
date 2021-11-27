"""
this is created by guru
"""
from tkinter import *
from time import*
import os

def zero(a):#change to zero
    a=0*a
    a=0
    return a
def chng (c,v):
    c.config(text=v)

def into(a,dype=None): #change the type
    a=dype(a)
    return a
def toa (a,j):
    a=j
def change(a,to=None): #change the val
   
    if type(a)== str:
        print("cant manipulate")
    else :
        w=type(a)
        a=w(to)
        return a
        
def chk_type(j):
    if type(j)==int :
        return int(j)
    elif type(j)==float :
        return float(j)

def uq (l): # this make the unique list
    l=set(l)
    l=list(l)
    return l
def x():
    exit()

'''def spk(t):
    o = gTTS(text=t, lang='en', slow=False)
    o.save("o.mp3")
    os.system('start o.mp3')'''
class gui ():
    def creat_win(win,tle=None, bgcol=None, winsize=None): #create a ready gui screen
        win.geometry(winsize)
        win.config(bg=bgcol)
        win.title(tle)
    def display (win,c,r,todis=None):#create
        global lbl
        lbl = Label(win, text=todis,bg="blue")
        lbl.grid(column=c, row=r)

    def bton (win,cl,r,btn=None,btcol=None,fcol="black",c=None):
        b=Button(win,text=btn,bg=btcol,fg=fcol,width=10,command=c).grid(column=cl, row=r)

    def chk_bton(win,c,r,btn=None):
        ckbt=Checkbutton(win,text=btn).grid(column=c,row=r)




