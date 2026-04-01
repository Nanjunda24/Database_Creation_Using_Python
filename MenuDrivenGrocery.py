class Grocery:
    def __init__(self):
        self.list_item = [ ]
    def add_item(self ,item):
        
        self.list_item.append(item)
        print(f"{item} added successfully to the cart!!!!")

    def remove_item(self,item):
        if item not in self.list_item:
            print("Entered iten not in the cart ")
        else:
            self.list_item.remove(item) 
            print(f"{item} removed successfully from the cart !!!")  

    def show_items(self):
        print("Items in cart : ",self.list_item)

g = Grocery()         

while True:
    print("----------Grocery simulation-----------")
    print("1. Show item in cart ")
    print("2. Add item to cart ")
    print("3. Remove item from the cart ")
    print("4. Exit")


    choice = int(input("Enter an your choic: "))

    if choice == 1:
        g.show_items()

    elif choice == 2:
        item = input("Enter an item to add into cart : ")
        g.add_item(item)
    
    elif choice == 3:
        item = input("Enter item to remove from the cart: ")
        g.remove_item(item)

    elif choice == 4:
        print("Exited successfully!!!!!")
        break
    else:
        print("You entered invalid choice!!!!")

        

    