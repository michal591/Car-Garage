from cars_package.menu import selection
from cars_package.actions import Total_Cars

car_list = [{"car_number": 1111111, "problem": "Engine", "price": 2000}]


def menu():
    Total_Cars(car_list)
    while True:
        print("1- get the cars list ")
        print("2- add a car ")
        print("3- delete a car ")
        print("4- search a car from the car list ")
        print("5- exit")
        select = int(input("enter your choose: "))
        if select == 5:
            break
        selection(car_list, select)


if __name__ == "__main__":
    menu()
