# quadratic factorer, and solver
from math import sqrt

def gcd(*values):
    x, *b = values
    for y in b:
        while y != 0:
            (x, y) = (y, x % y)
    return x


def isclose(a, b, tolerance):
    return abs(a-b) <= tolerance


def fraction(a, factor=0):
    while True:
        factor += 1
        a_rounded = int(round(a*factor))
        if isclose(a*factor, a_rounded, 0.01):
            break
    if factor == 1:
        return a_rounded
    else:
        return "{}/{}".format(a_rounded, factor)


def simplify_fraction(numer, denom):
    if denom == 0:
        return None, None

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    reduced_num, reduced_den = numer / common_divisor, denom / common_divisor
    # Note that reduced_den > 0 as documented in the gcd function.

    if common_divisor == 1:
        return numer, denom
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if reduced_den > denom:
            if (reduced_den * reduced_num < 0):
                return -reduced_num, -reduced_den
            else:
                return reduced_num, reduced_den
        else:
            return reduced_num, reduced_den


def get_determinant(a, b, c):
    return b**2 - 4*a*c


def solve_quadratic_equation(a, b, c):
    determinant = get_determinant(a, b, c)
    # two solutions, or one solution
    if determinant >= 0:
        return ( (-b+sqrt(get_determinant(a, b, c))) / (2*a), (-b-sqrt(get_determinant(a, b, c))) / (2*a)) # (x1, x2)
    # no solutions
    else:
        return None


def factor_quadratic_equation(a, b, c):
    a_original, b_original, c_original = a, b, c

    if get_determinant(a, b, c) >= 0:
        expression_is_divisible = ((b % a == 0) and (c % a == 0))

        gcf = gcd(a, b, c)
        if a < 0:
            gcf = -gcf
            a, b, c = -a, -b, -c

        if a == 1 or not expression_is_divisible:
            gcf = ""
        elif expression_is_divisible and not (a == 1):
            a, b, c = a/a, b/a, c/a

        x1, x2 = solve_quadratic_equation(a, b, c)
        mult1, mult2 = -x1*a, -x2*a
        num1, den1 = simplify_fraction(a, mult1)
        num2, den2 = simplify_fraction(a, mult2)

        if (num1 > a) or (num2 > a): # then complete square 2(x+3) + 1
            # a(x+p)^2 + q
            a, b, c = a_original, b_original, c_original
            p = b/(2*a)
            q = c - (b**2)/(4*a)
            sign1 = "+" if p > 0 else "-"
            sign2 = "+" if q > 0 else "-"
            p = -p if sign1 == "-" else p
            q = -q if sign2 == "-" else q

            return "{}(x{}{})^2 {} {}".format(a, sign1, fraction(p), sign2, fraction(q))

        else: # normal factoring (x+3)(x+3) or 2(x+3)(x+3)
            sign1 = "+" if den1 > 0 else ""
            sign2 = "+" if den2 > 0 else ""
            return "{}({}x{}{})({}x{}{})".format(gcf, fraction(num1), sign1, fraction(den1), fraction(num2), sign2, fraction(den2))

    else: # no factored form
        return None 


while True:
    a = int(input("insert a: "))
    b = int(input("insert b: "))
    c = int(input("insert c: "))
    factored_form = factor_quadratic_equation(a, b, c)
    solutions = solve_quadratic_equation(a, b, c)

    print(factored_form) if factored_form else print("No Factored Form")

    if solutions:
        print("x1 = {}".format(round(solutions[0], 5)))
        if solutions[0] != solutions[1]:
            print("x2 = {}".format(round(solutions[1], 5)))
    else:
        print("No Solution")

    stop = input("'x' to stop: ")
    if stop == 'x':
        break
         



    






