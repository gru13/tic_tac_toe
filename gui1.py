from tkinter import *
import tkinter

class game:
    def __init__(self) -> None:
        self.space = Tk()
        self.board = dict()
        self.CreateBoard()
        self._run()
    def CreateBoard(self):
        for a in range (1,4):
            for b in range(1,4):
                self.board[f"{a}{b}"] = [Button(self.space, text=f"{a}{b}", width=10, height=2,command=lambda:self._ButtonClicked()),f"{a}{b}"]
                self.board[f"{a}{b}"][0].grid(row=a,column=b)  
         

    def _run(self):
        # print(self.board)
        self.space.mainloop()
    def _ButtonClicked(self,name=None):
        print(name)
game()