__author__ = 'Александр'

from tkinter import *
from Ship import *

class Application(Frame):
    '''
    Приложение. Наследует класс Frame. Создание окна, холста и всех функций для реализации приложения
    '''
    #ширина рабочего поля
    width = 800
    #высота рабочего поля
    height = 400
    #цвет фона холста
    bg = "white"
    #отступ между ячейками
    indent = 2
    #размер одной из сторон квадратной ячейки
    gauge = 32
    #смещение по y (отступ сверху)
    offset_y = 40
    #смещение по x пользовательского поля
    offset_x_user = 30
    #смещение по x поля компьютера
    offset_x_comp = 430

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
        self.canv.delete('all')
        #добавление игровых полей пользователя и компьютера
        #создание поля для пользователя
        #перебор строк
        for i in range(10):
            #перебор столбцов
            for j in range(10):
                xn = j*self.gauge + (j+1)*self.indent + self.offset_x_user
                xk = xn + self.gauge
                yn = i*self.gauge + (i+1)*self.indent + self.offset_y
                yk = yn + self.gauge
                #добавление прямоугольника на холст с тегом в формате:
                #префикс_строка_столбец
                self.canv.create_rectangle(xn,yn,xk,yk,tag = "my"+"_"+str(i)+"_"+str(j))

        #создание поля для компьютера
        #перебор строк
        for i in range(10):
            #перебор столбцов
            for j in range(10):
                xn = j*self.gauge + (j+1)*self.indent + self.offset_x_comp
                xk = xn + self.gauge
                yn = i*self.gauge + (i+1)*self.indent + self.offset_y
                yk = yn + self.gauge
                #добавление прямоугольника на холст с тегом в формате:
                #префикс_строка_столбец
                self.canv.create_rectangle(xn,yn,xk,yk,tag = "nmy"+"_"+str(i)+"_"+str(j))

        #добавление букв и цифр
        for i in reversed(range(10)):
            #цифры пользователя
            xc = self.offset_x_user - 15
            yc = i*self.gauge + (i+1)*self.indent + self.offset_y + round(self.gauge/2)
            self.canv.create_text(xc,yc,text=str(i+1))
            #цифры компьютера
            xc = self.offset_x_comp - 15
            yc = i*self.gauge + (i+1)*self.indent + self.offset_y + round(self.gauge/2)
            self.canv.create_text(xc,yc,text=str(i+1))
        #буквы
        symbols = "АБВГДЕЖЗИК"
        for i in range(10):
            #буквы пользователя
            xc = i*self.gauge + (i+1)*self.indent + self.offset_x_user + round(self.gauge/2)
            yc = self.offset_y - 15
            self.canv.create_text(xc,yc,text=symbols[i])

            #буквы компьютера
            xc = i*self.gauge + (i+1)*self.indent + self.offset_x_comp + round(self.gauge/2)
            yc = self.offset_y - 15
            self.canv.create_text(xc,yc,text=symbols[i])


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