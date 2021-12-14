from tkinter import *
import tkinter
from tkinter.font import names


class game:
    def __init__(self) -> None:
        self.space = Tk()
        self.board = dict()
        self.remaining_space = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
        self.play_count=0
        self.CreateBoard()
        self._run()

    def CreateBoard(self):
        for a in range(1, 4):
            for b in range(1, 4):
                self.board[f"{a}{b}"] = Button(self.space, text="", width=10, height=2)
                self.board[f"{a}{b}"].grid(row=a, column=b)
                self.board[f"{a}{b}"].bind('<Return>', lambda : self._ButtonClicked)
        # #------------------------binding-enter------------------------------
        # self.board["11"].bind('<Return>', lambda : self._ButtonClicked("11"))
        # self.board["12"].bind('<Return>', lambda : self._ButtonClicked("12"))
        # self.board["13"].bind('<Return>', lambda : self._ButtonClicked("13"))
        # self.board["21"].bind('<Return>', lambda : self._ButtonClicked("21"))
        # self.board["22"].bind('<Return>', lambda : self._ButtonClicked("22"))
        # self.board["23"].bind('<Return>', lambda : self._ButtonClicked("23"))
        # self.board["31"].bind('<Return>', lambda : self._ButtonClicked("31"))
        # self.board["32"].bind('<Return>', lambda : self._ButtonClicked("32"))
        # self.board["33"].bind('<Return>', lambda : self._ButtonClicked("33"))
        # #-------------------adding-commands---------------------------
        self.board["11"]["command"] = lambda :self._ButtonClicked("11")
        self.board["12"]["command"] = lambda :self._ButtonClicked("12")
        self.board["13"]["command"] = lambda :self._ButtonClicked("13")
        self.board["21"]["command"] = lambda :self._ButtonClicked("21")
        self.board["22"]["command"] = lambda :self._ButtonClicked("22")
        self.board["23"]["command"] = lambda :self._ButtonClicked("23")
        self.board["31"]["command"] = lambda :self._ButtonClicked("31")
        self.board["32"]["command"] = lambda :self._ButtonClicked("32")
        self.board["33"]["command"] = lambda :self._ButtonClicked("33")
        #--------------------------------------------------------------
    def _ButtonClicked(self, name):
        # print(name)
        if name in self.remaining_space:
            self.board[name]=Label(self.space,text="clicked")
            self.chk()
            self.board[name].grid(row=int(name[0]), column=int(name[1]))
            self.remaining_space.remove(name)
        else:
            pass

    def _run(self):
        print(self.board)
        self.space.mainloop()
    def who_turns(self):
        pass
    def chk(self):
        pass

game()
