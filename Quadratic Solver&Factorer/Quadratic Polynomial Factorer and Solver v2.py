# quadratic factorer, and solver
from math import sqrt


def is_integer(n):
    """
    checks if the float given is an integer
    True - float can be an integer
    False - float is not an integer
    """
    return int(n) == n
    

def gcd(*values):
    """
    finds the greatest common divisor of values
    and returns the absolute value of the divisor
    """
    x, *b = values
    for y in b:
        while y != 0:
            (x, y) = (y, x % y)
    return abs(x)


def isclose(a, b, tolerance):
    """
    checks whether the difference between the two values are smaller or equal to the tolerance
    return True - yes
    return False - no
    """
    return abs(a-b) <= tolerance


def fraction(a, factor=0, tolerance=0.01):
    """
    Uses brute force, to turn a float into a fraction
    if a is a whole number, then it is returned.
    if a is a float, then the closest possible fraction to tolerance level of difference
        and returns a fraction in string format.
    """
    while True:
        factor += 1
        a_rounded = int(round(a*factor))
        if isclose(a*factor, a_rounded, tolerance):
            break
    if factor == 1:
        return a_rounded
    else:
        return "{}/{}".format(a_rounded, factor)


def simplify_fraction(numer, denom):
    """
    simplifies a fraction, to a simpler form
    """
    if denom == 0:
        return None, None
    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)

    return numer // common_divisor, denom // common_divisor


def get_determinant(a, b, c):
    """
    returns the determinant of a polynomial ax^2 + bx + c
    """
    return b**2 - 4*a*c


def factors(n):
    """
    finds the factors of n, and returns a list of factors (unordered)
    """
    return list(set(x for tup in ([i, n//i] 
                for i in range(1, int(sqrt(n))+1) if n % i == 0) for x in tup))


def simplify_sqrt(n):
    """
    simplifies the n in sqrt(n)
    and turns it into a surd

    return values:
    (x, y) --> xsqrt(y)
    - x is the coefficient of the surd
    - y is the value remaining in the sqrt

    (0, y) --> sqrt(y)
    (y, 0) --> y
    """
    perfect_square = None
    float_to_int = lambda x: int(x) if is_integer(x) else x
    for factor in sorted(factors(n), reverse=True)[:-1]:
        if is_integer(sqrt(factor)):
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
    """
    turns a tuple from simplify_sqrt to an actual string representation.
    """
    if A == 0:
        A = ""
    elif B == 0:
        return str(A)
    return "{}sqrt({})".format(A, B)


def solve_completing_the_square(a, b, c): 
    """
    ( x +- ysqrt(B) )/z
    acquires the values of x, y, B, and z by reverse engineering the solutions
    and returns them
    """
    f = simplify_sqrt(get_determinant(a, b, c))
    g = gcd(f[0], 2*a, -b)
    # x, y, B, z
    return -b/g, [int(f[0]/g), f[1]], (2*a)/g # x, (h[0], h[1]), z


def format_complete_the_square_solutions(x, h, z):
    """
    h = (y, B) --> ysqrt(B)
    acquires the x, h, and z 
    and formats a proper string representation for the solution using complete the square

    if z is 1
    then no '/1' is shown.
    """
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
    """
    returns a tuple of solutions, if a polynomial abc, has atleast 1 solution, else returns None
    formula = (-b+-sqrt(b^2-4ac))/2a
    """
    # two solutions, or one solution
    if get_determinant(a, b, c) >= 0:
        return ( (-b+sqrt(get_determinant(a, b, c))) / (2*a), (-b-sqrt(get_determinant(a, b, c))) / (2*a)) # (x1, x2)
    # no solutions
    else:
        return None


def factor_quadratic_equation(a, b, c):
    """
    factors the quadratic polynomial a, b, c on multiple conditions
    support when
    1) c = 0
    2) b = 0 (if perfect square)
    3) a, b, c present
    4) complete the square is involved
    """
    get_sign = lambda x: "+" if x > 0 else "-" # set the sign based on x's value
    flip_sign_if_negative = lambda x, sign: -x if sign == '-' else x # switch the signs for formatting if sign == '-'
    float_to_int = lambda x: int(x) if is_integer(x) else x # only if the float is actually an integer like 3.0

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

            if not (is_integer(x1_numer) and is_integer(x2_numer)) or not is_integer(denom): 
            # factor by completing the square 2(x+3) + 1
            # (x+p)^2 + q
                global completing_the_square
                completing_the_square = True

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
            solution0_fraction = "" if is_integer(solutions[0]) else fraction(solutions[0])
            solution1_fraction = "" if is_integer(solutions[1]) else fraction(solutions[1])

        solution1 = "x1 = {}".format(round(solutions[0], 5)) if solution0_fraction == "" else "x1 = {} or\n{}".format(round(solutions[0], 5), solution0_fraction)
        solution2 = "x2 = {}".format(round(solutions[1], 5)) if solution1_fraction == "" else "x2 = {} or\n{}".format(round(solutions[1], 5), solution1_fraction)

        print(solution1)
        print(solution2) if solutions[0] != solutions[1] else None

    else:
        print("No Solution")

    stop = input("'x' to stop: ")
    if stop == 'x':
        break
         



    






