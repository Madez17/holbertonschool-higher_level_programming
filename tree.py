#!/usr/bin/python3
class Tree:
    def __init__(self):
	#create atributtes to calss:
        self.__height = 0 #height tree atributte private
        self.__age = 0 #age tree atributte private
        self.__alive = True #alive is init in true atributte private
        self.__oranges = [] #oranges array tha save oranges - atributte private
    def dead(self): #return True if three is dead 
        if self.__alive:
            return False
        else:
            return True

    def any_oranges(self): #Method that verify if there are orange.
        if len(self.__oranges) > 0:
            return True
        else:
            return False

    @property #DECORATOR to get height
    def height(self):
        print("Getter method height")
        return self.__height

    @height.setter #setter the value to height
    def height(self):
        self.__height = value

    @property#DECORATOR to get age
    def age(self):
        print("Getter method age")
        return self.__age
    
    def grow(self):
        self.__age += 1 #increase the age and conditions
        if self.__age > 80: #value if age is grather than 80 
            self.__alive = False 
        if self.__age >= 10 and self.__alive: #value age is greather than or equal 10 and if the tree is alive
            self.create_oranges() #call method that create orange

    @property #DECORATOR to get_alive
    def alive(self):
        print("Getter method alive")
        return self.__alive
    
    def create_oranges(self): #Method Creates orange.
        for i in range(15):
            self.__oranges.append(Orange()) #add orange to our atributte array orange private

    def pick_up(self): #Method pick_up our orange
        return self.__oranges.pop() #return the orange

class Orange: #New class orange
    def __init__(self): #create a new instance that class orange
        self.__diameter = 5 # diameter atributte private

    @property
    def diameter(self):
        print("Getter method diameter")
        return self.__diameter

tree  =  Tree()
print(tree.height(250))
print(tree.dead())
print(tree.any_oranges())
while (tree.any_oranges() == False):
    tree.grow()
i = 0
while (tree.any_oranges() == True):
    tree.pick_up()
    i += 1
print(i)

