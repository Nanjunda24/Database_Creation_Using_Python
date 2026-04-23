class database:
    def __init__(self):
        self.storage = {}

    def write(self,key,value):
        self.storage[key] = value 
        print("Data added successfully completed!!!!")

    def read(self,key):
        if key in self.storage:
            print(self.storage[key])
        else:
            print("Data not found in data base")

    def del_data(self, key):
        if key in self.storage:
            del self.storage[key]
            print("After deletion of item: ",self.storage)
        else:
            print("Data not found in  database!!!")
    
    def display(self):
        if len(self.storage)== 0:
            print("No data available in database!!!!")
        else:
            print("Databse data: " ,self.storage)

d = database()

d.write("Name","Nanjunda K M")
d.write("USN","1RR22IS028")
d.write("College","Rajarajeswari college of Engineering")
d.read("College")
d.del_data("Collage")
d.display()

