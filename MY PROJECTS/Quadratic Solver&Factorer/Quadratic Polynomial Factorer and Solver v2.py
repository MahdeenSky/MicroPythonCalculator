from math import sqrt, pi

print("ax^2+bx+c=0")


def stopper():
    stop_flag = False
    stop_or_continue = ""
    while stop_or_continue != "a" or stop_or_continue != "b":
        stop_or_continue = input("Stop?: ")
        if stop_or_continue == "a":
            stop_flag = True
            break
        if stop_or_continue == "b":
            stop_flag = False
            break
    if stop_flag:
        raise SystemExit



def polynomial_checker(a, b, c):
    negative_factor = False
    if a < 0:
        negative_factor = True
    #  checks if gcf can be applied to simplify the quadratic expression
    b_divisible_by_a = (b % a == 0)
    c_divisible_by_a = (c % a == 0)
    check_divisible = (b_divisible_by_a and c_divisible_by_a)
    a_is_one = (a == (a / a))
    return a_is_one, check_divisible, negative_factor


def isclose(a, b, tol):
    if abs(a-b) <= tol:
        return True
    else:
        return False


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def fraction(a):
    factor = 0
    while True:
        factor += 1
        a_rounded = int(round(a*factor))
        if isclose(a*factor, a_rounded, 0.01):
            text = ("{}/{}".format(a_rounded, factor))
            return text


def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
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


def complete_the_square(a, b, c, output):
    a_original, b_original, c_original = float(a), float(b), float(c)
    a_is_one, check_divisible, negative_factor = polynomial_checker(a_original, b_original, c_original)
    if negative_factor:
        gcf = -int(gcd(int(-a_original), gcd(int(-b_original), int(-c_original))))
        b_original, c_original, a_original = -b_original, -c_original, -a_original

    if a_is_one and (check_divisible is False):
        gcf = ""

    elif check_divisible and (a_is_one is False):

        if negative_factor is False:
            gcf = int(gcd(int(a_original), gcd(int(b_original), int(c_original))))
        b_original, c_original, a_original = b_original / a_original, c_original / a_original, a_original / a_original

    else:
        gcf = ""
        b_original, c_original, a_original = b_original/a_original, c_original/a_original, a_original/a_original
    d = b_original / (2 * a_original)
    e = c_original - (b_original**2/(4 * a_original))

    d_eval = False
    e_eval = False
    if d > 0:
        sign1 = "+"
        if (d % 1 != 0):
            d = fraction(d)
            d_eval = True
    else:
        if (d % 1 != 0):
            d = fraction(-d)
            d_eval = True
        sign1 = "-"
        if d_eval is False:
            d = -d

    if e > 0:
        sign2 = "+"
        if (e % 1 != 0):
            e = fraction(e)
            e_eval = True
    else:
        if (e % 1 != 0):
            e = fraction(-e)
            e_eval = True
        sign2 = "-"
        if e_eval is False:
            e = -e

    if output:
        print("The Factored Form is:\n{}(x{}{})^2{}{}".format(gcf, sign1, d, sign2, e))
    if d_eval:
        d = -eval(d)
    elif d_eval is False:
        pass
    if e_eval:
        e = -eval(e)
    elif e_eval is False:
        e = -e

    return gcf, d, e


def quadratic_function(a, b, c, output):
    complete_square = False
    a_original, b_original, c_original = a, b, c
    if b ** 2 - 4 * a * c >= 0:
        a_is_one, check_divisible, negative_factor = polynomial_checker(a, b, c)
        if negative_factor:
            gcf = -int(gcd(int(-a), gcd(int(-b), int(-c))))
            b, c, a = -b, -c, -a
        if a_is_one or (check_divisible is False):
            gcf = ""
        elif check_divisible and (a_is_one is False):
            if negative_factor is False:
                gcf = int(gcd(int(a), gcd(int(b), int(c))))
            b, c, a = b/a, c/a, a/a
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        # Added a "-" to these next 2 values because they would be moved to the other side of the equation
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1, den1) = simplify_fraction(a, mult1)
        (num2, den2) = simplify_fraction(a, mult2)
        if (num1 > a) or (num2 > a):
            # acquires the complete square since it is not factorable using normal means
            if output:
                complete_the_square(a_original, b_original, c_original, True)
            complete_square = True
            gcf, d, e = complete_the_square(a_original, b_original, c_original, False)
        else:
            # Getting ready to make the print look nice
            if output:
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

        if output:
            complete_the_square(a_original, b_original, c_original, True)
            print("Solutions are imaginary")
        complete_square = True
        gcf, d, e = complete_the_square(a_original, b_original, c_original, False)
    if complete_square:
        return complete_square, gcf, d, e
    return complete_square


def solutions(a, b, c, complete_square):
    if complete_square is False:
        discriminant = b ** 2 - 4 * a * c
        if discriminant == 0:
            x_one = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # x_one
            if eval(fraction(x_one)) % 1 == 0:
                print("x1 is : ", int(x_one))
            else:
                print("x1 is : ", fraction(x_one))
        if discriminant > 0:
            x_one = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # x_one
            if eval(fraction(x_one)) % 1 == 0:
                print("x1 is : ", int(x_one))
            else:
                print("x1 is : ", fraction(x_one))
            x_two = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # x_two
            if eval(fraction(x_two)) % 1 == 0:
                print("x2 is : ", int(x_two))
            else:
                print("x2 is : ", fraction(x_two))
        if discriminant < 0:
            pass
    elif complete_square:
        gcf, d, e = a, b, c
        right_side = -e
        if gcf == "":
            gcf = 1
        right_side = right_side/gcf
        if (right_side % 1 != 0):
            right_side_3 = fraction(right_side)
        else:
            right_side_3 = right_side
        right_side_1 = sqrt(right_side)
        right_side_2 = -sqrt(right_side)
        x_one = right_side_1 - d
        x_two = right_side_2 - d
        sign_one = "+"
        sign_two = "-"
        print("x1 is : {}{}sqrt({})/{} or {} ".format(-d, sign_one, right_side_3, gcf, round(x_one, 3)))
        print("x2 is : {}{}sqrt({})/{} or {} ".format(-d, sign_two, right_side_3, gcf, round(x_two, 3)))


stop_flag = False
while True:
    try:
        if stop_flag is True:
            break

        a = float(eval(input("insert a: ").replace("pi", str(pi))))
        b = float(eval(input("insert b: ").replace("pi", str(pi))))
        c = float(eval(input("insert c: ").replace("pi", str(pi))))

        complete_square = quadratic_function(a, b, c, True)
        if complete_square:
            complete_square, a, b, c = quadratic_function(a, b, c, False)

        solutions(a, b, c, complete_square)
        stopper()

    except ValueError:
        stopper()
        pass
