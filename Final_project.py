# the prev reviwer said that options 3 and 5 gave the error :ValueError: invalid literal for int() with base 10:
# Option 5 however DOES NOT give this error
# Option 3 on the other hand asks the user to enter the quantity they want to update it to
# It Does show the updated quantity after the user chooses what quantity to update it to
# but when the user selects it again, it gives the error
class Shoes():
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
     return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: R{float(self.cost):.2f}\nQuantity: {self.quantity}"

shoes_list = []


def read_shoes_data():
    with open("inventory.txt", "r") as file:
        file_contents = file.readlines()
        for line in file_contents[1:]:
          line = line.split(",")
          product_entery = Shoes(line[0],line[1],line[2],line[3],line[4])
          shoes_list.append(product_entery)
        

def capture_shoes():
    # To keep consistent and append to file easier
    country = input("Country: ")
    code = input("Code: ").upper()
    product = input("Product: ")
    # Making user user enters a valid number
    while True:
        try:
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            break
        # If user entered an incorrect value they will be asked to try again
        except ValueError:
            print("Enter valid number value")
    # Creating shoe object to add to the list
    shoe = Shoes(
    country=country,
    code=code,
    product=product,
    cost=cost,
    quantity=quantity
    )
    # Appending shoe to list
    shoes_list.append(shoe)
    # Appending shoe to file
    with open("inventory.txt", "a") as shoes:
        shoes.write(f"\n{country},{code},{product},{cost},{quantity}")

def view_all():
    for item in shoes_list:
        print(item.__str__())
      

def re_stock():
    lowest_quantity = shoes_list [0]
    for shoe in shoes_list:
        if int(shoe.get_quantity()) < int(lowest_quantity.get_quantity()):
            lowest_quantity = shoe
    print(f"Lowest quantity details:\n"+ str(lowest_quantity))

  
    need_restock = input("Do you want to add to quantity of shoes(yes/no): ")
    if need_restock.lower() == "yes":
        quantity_to_update = input("Enter quantity to update: ")
        lowest_quantity.quantity = str(float(lowest_quantity.get_quantity()) + float(quantity_to_update))
        print(lowest_quantity)
        shoes_list.append(lowest_quantity.quantity)
    else:
        print("You chose not to restock.")

    with open('inventor.txt','w') as file:
        file.write(lowest_quantity.quantity)



def search_shoe():
    search_code = input("please enter the code of the shoe: ")
    for shoe in shoes_list:
        if shoe.code == search_code:
            return shoe    

def value_per_item():
    for shoe in shoes_list:
        value = float(shoe.cost) * int(shoe.quantity)
        print(f"\n {shoe.code} {shoe.product} total = {value}")


def highest_quantity():
    highest_quantity = shoes_list[0]
    for shoe in shoes_list:
        if shoe.get_quantity() == highest_quantity.get_quantity():
            shoe = highest_quantity
    print(f"{shoe} is on sale!")

def menu():
    
        print("""
Please select one of the following options:
1.) Capture shoes.
2.) View all shoes.
3.) Restock shoes.
4.) Search shoe.
5.) Get total value of stock 
6.) Shoe for sale.
""")

menu()
option = input("Enter your option: ")
read_shoes_data()
while option != 0:
    if option == '1':
        capture_shoes()

    elif option == '2':
        view_all()
        

    elif option == '3':
        re_stock()
        

    elif option == '4':
         print( search_shoe())
        

    elif option == '5':
         value_per_item()
       

    elif option == '6':
        highest_quantity()


    else:
        print("Invalid option!")
        
    print()
    menu()
    option = input("Enter your option: ")





















