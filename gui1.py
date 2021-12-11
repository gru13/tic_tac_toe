from tkinter import *
import tkinter


class game:
    def __init__(self) -> None:
        self.space = Tk()
        self.board = dict()
        self.CreateBoard()
        self._run()

    def CreateBoard(self):
        for a in range(1, 4):
            for b in range(1, 4):
                self.board[f"{a}{b}"] = Button(self.space, text=f"{a}{b}", width=10, height=2)
                self.board[f"{a}{b}"].grid(row=a, column=b)
        self.board["11"]["command"] = lambda :self._ButtonClicked("11")
        self.board["12"]["command"] = lambda :self._ButtonClicked("12")
        self.board["13"]["command"] = lambda :self._ButtonClicked("13")
        self.board["21"]["command"] = lambda :self._ButtonClicked("21")
        self.board["22"]["command"] = lambda :self._ButtonClicked("22")
        self.board["23"]["command"] = lambda :self._ButtonClicked("23")
        self.board["31"]["command"] = lambda :self._ButtonClicked("31")
        self.board["32"]["command"] = lambda :self._ButtonClicked("32")
        self.board["33"]["command"] = lambda :self._ButtonClicked("33")

    def _run(self):
        print(self.board)
        self.space.mainloop()

    def _ButtonClicked(self, name):
        # print(name)
        self.board[name]=Label(self.space,text="clicked")
        self.board[name].grid(row=int(name[0]), column=int(name[1]))
        

game()
