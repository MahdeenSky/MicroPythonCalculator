from math import sqrt, pi, acos, cos, sin, asin

print("Formula Solver")

def stopper():
    stop_or_continue = input("Stop?: then enter x ")
    if stop_or_continue == "x":
        raise SystemExit    

def float_eval_input(prompt):
    return float(eval(input(prompt)))

def pi_replacer_input(prompt):
    return float(eval(input(prompt).replace("pi", str(pi))))

while True:
    choice = {'a':'distance', 'b':'midpoint', 'c':'cosine rule', 'd':'sine rule'}
    choice_dict = input("enter a for distance\nb for midpoint\nc for cosine rule\nd for sine rule\n: ")
    choice = choice[choice_dict]

    if choice == "distance": # # #
        x_one = float_eval_input("enter x1: ")
        y_one = float_eval_input("enter y1: ")
        x_two = float_eval_input("enter x2: ")
        y_two = float_eval_input("enter y2: ")

        delta_x = x_one - x_two
        delta_y = y_one - y_two
        whole = delta_x**2 + delta_y**2
        distance = sqrt(whole)
        print("Length/distance\n: ", distance)

    if choice == "midpoint": # # #
        x_one = float(eval(input("enter x1: ")))
        y_one = float(eval(input("enter y1: ")))
        x_two = float(eval(input("enter x2: ")))
        y_two = float(eval(input("enter y2: ")))

        sum_x, sum_y = (x_one + x_two), (y_one + y_two)
        mid_x, mid_y  = (sum_x/2), (sum_y/2)
        print("Mid-point is\n: (", mid_x, ",", mid_y, ")")

    if choice == "cosine rule": # # #

        Unit = {'a': 'Degrees', 'b': 'Radians'}
        unknown = ""
        choice_type = ""
        while choice_type not in {'a', 'b'}:
            choice_type = input("For Deg, enter 'a',\nFor Rad, enter 'b'\n: ")
            Unit = Unit[choice_type]
            if Unit == "Degrees":
                C_Factor = pi/180
                break
            if Unit == "Radians":
                C_Factor = 180/pi
                break
            if Unit == ".":
                break

        temp = None
        unknown = {'a': 'Resultant-Side', 'A': 'Angle'}
        choice = input("Enter a\nfor side or\nA for angle\n: ")
        unknown = unknown[choice]

        if unknown == "Resultant-Side":
            b = float(eval(input("Enter Side1: ")))
            c = float(eval(input("Enter Side2: ")))
            temp = pi_replacer_input("Enter Theta/Angle: ")
            if type(temp) is str:
                A = float(eval(temp))
            else:
                A = float(temp)

            if Unit == "Degrees":
                C_Angle = A * C_Factor
                Angle_In_Deg = A
            if Unit == "Radians":
                C_Angle = A
                Angle_In_Deg = A * C_Factor

            Value = b**2 + c**2 - 2*b*c*cos(C_Angle)
            Ans = sqrt(Value)
            print("The Res. Side is\n: ", round(Ans, 4))

        if unknown == "Angle":
        
            b = pi_replacer_input("Enter Side1: ")
            c = pi_replacer_input("Enter Side2: ")
            a = pi_replacer_input("Enter Side3: ")

            Value = (b**2 + c**2 - a**2)/(2*b*c)
            Ans_Rad = acos(Value)
            Ans_Deg = acos(Value) * (180/pi)
            print("The Angle in\nRads is: ", round(Ans_Rad, 5), "\nDeg is: ", round(Ans_Deg, 5))

    if choice == "sine rule": # # #

        choice_type = None
        choice_dict = {'a':'Degrees', 'b': 'Radians'}
        while choice_type not in ['a', 'b']:
            choice_type = input("enter a for degrees\nenter b for radians\n: ")
            choice = choice_dict[choice_type]
            if choice == "Degrees":
                Conversion_Factor = (pi/180)
                Conversion_Factor_2 = (180/pi)
            if choice == "Radians":
                Conversion_Factor = 1
                Conversion_Factor_2 = (180/pi)

        
        choice_two_dict = {'a': 'angle_unknown', 'b':'side_unknown'}
        choice_two_type = None
        while choice_two_type not in ['a', 'b']:
            choice_two_type = input("enter a if\nangle unknown\nenter b if\nside unknown\n: ")
            choice_two = choice_two_dict[choice_two_type]

        if choice_two == "angle_unknown":
            side_one = float_eval_input("Enter Side1: ")
            raw_angle_one = float_eval_input("Enter Angle1: ")
            side_two = float_eval_input("Enter Side2: ")

            c_angle_one = raw_angle_one * Conversion_Factor

            eq_side_first = side_two * sin(c_angle_one)
            c_angle_two = asin(eq_side_first/side_one)
            c_angle_two_deg = c_angle_two * Conversion_Factor_2
            print("Calculated Angle\nin Rads:", round(c_angle_two, 4), "\nDeg:", round(c_angle_two_deg, 4))

        if choice_two == "side_unknown":
            side_one = float_eval_input("Enter Side1: ")
            raw_angle_one = float_eval_input("Enter Angle1: ")
            raw_angle_two = float_eval_input("Enter Angle2: ")

            c_angle_one = raw_angle_one * Conversion_Factor
            c_angle_two = raw_angle_two * Conversion_Factor

            eq_side_first = side_one * sin(c_angle_two)
            side_two = (eq_side_first/sin(c_angle_one))
            print("Calculated Side\n: ", round(side_two, 4))


    stopper()

