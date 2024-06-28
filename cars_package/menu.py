
from cars_package.actions import get_list, delete_car, search_car, add_car


def selection(car_list, select):
    if select == 1:
        get_list(car_list)
    elif select == 2:
        car_list = add_car(car_list)
    elif select == 3:
        delete_car(car_list)
    elif select == 4:
        search_car(car_list)
