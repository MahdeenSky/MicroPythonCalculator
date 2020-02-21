from math import pi, sin


print("Sector Quantities\nCalculator:\n")
C_Factor = 0
Area = 0
B = 0
while True:
    C_Factor = 0
    Area = 0

    Unit = ""
    # + = degrees , - = radians
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
    # R = Radius, A = theta/angle in deg/rads, C_Angle = Converted Angle, C_Factor = Conversion Factor of Angle

    if Unit == ".":
        break

    R = float(eval(input("\nEnter Radius: ").replace("pi", str(pi))))
    A = float(eval(input("Enter Theta/Angle: ").replace("pi", str(pi))))

    if Unit == "+":
        C_Angle = A * C_Factor
        Angle_In_Deg = A
    if Unit == "-":
        C_Angle = A
        Angle_In_Deg = A * C_Factor

    print()
    Sector_Area = 1/2 * (R**2) * C_Angle
    Triangle_Area = 1/2 * (R**2) * sin(C_Angle)
    Arc_Length = R * C_Angle
    Chord_Area = Sector_Area - Triangle_Area
    Chord_Length = 2 * R * sin(C_Angle/2)
    Perimeter_Sector = 2 * R + Arc_Length
    print("Area of Sector\n= ", Sector_Area)
    print("Area of inner Triangle\n= ", Triangle_Area)
    print("Arc Length\n= ", Arc_Length)
    print("Chord Area\n= ", Chord_Area)
    print("Chord Length\n= ", Chord_Length)
    print("Sector Perimeter\n= ", Perimeter_Sector)
    print()
    stop_or_continue = input("Stop?: ")
    if stop_or_continue == "y":
        break
    if stop_or_continue == "n":
        pass
