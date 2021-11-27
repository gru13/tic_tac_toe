from tern import *

b = [" ", " ", " ",
     " ", " ", " ",
     " ", " ", " ", ]
h=0
win=Tk()
gui.creat_win(win,tle="TIC-TAC-TOE",winsize="300x100",bgcol="grey")
abel=Label(text=" start the game")
abel.grid(column=15, row=15)
def chck_win(l):
    global abel
    if( b[0] == b[1] == b[2] == l) or( b[3] == b[4] == b[5] == l)or(b[6] == b[7] == b[8] == l) or(b[0] == b[3] == b[6] == l) or(b[1] == b[4] == b[7] == l)or(b[2] == b[5] == b[8] == l) or(b[0] == b[4] == b[8]==l):
        abel.config(text=f"this match won by {l} \n The start with 'X' ")

def c0 ():
    global h
    if h%2==0:
        b.pop(0)
        b.insert(0,"X")
        b0["text"]="X"
        chck_win("X")
        abel.config(text="The next game is 'O'")
    else:
        b.insert(0,"O")
        b0["text"]="O"
        chck_win("O")
    h += 1
def c1():
    global h
    if h%2==0:
        b.pop(1)
        b.insert(1,"X")
        b1["text"]="X"
        chck_win("X")
    else:
        b.insert(1,"O")
        b1["text"]="O"
        chck_win("O")
    h += 1
def c2 ():
    global h
    if h%2==0:
        b.pop(0)
        b.insert(2,"X")
        b2["text"]="X"
        chck_win("X")
    else:
        b.insert(2,"O")
        b2["text"]="O"
        chck_win("O")
    h += 1
def c3 ():
    global h
    if h%2==0:
        b.pop(3)
        b.insert(3,"X")
        b3["text"]="X"
        chck_win("X")

    else:
        b.insert(3,"O")
        b3["text"]="O"
        chck_win("O")
    h += 1
def c4 ():
    global h
    if h%2==0:
        b.pop(4)
        b.insert(4,"X")
        b4["text"]="X"
        chck_win("X")
    else:
        b.insert(4,"O")
        b4["text"]="O"
        chck_win("O")
    h += 1
def c5 ():
    global h
    if h%2==0:
        b.pop(5)
        b.insert(5,"X")
        b5["text"]="X"
        chck_win("X")
    else:
        b.insert(5,"O")
        b5["text"]="O"
        chck_win("O")
    h += 1
def c6 ():
    global h
    if h%2==0:
        b.pop(6)
        b.insert(6,"X")
        b6["text"]="X"
        chck_win("X")
    else:
        b.insert(6,"O")
        b6["text"]="O"
        chck_win("O")
    h += 1
def c7 ():
    global h
    if h%2==0:
        b.pop(7)
        b.insert(7,"X")
        b7["text"]="X"
        chck_win("X")
    else:
        b.insert(7,"O")
        b7["text"]="O"
        chck_win("O")
    h += 1
def c8 ():
    global h
    if h%2==0:
        b.pop(8)
        b.insert(8,"X")
        b8["text"]="X"
        chck_win("X")
    else:
        b.insert(8,"O")
        b8["text"]="O"
        chck_win("O")
    h += 1


b0=Button(text=b[0],width=5,command=c0)
b0.grid(column=0, row=0)

b1=Button(text=b[1],width=5,command=c1)
b1.grid(column=6, row=0)

b2=Button(text=b[2],width=5,command=c2)
b2.grid(column=11, row=0)

b3=Button(text=b[3],width=5,command=c3)
b3.grid(column=0, row=1)

b4=Button(text=b[4],width=5,command=c4)
b4.grid(column=6, row=1)

b5=Button(text=b[5],width=5,command=c5)
b5.grid(column=11, row=1)

b6=Button(text=b[6],width=5,command=c6)
b6.grid(column=0, row=2)

b7=Button(text=b[7],width=5,command=c7)
b7.grid(column=6, row=2)

b8=Button(text=b[8],width=5,command=c8)
b8.grid(column=11, row=2)

le=len(b)

win.mainloop()