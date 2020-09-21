# quadratic factorer, and solver
from math import sqrt, log10, pow

def filter(func, iterable):
    """
    reimplementing the filter function, since its not in micropython
    """
    l = []
    for val in iterable:
        if func(val):
            l.append(val)
    return l


def float_scale(x, max_digits=14):
    """
    finds the precision of the float
    """
    int_part = int(abs(x))
    magnitude = 1 if int_part == 0 else int(log10(int_part)) + 1
    if magnitude >= max_digits: 
        return 0
    frac_part = abs(x) - int_part
    multiplier = 10 ** (max_digits - magnitude)
    frac_digits = multiplier + int(multiplier * frac_part + 0.5)
    while frac_digits % 10 == 0:
        frac_digits /= 10
    return int(log10(frac_digits))


def gcd(a, b):
    """
    greatest common divisor, works with floats too.
    """
    gcd_ = lambda a, b: a if b == 0 else gcd_(b, a%b)
    sc = float_scale(a)
    sc_b = float_scale(b)
    sc = sc_b if sc_b > sc else sc
    fac = pow(10, sc)

    a = int(round(a*fac))
    b = int(round(b*fac))

    return abs(round(gcd_(a, b)/fac, sc))
    

def is_integer(n):
    """
    checks if the float given is an integer
    True - float can be an integer
    False - float cannot be an integer
    """
    return int(n) == n
    

def is_close(a, b, tolerance):
    """
    checks whether the difference between the two values are smaller or equal to the tolerance
    returns True, or False
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
        if is_close(a*factor, a_rounded, tolerance):
            break
    if factor == 1:
        return a_rounded
    else:
        return "{}/{}".format(a_rounded, factor)


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


def solve_and_format_completing_the_square(a, b, c): 
    """
    ( x +- ysqrt(B) )/z
    acquires the values of x, y, B, and z by reverse engineering the solutions
    and returns them

    h = (y, B) --> ysqrt(B)
    acquires the x, h, and z 
    and formats a proper string representation for the solution using complete the square

    if z is 1
    then no '/1' is shown.
    """
    f = simplify_sqrt(get_determinant(a, b, c))
    g = gcd(gcd(f[0], 2*a), -b)
    # x, y, B, z
    x, h, z = -b/g, [int(f[0]/g), f[1]], (2*a)/g # x, (h[0], h[1]), z

    # ( x +- h[0]sqrt(h[1]) )/z
    h[0] = 0 if h[0] == 1 else h[0]
    h = format_tuple_to_sqrt(*h)
    if z < 0:
        x, z = -x, -z

    sol1 = "( {} + {} )/{}".format(int(x), h, int(z))
    sol2 = "( {} - {} )/{}".format(int(x), h, int(z))
    if z == 1:
        return sol1[:-2], sol2[:-2]
    return sol1, sol2


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
    if a != 0: # Quadratic
        if get_determinant(a, b, c) >= 0:
            return ( (-b+sqrt(get_determinant(a, b, c))) / (2*a), \
                     (-b-sqrt(get_determinant(a, b, c))) / (2*a) ) # (x1, x2)
        # no solutions
        else:
            return None, None
    else: # Linear
        return -c/b, None


def format_solutions(solutions, completing_the_square):   
    """
    formats the solutions, depending on the solutions and complete the square.
    """
    solution1_fraction = None
    solution2_fraction = None
    if solutions[0] or solutions[1]:
        if completing_the_square:
            solution1_fraction, solution2_fraction \
                = solve_and_format_completing_the_square(a, b, c)

        else:
            if not is_integer(solutions[0]): solution1_fraction = fraction(solutions[0])
            if solutions[1] is not None:
                if not is_integer(solutions[1]): solution2_fraction = fraction(solutions[1])

        solution = "x{} = {}".format(1, round(solutions[0], 5))
        if solution1_fraction:
            solution += " or\n{}".format(solution1_fraction)
        
        if solutions[0] != solutions[1] and solutions[1] is not None:
            
            solution += "\nx{} = {}".format(2, round(solutions[1], 5))
            if solution2_fraction:
                solution += " or\n{}".format(solution2_fraction)

        return solution

    else:
        return "No Solution"


def check_complete_the_square(x1, x2, x1_numer, x2_numer, denom):
    """
    returns True, if the function is a complete the square type of expression
    returns False, if it is factorable with the normal method
    """
    first_check = not (x1 and x2)
    if first_check:
        return True
    second_check = not (is_integer(x1_numer) and is_integer(x2_numer))
    if second_check:
        return True
    third_check = not is_integer(denom)
    if third_check:
        return True
    return False
    

def factor_quadratic_equation(a, b, c):
    """
    factors the quadratic polynomial a, b, c on multiple conditions
    support when
    1) c = 0
    2) b = 0 (if perfect square)
    3) a, b, c present
    4) complete the square is involved
    5) a = 0, so linear expression

    returns a factored form, and a Boolean Value representing whether completing the square was used.
    """
    get_sign = lambda x: "+" if x > 0 else "-" # set the sign based on x's value
    float_to_int = lambda x: int(x) if is_integer(x) else x # only if the float is actually an integer like 3.0

    orig_a, orig_b, orig_c = a, b, c
    if a == 0: # Linear equation 2x+6
        gcf = gcd(b, c)
        b, c = b/gcf, c/gcf
        if gcf == 1:
            return "No Factored Form", False
        return "{}({}x+{})".format(gcf, b, c), False

    if a < 0: # make the value of a positive
        a, b, c = -a, -b, -c

    gcf = None
    # checks if any of the values, are a float, if they are, then they are turned into whole numbers, and the gcf is stored.
    if any(filter(lambda x: not is_integer(x), [a, b, c])):
        gcf = gcd(gcd(a, b), c)
        a, b, c = a/gcf, b/gcf, c/gcf

    if c == 0: 
    # factor by gcf 6x^2 - 2x
        if not gcf:
            gcf = float_to_int(gcd(a, b))
            a, b = a/gcf, b/gcf
        if gcf == 1: gcf = ""

        return "{}x({}x{}{})".format(gcf, fraction(a), get_sign(b), fraction(abs(b))), False

    else: 
        denom = 2*a
        x1, x2 = solve_quadratic_equation(a, b, c)
        if x1 or x2: 
            x1_numer, x2_numer = x1*denom, x2*denom
        else: 
            x1_numer = x2_numer = None

        if check_complete_the_square(x1, x2, x1_numer, x2_numer, denom): 
        # factor by completing the square (x+p)^2 + q
            if a != 1:
                a, b, c = a/a, b/a, c/a

            p = b/(2*a)
            q = c - (b**2)/(4*a)
            return "(x{}{})^2 {} {}\nvertex: ({}, {})".format(get_sign(p), fraction(abs(p)), \
                    get_sign(q), fraction(abs(q)), fraction(-orig_b/(2*orig_a)), fraction(orig_c-((orig_b**2)/(4*orig_a)))), True

        else: 
        # normal factoring a(x+b)(x+c)
            x1_gcd, x2_gcd = gcd(x1_numer, denom), gcd(x2_numer, denom)
            x1_numer, x2_numer = -x1_numer/x1_gcd, -x2_numer/x2_gcd
            x1_denom, x2_denom = denom/x1_gcd, denom/x2_gcd
            if not gcf:
                gcf = float_to_int(gcd(gcd(a, b), c)*a/abs(a))

            if gcf == 1: gcf = ""

            if x1_denom == 1: x1_denom = ""
            else:             x1_denom = fraction(x1_denom)
            if x2_denom == 1: x2_denom = ""
            else:             x2_denom = fraction(x2_denom)

            return "{}({}x{}{})({}x{}{})".format\
            (gcf, x1_denom, get_sign(x1_numer), fraction(abs(x1_numer)) \
            , x2_denom, get_sign(x2_numer), fraction(abs(x2_numer))), False


while True:
    a = float(input("insert a: "))
    b = float(input("insert b: "))
    c = float(input("insert c: "))
    factored_form, completing_the_square = factor_quadratic_equation(a, b, c)
    solutions = solve_quadratic_equation(a, b, c)

    print(factored_form)
    print(format_solutions(solutions, completing_the_square))    

    stop = input("'x' to stop: ")
    if stop == 'x': break
         



    






