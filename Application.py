__author__ = 'Александр'

from random import randrange
from time import time
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
    #время генерации флота
    fleet_time = 0

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

        self.fleet_time = time()
        #генерация кораблей противника
        self.createShips("nmy")

    def createShips(self, prefix):
        #функция генерации кораблей на поле
        #количество сгенерированных кораблей
        count_ships = 0
        while count_ships < 10:
            #массив занятых кораблями точек
            fleet_array = []
            #обнулить количество кораблей
            count_ships = 0
            #массив с флотом
            fleet_ships = []
            #генерация кораблей (length - палубность корабля)
            for length in reversed(range(1,5)):
                #генерация необходимого количества кораблей необходимой длины
                for i in range(5-length):
                    #генерация точки со случайными координатами, пока туда не установится корабль
                    err = 0
                    while 1:
                        err += 1
                        if err > 100:
                            print(length)
                            break
                        #генерация точки со случайными координатами
                        ship_point = prefix+"_"+str(randrange(10))+"_"+str(randrange(10))
                        #случайное расположение корабля (либо горизонтальное, либо вертикальное)
                        orientation = randrange(2)
                        #print(ship_point,orientation,length)
                        #создать экземпляр класса Ship
                        new_ship = Ship(length,orientation,ship_point)
                        #если корабль может быть поставлен корректно и его точки не пересекаются с уже занятыми точками поля
                        #пересечение множества занятых точек поля и точек корабля:
                        intersect_array = list(set(fleet_array) & set(new_ship.around_map+new_ship.coord_map))
                        if new_ship.ship_correct == 1 and len(intersect_array) == 0:
                            #добавить в массив со всеми занятыми точками точки вокруг корабля и точки самого корабля
                            fleet_array += new_ship.around_map + new_ship.coord_map
                            fleet_ships.append(new_ship)
                            count_ships += 1
                            #print("Корабль создан")
                            break

            print("Кораблей:",count_ships)
        print("Флот готов",fleet_ships)
        self.fleet = fleet_ships



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