from problems_package.problems import select_problem, problem_list, price_list


def menu_problem():
    while True:
        print("1- Engine- price: 2000 ")
        print("2- Breaks- price: 1000 ")
        print("3- 5000 km treatment- price: 500 ")
        print("4- 10,000 km treatment- price: 1000 ")
        print("5- Filters + Oil- price: 250")
        print("6- Gear- price: 1000")
        print("7- total cost")
        print("8- exit")
        select = int(input("enter your choose: "))
        if select > 7:
            break
        select_problem(problem_list, select, price_list)
