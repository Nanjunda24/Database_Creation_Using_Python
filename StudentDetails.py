class Student:
    def __init__(self):
        self.student_details = {}
    
    def add_student_details(self,key,value):
        self.student_details[key] = value
        print("Student details added successfully!!!!!")

    def display_details(self):
        return self.student_details
    
    def remove(self,item):
         if item in self.student_details:
            del self.student_details[item]
            print("Student removed successfully!!!")
         else:
              print("Entered details not in the storage: ")
s = Student()

while True:
    print("----------------Student_details--------------")
    print("1. Add student datails ")
    print("2. Display student details ")
    print("3. Remove student details ")
    print("4. Exit ")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        key = input("Enter the key student details : ")
        value = input("Enter the value to key : ")
        s.add_student_details(key,value)
    elif choice == 2:
            print("student details are displayed successfully!!!!")
            print(s.display_details())
    
    elif choice ==3:
         item = input("Enter item to remove the  item for the stuident details ")
         s.remove(item)
        
    elif choice ==4:
         print("Exit successfully!!!!")
         break
    else:
         print("Enter the valid choice")

