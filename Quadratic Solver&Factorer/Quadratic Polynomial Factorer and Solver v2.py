# quadratic factorer, and solver
from math import sqrt

def gcd(*values):
    x, *b = values
    for y in b:
        while y != 0:
            (x, y) = (y, x % y)
    return abs(x)


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
        return 0, 0

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
        return reduced_num, reduced_den


def get_determinant(a, b, c):
    return b**2 - 4*a*c


def factors(n): # finds the factors
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(sqrt(n))+1) if n % i == 0) for x in tup)


def simplify_sqrt(n): # simplifies sqrt(n)
    perfect_square = None
    float_to_int = lambda x: int(x) if x.is_integer() else x
    for factor in tuple(sorted(factors(n)))[:0:-1]:
        if (sqrt(factor)).is_integer():
            perfect_square = factor
            break

    if perfect_square == n:
        return (int(sqrt(perfect_square)), 0)

    elif perfect_square:
        factor1 = sqrt(perfect_square)
        factor2 = n / perfect_square
        return (float_to_int(factor1), float_to_int(factor2))

    else:
        return (0, n)


def format_tuple_to_sqrt(A, B): # Asqrt(B) 
    if A == 0:
        A = ""
    elif B == 0:
        return str(A)
    return "{}sqrt({})".format(A, B)


def solve_completing_the_square(a, b, c): # ( x +- ysqrt(B) )/z
    f = simplify_sqrt(get_determinant(a, b, c))
    g = gcd(f[0], 2*a, -b)
    # x, y, B, z
    return -b/g, [int(f[0]/g), f[1]], (2*a)/g # x, (h[0], h[1]), z


def format_complete_the_square_solutions(x, h, z): # h = (y, B) --> ysqrt(B)
    # ( x +- h[0]sqrt(h[1]) )/z
    h[0] = 0 if h[0] == 1 else h[0]
    h = format_tuple_to_sqrt(*h)
    if z < 0:
        x, z = x*-1, z*-1

    sol1 = "( {} + {} )/{}".format(int(x), h, int(z))
    sol2 = "( {} - {} )/{}".format(int(x), h, int(z))
    if z == 1:
        return sol1[:-2], sol2[:-2]
    return sol1, sol2


def solve_quadratic_equation(a, b, c):
    determinant = get_determinant(a, b, c)
    # two solutions, or one solution
    if determinant >= 0:
        return ( (-b+sqrt(get_determinant(a, b, c))) / (2*a), (-b-sqrt(get_determinant(a, b, c))) / (2*a)) # (x1, x2)
    # no solutions
    else:
        return None


def factor_quadratic_equation(a, b, c):
    get_sign = lambda x: "+" if x > 0 else "-" # set the sign based on x's value
    flip_sign_if_negative = lambda x, sign: -x if sign == '-' else x # switch the signs for formatting if sign == '-'
    float_to_int = lambda x: int(x) if x.is_integer() else x # only if the float is actually an integer like 3.0

    if get_determinant(a, b, c) >= 0:

        if c == 0: # factor by gcf 6x^2 - 2x
            gcf = gcd(a, b)
            a, b = a/gcf, b/gcf
            gcf = "" if gcf == 1 else gcf

            sign = get_sign(b)
            b = flip_sign_if_negative(b, sign)

            return "{}x({}x{}{})".format(float_to_int(gcf), fraction(a), sign, fraction(b))
 
        else: 
            denom = 2*a
            x1, x2 = solve_quadratic_equation(a, b, c)
            x1_numer, x2_numer = x1*denom, x2*denom

            if not (x1_numer.is_integer() and x2_numer.is_integer()) or not denom.is_integer(): 
                global completing_the_square
                completing_the_square = True
            # factor by completing the square 2(x+3) + 1
            # (x+p)^2 + q
                if a != 1:
                    a, b, c = a/a, b/a, c/a

                p = b/(2*a)
                q = c - (b**2)/(4*a)

                sign1 = get_sign(p)
                sign2 = get_sign(q)
                p = flip_sign_if_negative(p, sign1)
                q = flip_sign_if_negative(q, sign2)

                return "(x{}{})^2 {} {}".format(sign1, fraction(p), sign2, fraction(q))

            else: 
            # normal factoring (x+3)(x+3)
                x1_gcd, x2_gcd = gcd(x1_numer, denom), gcd(x2_numer, denom)
                x1_numer, x2_numer = -x1_numer/x1_gcd, -x2_numer/x2_gcd
                x1_denom, x2_denom = denom/x1_gcd, denom/x2_gcd
                gcf = gcd(a, b, c)*a/abs(a)

                sign1 = get_sign(x1_numer)
                sign2 = get_sign(x2_numer)
                x1_numer = flip_sign_if_negative(x1_numer, sign1)
                x2_numer = flip_sign_if_negative(x2_numer, sign2)

                return "{}({}x{}{})({}x{}{})".format(float_to_int(gcf) if gcf != 1 else "", fraction(x1_denom), sign1, fraction(x1_numer), fraction(x2_denom), sign2, fraction(x2_numer))

    else: # no factored form
        return None 


while True:
    completing_the_square = False
    a = float(input("insert a: "))
    b = float(input("insert b: "))
    c = float(input("insert c: "))
    factored_form = factor_quadratic_equation(a, b, c)
    solutions = solve_quadratic_equation(a, b, c)

    print(factored_form) if factored_form else print("No Factored Form")

    if solutions:
        if completing_the_square:
            solution0_fraction, solution1_fraction \
                = format_complete_the_square_solutions(*solve_completing_the_square(a, b, c))

        else:
            solution0_fraction = "" if solutions[0].is_integer() else fraction(solutions[0])
            solution1_fraction = "" if solutions[1].is_integer() else fraction(solutions[1])

        solution1 = "x1 = {}".format(round(solutions[0], 5)) if solution0_fraction == "" else "x1 = {} or {}".format(round(solutions[0], 5), solution0_fraction)
        solution2 = "x2 = {}".format(round(solutions[1], 5)) if solution1_fraction == "" else "x2 = {} or {}".format(round(solutions[1], 5), solution1_fraction)

        print(solution1)
        print(solution2) if solutions[0] != solutions[1] else None

    else:
        print("No Solution")

    stop = input("'x' to stop: ")
    if stop == 'x':
        break
         



    






