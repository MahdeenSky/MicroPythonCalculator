from math import sqrt

print("Formula Solver")

while True:
    choice = ""
    while choice != "a" and choice != "b":
        choice = input("enter a for distance\nenter b for midpoint\n: ")

    if choice == "a":
        x_one = float(eval(input("enter x1: ")))
        y_one = float(eval(input("enter y1: ")))
        x_two = float(eval(input("enter x2: ")))
        y_two = float(eval(input("enter y2: ")))

        delta_x = x_one - x_two
        delta_y = y_one - y_two
        whole = delta_x**2 + delta_y**2
        distance = sqrt(whole)
        print("Length/distance\n: ", distance)

    if choice == "b":
        x_one = float(eval(input("enter x1: ")))
        y_one = float(eval(input("enter y1: ")))
        x_two = float(eval(input("enter x2: ")))
        y_two = float(eval(input("enter y2: ")))

        sum_x = x_one + x_two
        sum_y = y_one + y_two
        mid_x = sum_x/2
        mid_y = sum_y/2
        print("Mid-point is\n: (", mid_x, ",", mid_y, ")")

    stop_flag = 0
    while True:
        stop_or_continue = input("Stop?: ")
        if stop_or_continue == "y":
            stop_flag = 1
            break
        if stop_or_continue == "n":
            stop_flag = 0
            break

    if stop_flag == 1:
        break
    else:
        pass

