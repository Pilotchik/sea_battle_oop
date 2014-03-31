from tkinter import *
from random import randrange

class Ship():
    '''
    Класс Ship - реализация поведения объекта корабль для игры "Морской бой"
    свойство (указывается при создании объекта):палубность (1 - 4)
    свойство (указывается при создании объекта):расположение (0 - горизонтальное, 1 - вертикальное)
    свойство (указывается при создании объекта):ключевая точка (тег в формате: "столбец_строка")
    свойство:массив со статусами точек, который формируется конструктором
    свойство:массив с координатами точек корабля, который формируется конструктором
    свойство:координаты точек вокруг корабля
    свойство:статус гибели корабля
    метод-конструктор:изменение массива со статусами точек, например [0,0,1,0]
    метод:shoot(координаты точки), возвращает 1 - если попали, 2 - убил, 0 - мимо
    '''
    
    #свойства объектов, описанные в классе
    #массив со статусами точек корабля
    status_map = []
    #массив с координатами точек корабля
    coord_map = []
    #точки вокруг корабля
    around_map = []
    #статус гибели корабля
    death = 0
    
    #метод-конструктор
    def __init__(self,length,rasp,keypoint):
        #создать массивы status_map и coord_map (в зависимости от направления)
        stolb = int(keypoint[0])
        stroka = int(keypoint[2])
        for i in range(length):
            self.status_map.append(0)
            #в зависимости от направления генерировать новые точки корабля
            #0 - горизонт (увеличивать столбец), 1 - вертикаль (увеличивать строку)
            if rasp == 0:
                self.coord_map.append(str(stolb+i)+"_"+str(stroka))    
            else:
                self.coord_map.append(str(stolb)+"_"+str(stroka+i))
        for point in self.coord_map:
            ti = int(point[0])
            tj = int(point[2])
            for ri in range(ti-1,ti+2):
                for rj in range(tj-1,tj+2):
                    if ri>=0 and ri<=9 and rj>=0 and rj<=9:
                        if not(str(ri)+"_"+str(rj) in self.around_map) and not(str(ri)+"_"+str(rj) in self.coord_map):
                            self.around_map.append(str(ri)+"_"+str(rj))

    #выстрел
    def shoot(self,shootpoint):
        #определить номер точки и изменить её статус
        status = 0
        for point in range(len(self.coord_map)):
            if self.coord_map[point] == shootpoint:
                self.status_map[point] = 1
                status = 1
                break
        if not(0 in self.status_map):
            status = 2
            self.death = 1
        return status

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


#инициализация окна
root = Tk()
root.title = "Морской бой"
root.geometry("800x500+100+100")

app = Application(master=root)
app.mainloop()
root.destroy()
