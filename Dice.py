from tkinter import *
import random as rdm
from PIL import Image, ImageTk


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn1 = Button(root, text="1", font=("Times New Roman", 15),
                     command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="2", font=("Times New Roman", 15),
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="3", font=("Times New Roman", 15),
                      command=lambda x=3: self.btn_click(x))
        btn4 = Button(root, text="4", font=("Times New Roman", 15),
                     command=lambda x=4: self.btn_click(x))
        btn5 = Button(root, text="5", font=("Times New Roman", 15),
                      command=lambda x=5: self.btn_click(x))
        btn6 = Button(root, text="6", font=("Times New Roman", 15),
                     command=lambda x=6: self.btn_click(x))
        btn7 = Button(root, text="7", font=("Times New Roman", 15),
                      command=lambda x=7: self.btn_click(x))
        btn8 = Button(root, text="8", font=("Times New Roman", 15),
                      command=lambda x=8: self.btn_click(x))
        btn9 = Button(root, text="9", font=("Times New Roman", 15),
                      command=lambda x=9: self.btn_click(x))
        btn10 = Button(root, text="10", font=("Times New Roman", 15),
                      command=lambda x=10: self.btn_click(x))
        btn11 = Button(root, text="11", font=("Times New Roman", 15),
                       command=lambda x=11: self.btn_click(x))
        btn12 = Button(root, text="12", font=("Times New Roman", 15),
                      command=lambda x=12: self.btn_click(x))
        btn13 = Button(root, text="13", font=("Times New Roman", 15),
                       command=lambda x=13: self.btn_click(x))
        btn14 = Button(root, text="14", font=("Times New Roman", 15),
                       command=lambda x=14: self.btn_click(x))
        btn15 = Button(root, text="15", font=("Times New Roman", 15),
                       command=lambda x=15: self.btn_click(x))
        btn16 = Button(root, text="16", font=("Times New Roman", 15),
                       command=lambda x=16: self.btn_click(x))
        btn17 = Button(root, text="17", font=("Times New Roman", 15),
                       command=lambda x=17: self.btn_click(x))
        btn18 = Button(root, text="18", font=("Times New Roman", 15),
                       command=lambda x=18: self.btn_click(x))
        btn19 = Button(root, text="19", font=("Times New Roman", 15),
                       command=lambda x=19: self.btn_click(x))
        btn20 = Button(root, text="20", font=("Times New Roman", 15),
                       command=lambda x=20: self.btn_click(x))

        btn1.place(x=10, y=100, width=30, height=30)
        btn2.place(x=100, y=100, width=30, height=30)
        btn3.place(x=190, y=100, width=30, height=30)
        btn4.place(x=280, y=100, width=30, height=30)
        btn5.place(x=370, y=100, width=30, height=30)

        btn6.place(x=70, y=160, width=90, height=60)
        btn7.place(x=190, y=175, width=30, height=30)
        btn8.place(x=250, y=160, width=90, height=60)

        btn9.place(x=100, y=250, width=30, height=30)
        btn10.place(x=190, y=250, width=30, height=30)
        btn11.place(x=280, y=250, width=30, height=30)

        btn12.place(x=70, y=310, width=90, height=60)
        btn13.place(x=190, y=325, width=30, height=30)
        btn14.place(x=250, y=310, width=90, height=60)

        btn15.place(x=100, y=400, width=30, height=30)
        btn16.place(x=190, y=400, width=30, height=30)
        btn17.place(x=280, y=400, width=30, height=30)

        btn18.place(x=70, y=460, width=90, height=60)
        btn19.place(x=190, y=475, width=30, height=30)
        btn20.place(x=250, y=460, width=90, height=60)



        self.lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                         text=f"Побед: {self.win}\nПроигрышей:"
                              f" {self.lose}\nНичей: {self.drow}",
                         bg="#FFF")
        self.lbl2.place(x=5, y=5)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа")
        else:
            self.lose += 1
            self.lbl.configure(text="Проигрыш")

        self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"
                              f" {self.lose}\nНичей: {self.drow}")

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("1368x700+0+0")
    root.title("Double Dice")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()