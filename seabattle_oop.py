from tkinter import *

class Ship():
    '''
    Класс Ship - реализация поведения объекта корабль для игры "Морской бой"
    свойство (указывается при создании объекта):палубность (1 - 4)
    свойство (указывается при создании объекта):расположение (0 - горизонтальное, 1 - вертикальное)
    свойство (указывается при создании объекта):ключевая точка (тег в формате: "столбец_строка")
    свойство:массив со статусами точек, который формируется конструктором
    свойство:статус гибели корабля
    метод-конструктор:изменение массива со статусами точек, например [0,0,1,0]
    метод:выстрел(координаты точек)
    метод:вернуть координаты точек вокруг корабля
    '''
    
    #свойства
    #массив со статусами точек корабля
    status_map = []

    death = 0
    
    #метод-конструктор
    def __init__(self,length,rasp,keypoint):
        print(length,rasp,keypoint)

obj = Ship(4,0,"0_0")
print(Ship.__doc__)
