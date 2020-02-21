from math import sqrt, pi, sin, asin

print("Formula for Graph")

choice = ""
while choice != "a" and choice != "b":
    choice = input("enter a for degrees\nenter b for radians\n: ")
    if choice == "a":
        Conversion_Factor = (pi/180)
        Conversion_Factor_2 = (180/pi)
    if choice == "b":
        Conversion_Factor = 1
        Conversion_Factor_2 = (180/pi)
while True:
    choice_two = ""
    while choice_two != "a" and choice_two != "b":
        choice_two = input("enter a if\nangle unknown\nenter b if\nside unknown\n: ")

    if choice_two == "a":
        side_one = float(eval(input("Enter side1: ")))
        raw_angle_one = float(eval(input("Enter angle1: ")))
        side_two = float(eval(input("Enter side2: ")))

        c_angle_one = raw_angle_one * Conversion_Factor

        eq_side_first = side_two * sin(c_angle_one)
        c_angle_two = asin(eq_side_first/side_one)
        c_angle_two_deg = c_angle_two * Conversion_Factor_2
        print("Calculated Angle\nin Rads:", c_angle_two, "\nDeg:", c_angle_two_deg)

    if choice_two == "b":
        side_one = float(eval(input("Enter side1: ")))
        raw_angle_one = float(eval(input("Enter angle1: ")))
        raw_angle_two = float(eval(input("Enter angle2: ")))

        c_angle_one = raw_angle_one * Conversion_Factor
        c_angle_two = raw_angle_two * Conversion_Factor

        eq_side_first = side_one * sin(c_angle_two)
        side_two = (eq_side_first/sin(c_angle_one))
        print("Calculated Side\n: ", side_two)

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

