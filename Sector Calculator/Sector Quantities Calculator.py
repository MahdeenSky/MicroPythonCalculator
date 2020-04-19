from math import pi, sin

def input_pi_replacer(prompt):
    return float(eval(input(prompt).replace("pi", str(pi))))

def stopper():
    stop_or_continue = input("Stop?: ")
    if stop_or_continue == "x":
        raise SystemExit  

print("Sector Quantities\nCalculator:\n")
C_Factor = 0
Area = 0
B = 0
while True:
    C_Factor = 0
    Area = 0

    Unit = ""
    # a = degrees , b = radians
    Unit = {'a': 'Degrees', 'b': 'Radians'}
    choice_type = ""
    while choice_type not in ['a', 'b']:
        choice_type = input("For Deg, enter 'a',\nFor Rad, enter 'b'\n: ")
        Unit = Unit[choice_type]
        if Unit == "Degrees":
            C_Factor = pi/180
            break
        if Unit == "Radians":
            C_Factor = 180/pi
            break
        if Unit == ".":
            raise SystemExit
    # R = Radius, A = theta/angle in deg/rads, C_Angle = Converted Angle, C_Factor = Conversion Factor of Angle

    R = input_pi_replacer("\nEnter Radius: ")
    A = input_pi_replacer("Enter Theta/Angle: ")

    if Unit == "Degrees":
        C_Angle = A * C_Factor
        Angle_In_Deg = A
    elif Unit == "Radians":
        C_Angle = A
        Angle_In_Deg = A * C_Factor

    print()
    Sector_Area = 1/2 * (R**2) * C_Angle
    Triangle_Area = 1/2 * (R**2) * sin(C_Angle)
    Arc_Length = R * C_Angle
    Chord_Area = Sector_Area - Triangle_Area
    Chord_Length = 2 * R * sin(C_Angle/2)
    Perimeter_Sector = 2 * R + Arc_Length
    print("Area of Sector\n= ", round(Sector_Area, 4))
    print("Area of inner Triangle\n= ", round(Triangle_Area, 4))
    print("Arc Length\n= ", round(Arc_Length, 4))
    print("Chord Area\n= ", round(Chord_Area, 4))
    print("Chord Length\n= ", round(Chord_Length, 4))
    print("Sector Perimeter\n= ", round(Perimeter_Sector, 4))
    print()
    stopper()
