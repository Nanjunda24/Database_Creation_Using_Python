class Student:
    def __init__(self,name,marks):  # constructor
        self.__name = name    #private variable 
        self.__marks = marks

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_marks(self, marks):
        if isinstance(marks,int):
            if (marks <= 100 ):
                self.__marks = marks
            else:
                print("Marks should be less than 100")
        else:
            print("Marks should be int means integer ")

    def get_marks(self ):
        return self.__marks
s = Student()

s.set_name("Nanjunda")

print(s.get_name())

s.set_marks(101)

print(s.get_marks())


