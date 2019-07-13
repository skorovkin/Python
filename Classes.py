class Things:
    pass


class Inanimate (Things):
    pass


class Animate (Things):
    pass


class Sidewalks (Inanimate):
    pass


class Animal (Animate):
    def breathe(self):
        pass

    def move (self):
        print ("I'm mooving")

    def eat_food (self):
        pass


class Mammals (Animal):
    def feed_young_with_milk (self):
        pass


class Giraffes (Mammals):
    def eat_leaves_from_trees (self):
        pass

    def giraffe_name(self,name):
        print ('Я жираф по имени %s' %(name))


reginald = Giraffes ()
reginald.move ()
reginald.giraffe_name('Reginald')
harold = Giraffes ()
harold.move ()
import turtle
avery = turtle.Pen ()
kate = turtle.Pen ()
avery.forward(40)
kate.circle(50)

