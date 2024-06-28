from problems_package.problem_menu import menu_problem, problem_list, price_list


def Total_Cars(car_list):
    print(f"now there are: {len(car_list)} in the garage")
    total_profit = sum(car["price"] for car in car_list)
    print(f"the profit of the garage: {total_profit}")


def get_list(car_list):
    for car in car_list:
        print(car)


def delete_car(car_list: list):
    car_to_delete = int(input("enter the number of car to delete "))
    for car in car_list:
        if car["car_number"] == car_to_delete:
            car_list.remove(car_to_delete)
            print(f"the car: {car} has been removed from the list")
        else:
            print(f"the car: {car_to_delete} is not on the list")


def search_car(car_list):
    car_to_search = int(input("enter the number of car to search "))
    car_search = [car for car in car_list if car["car_number"] == car_to_search]
    if car_search:
        print(f"the car found with {car_to_search}: {car_search}")
    else:
        print(f"no cars found starting with {car_to_search}")


def add_car(car_list):
    new_car = int(input("enter number of car "))
    menu_problem()
    add_car_to_list = input("are you want to continue? yes/no ")
    if add_car_to_list == "yes":
        car_to_add = {"number": new_car, "problem": problem_list, "price": price_list}
        car_list.append(car_to_add)
        print(car_list)
        print(f"The car: {new_car} has been added to the list")
    else:
        print(f"The car: {new_car} has not been added to the list")
