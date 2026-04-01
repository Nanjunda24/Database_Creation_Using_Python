class Car:
    def __init__(self):
        self.__name="Nanjunda"

    def get_name(self):
        return self.__name
    
    def set_name(self, name):    # modify the name setter method is used 
        self.__name = name

c = Car()

print(c.get_name())   # to access get method is used

c.set_name("Charan  H G ")

print(c.get_name())
