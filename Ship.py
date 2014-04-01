__author__ = 'Александр'

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
    свойство (указывается при создании объекта):префикс тега (для своих кораблей будет, например, "my", для чужих "nmy"
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
    #префикс тега
    prefix = ""
    #свойство: корабль был создан и не выходит за рамки поля
    ship_correct = 1

    #метод-конструктор
    def __init__(self,length,rasp,keypoint):
        self.status_map = []
        self.around_map = []
        self.coord_map = []
        self.death = 0
        self.ship_correct = 1
        #переопределить переменную self.prefix
        self.prefix = keypoint.split("_")[0]
        #создать массивы status_map и coord_map (в зависимости от направления)
        stroka = int(keypoint.split("_")[1])
        stolb = int(keypoint.split("_")[2])
        for i in range(length):
            self.status_map.append(0)
            #в зависимости от направления генерировать новые точки корабля
            #0 - горизонт (увеличивать столбец), 1 - вертикаль (увеличивать строку)
            if stolb + i > 9 or stroka + i > 9:
                self.ship_correct = 0
            if rasp == 0:
                self.coord_map.append(self.prefix+"_"+str(stroka)+"_"+str(stolb+i))
            else:
                self.coord_map.append(self.prefix+"_"+str(stroka+i)+"_"+str(stolb))
        for point in self.coord_map:
            ti = int(point.split("_")[1])
            tj = int(point.split("_")[2])
            for ri in range(ti-1,ti+2):
                for rj in range(tj-1,tj+2):
                    if ri>=0 and ri<=9 and rj>=0 and rj<=9:
                        if not(self.prefix+"_"+str(ri)+"_"+str(rj) in self.around_map) and not(self.prefix+"_"+str(ri)+"_"+str(rj) in self.coord_map):
                            self.around_map.append(self.prefix+"_"+str(ri)+"_"+str(rj))

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