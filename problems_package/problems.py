problem_list = []
price_list = []


def select_problem(problem_list, select, price_list):
    if select == 1:
        problem = "Engine"
        price = 2000
        problem_list.append(problem)
        price_list.append(price)
        print(f"your choise is {problem}, the price is {price}")
    elif select == 2:
        problem = "Breaks"
        price = 1000
        problem_list.append(problem)
        price_list.append(price)
        print(f"your choise is {problem}, the price is {price}")
    elif select == 3:
        problem = "5000 km treatment"
        price = 500
        problem_list.append(problem)
        price_list.append(price)
        print(f"your choise is {problem}, the price is {price}")
    elif select == 4:
        problem = "10,000 km treatment"
        price = 1000
        problem_list.append(problem)
        price_list.append(price)
        print(f"your choise is {problem}, the price is {price}")
    elif select == 5:
        problem = "Filters + Oil"
        price = 250
        problem_list.append(problem)
        price_list.append(price)
        print(f"your choise is {problem}, the price is {price}")
    elif select == 6:
        problem = "Gear"
        price = 1000
        problem_list.append(problem)
        price_list.append(price)
        print(f"your choise is {problem}, the price is {price}")
    elif select == 7:
        total_price = 0
        for price in price_list:
            total_price += price
        print(f"the total price- {total_price}")
