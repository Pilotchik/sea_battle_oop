__author__ = 'Александр'

from tkinter import *

class Application(Frame):
    '''
    Приложение. Наследует класс Frame. Создание окна, холста и всех функций для реализации приложения
    '''
    width = 800
    height = 400
    bg = "white"

    #добавление холста на окно
    def createCanvas(self):
        self.canv = Canvas(self)
        self.canv["height"] = self.height
        self.canv["width"] = self.width
        self.canv["bg"] = self.bg
        self.canv.pack()
        #клик по холсту вызывает функцию play
        self.canv.bind("<Button-1>",self.play)

    def new_game(self):
        print("New_game")

    def play(self,e):
        print("Play",e.x)

    def __init__(self, master=None):
        #инициализация окна
        Frame.__init__(self, master)
        self.pack()

        #инициализация меню
        self.m = Menu(master)
        master.config(menu = self.m)
        self.m_play = Menu(self.m)
        self.m.add_cascade(label = "Игра",menu = self.m_play)
        self.m_play.add_command(label="Новая игра", command = self.new_game)
        #вызов функции создания холста
        self.createCanvas()