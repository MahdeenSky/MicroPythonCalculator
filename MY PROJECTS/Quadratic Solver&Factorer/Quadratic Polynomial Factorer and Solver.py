from math import sqrt, pi, isclose, gcd

print("ax+by+c=0")


def gcd_2(a, b):
    while b:
        a, b = b, a % b
    return a


def fraction(a):
    factor = 0
    while True:
        factor += 1
        a_rounded = int(round(a*factor))
        if isclose(a*factor, a_rounded, abs_tol=0.01):
            text = ("{}/{}".format(a_rounded, factor))
            return text


def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd_2(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if common_divisor == 1:
        return (numer, denom)
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return (-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)


def quadratic_function(a, b, c):
    a_original, b_original, c_original = a, b, c
    if b ** 2 - 4 * a * c >= 0:
        negative_factor = False
        if a < 0:
            negative_factor = True
        #  checks if gcf can be applied to simplify the quadratic expression
        b_divisible_by_a = (b % a == 0)
        c_divisible_by_a = (c % a == 0)
        check_divisible = (b_divisible_by_a and c_divisible_by_a)
        a_is_one = (a == (a/a))
        if negative_factor:
            gcf = -int(gcd(int(-a), gcd(int(-b), int(-c))))
            b, c, a = -b, -c, -a
        if a_is_one or (check_divisible is False):
            gcf = ""
        elif check_divisible and (a_is_one is False):
            if negative_factor is False:
                gcf = int(gcd(int(-a), gcd(int(-b), int(-c))))
            b, c, a = b/a, c/a, a/a
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        # Added a "-" to these next 2 values because they would be moved to the other side of the equation
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1, den1) = simplify_fraction(a, mult1)
        (num2, den2) = simplify_fraction(a, mult2)
        if (num1 > a) or (num2 > a):
            # simplify fraction will make too large of num and denom to try to make a sqrt work
            print("No factorization")
            c =(b/2)**2

        else:
            # Getting ready to make the print look nice
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            print("The Factored Form is:\n{}({}x{}{})({}x{}{})".format(gcf, int(num1), sign1, int(den1), int(num2), sign2,int(den2)))
    else:
        # if the part under the sqrt is negative, you have a solution with i
        print("Solutions are imaginary")
    return


while True:
    try:
        stop_flag = 0
        stop_or_continue = ""
        a = float(eval(input("insert a: ").replace("pi", str(pi))))
        b = float(eval(input("insert b: ").replace("pi", str(pi))))
        c = float(eval(input("insert c: ").replace("pi", str(pi))))

        quadratic_function(a, b, c)

        discriminant = b ** 2 - 4 * a * c


        if discriminant == 0:
            x_one = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)   # x_one
            if eval(fraction(x_one)) % 1 == 0:
                print("x1 is : ", x_one)
            else:
                print("x1 is : ", fraction(x_one))
        if discriminant > 0:
            x_one = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # x_one
            if eval(fraction(x_one)) % 1 == 0:
                print("x1 is : ", x_one)
            else:
                print("x1 is : ", fraction(x_one))
            x_two = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # x_two
            if eval(fraction(x_two)) % 1 == 0:
                print("x2 is : ", x_two)
            else:
                print("x2 is : ", fraction(x_two))
        if discriminant < 0:
            pass

        while stop_or_continue != "a" or "b":
            stop_or_continue = input("Stop?: ")
            if stop_or_continue == "a":
                stop_flag = 1
                break
            if stop_or_continue == "b":
                stop_flag = 0
                break
        if stop_flag == 1:
            break

    except ValueError:
        pass

