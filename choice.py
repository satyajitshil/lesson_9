print("Select a choice:")
print("1. Bike")
print("2. Car")

option = int(input("Enter your choice, 1 or 2:"))

if option == 1:
    print("Pick your bike type:")
    print("1. Dirt Bike ")
    print("2. Road Bike")
    option = int(input("Enter your choice, 1 or 2:"))
    if option == 1:
        print("You chose a dirt bike")
    else:
        print("You chose a road bike")
else:
    print("Pick your car type:")
    print("1. SUV ")
    print("2. Sport")
    option = int(input("Enter your choice, 1 or 2:"))
    if option == 1:
        print("You chose a SUV")
    else:
        print("You chose a sports car")
    