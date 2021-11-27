def main ():

    b=[" "," ", " ",
       " "," ", " ",
       " ", " ", " ", ]
    l=[1,2,3,4,5,6,7,8,9]
    t=''
    def board_display():
        print("  |   |  ")
        print( b[0],"|" ,b[1],"|", b[2] )
        print("----------")
        print( b[3],"|" ,b[4],"|", b[5] )
        print("----------")
        print( b[6],"|" ,b[7],"|",  b[8]  )
        print("  |   |  ")

    def chck_win(l):
        if  b[0]==b[1]==b[2]==l:
            print(f"{b[0]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif b[3]==b[4]==b[5]==l:
            print(f"{b[3]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif b[6]==b[7]==b[8]==l:
            print(f"{b[6]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif b[0] == b[3] == b[6]==l:
            print(f"{b[3]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif  b[1]==b[4]==b[7]==l:
            print(f"{b[7]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif  b[2]==b[5]==b[8]==l:
            print(f"{b[8]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif  b[0]==b[4]==b[8]:
            print(f"{b[0]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        elif b[2] == b[4] == b[6]==l:
            print(f"{b[6]} is wins this round")
            t=input("do u want play again(y/n)")
            if t=="y":
                main()
        if len(l)==0:
            print("the match is draw")
            t = input("do u want play again(y/n)")
            if t == "y":
                main()
    def move_x():
        if len(l) == 0:
            print("the match is draw")
            t = input("do u want play again(y/n)")
            if t == "y":
                main()
        print(f"this your turn X")
        print(f"which place do you want to move (available places {l})")
        place=int(input())

        if place in l :
            l.pop(l.index(place))
            place -= 1
            b.pop(place)
            b.insert(place,"X")
            board_display()
        else:
            print("already occupide")
            move_x()
    def move_O():
        if len(l) == 0:
            print("the match is draw")
            t = input("do u want play again(y/n)")
            if t == "y":
                main()


        print(f"this your turn O")
        print(f"which place do you want to move (available places {l})")
        place=int(input())
        if place in l :
            l.pop(l.index(place))
            place -= 1
            b.pop(place)
            b.insert(place,"O")
            board_display()
        else:
            print("already occupide")
            move_O()
    h=0
    le=len(l)
    board_display()
    while le!=0:
        if h %2==0:
            move_x()
            chck_win("X")
            h+=1
        else:
            move_O()
            chck_win("O")
            h+=1
main()