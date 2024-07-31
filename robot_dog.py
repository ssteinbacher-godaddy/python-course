class RobotDog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val
    def bark(self):
        print('woof')   

#Main program
mydog = RobotDog('bot', 'bulldog')
print(mydog.name)
print(mydog.breed) 
mydog.bark() 