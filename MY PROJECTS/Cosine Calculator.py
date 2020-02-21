from math import cos, pi, sqrt, acos

print("Cosine Solver\n")

Unit = ""
unknown = ""
while Unit != "+" or "-":
    Unit = input("For Deg, enter '+',\nFor Rad, enter '-'\n: ")
    if Unit == "+":
        C_Factor = pi/180
        break
    if Unit == "-":
        C_Factor = 180/pi
        break
    if Unit == ".":
        break


while True:
    temp = 0
    unknown = ""
    while unknown != "a" and unknown != "A":
        unknown = input("Enter a\nfor side or\nA for angle\n: ")

    if unknown == "a":
        b = float(eval(input("Enter Side1: ")))
        c = float(eval(input("Enter Side2: ")))
        temp = input("Enter Theta/Angle: ").replace("pi", str(pi))
        A = float(eval(temp))

        if Unit == "+":
            C_Angle = A * C_Factor
            Angle_In_Deg = A
        if Unit == "-":
            C_Angle = A
            Angle_In_Deg = A * C_Factor

        Value = b**2 + c**2 - 2*b*c*cos(C_Angle)
        Ans = sqrt(Value)
        print("The Res. Side is\n: ", Ans)

    if unknown == "A":
        b = float(eval(input("Enter Side1: ").replace("pi", str(pi))))
        c = float(eval(input("Enter Side2: ").replace("pi", str(pi))))
        a = float(eval(input("Enter Side3: ").replace("pi", str(pi))))

        Value = (b**2 + c**2 - a**2)/(2*b*c)
        Ans_Rad = acos(Value)
        Ans_Deg = acos(Value) * (180/pi)
        print("The Angle in\nRads is: ", Ans_Rad, "\nDeg is: ", Ans_Deg)

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
