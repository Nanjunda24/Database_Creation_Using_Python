class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):   # when declaringmethod inside class the method argimet self is mandatory 
        print(f"Car brand: {self.brand}")
        print(f"Car model id : {self.model}")
        print(f"Car year is : {self.year}")
    def check_year(self):
        total_year= 2025-self.year
        print("Total year : ",total_year)    

c = Car("TATA",2025,2027)

c.display()
c.check_year()
