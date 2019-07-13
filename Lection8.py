class Things:
    pass


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Sidewalks(Inanimate):
    pass


class Animals(Animate):
    def breathe(self):
        print('Дышит')

    def move(self):
        print('Идет')

    def eat_food(self):
        print('Кушает')


class Mammals(Animals):
    def feed_young_with_milk(self):
        print('Кормит детей молоком')


class Giraffes(Mammals):

    def left_foot_forward(self):
        print('Переставляет левую ногу вперед')

    def right_foot_forward(self):
        print('Переставляет правую ногу вперед')

    def left_foot_back(self):
        print('Переставляет левую ногу назад')

    def right_foot_back(self):
        print('Переставляет правую ногу назад')

    def __init__(self,spots):
        self.giraffe_spots = spots

    def find_food(self):
        self.move()
        print('Я нашел еду!')
        self.eat_food()

    def eat_leafs_from_trees(self):
        print('Кушает листья с деревьев')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()
    def dace_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

# turtle
'''import turtle

avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)'''

#1 Жирафий танец
reginald = Giraffes(100)
reginald.dance()

#2 Черепашьи вилы
'''import turtle

t = turtle.Pen()
u = turtle.Pen()
v = turtle.Pen()
w = turtle.Pen()

t.forward(100)
u.forward(110)
v.forward(110)
w.forward(100)
t.left(90)
t.forward(50)
w.right(90)
w.forward(50)
u.left(90)
u.forward(25)
v.right(90)
v.forward(25)
t.right(90)
t.forward(50)
w.left(90)
w.forward(50)
u.right(90)
u.forward(25)
v.left(90)
v.forward(25)'''
