def float_integer(num):
    """
    returns an integer if the float given, is a whole number.
    otherwise returns the same value as the argument num.

    Ex:
        4.0 ---> 4
        3.5 ---> 3.5
    """
    if num == int(num):
        return int(num)
    return num


def seperate_to_pairs(iterable):
    """
    changes it so that each item in the list pairs with its neighbor items.
    Ex:
        [1, 2, 1]       ---> [[1, 2], [2, 1]]
        [1, 2, 3, 1]    ---> [[1, 2], [2, 3], [3, 1]]
        [1, 2, 3, 2, 1] ---> [[1, 2], [2, 3], [3, 2], [2, 1]]
    """
    iter1 = iter(iterable)   # create 1st iterator
    iter2 = iter(iterable)   # create a 2nd iterator
    next(iter2)              # advance 2nd iterator one position

    return [(a, b) for a, b in zip(iter1, iter2)]

def factorial(n, endpoint=1):
    """
    acquires the factorial of n
    Ex:
        5 ---> 120
    """
    res = 1
    for i in range(endpoint, n+1):
        res *= i
    return res


def combinations(n, r):
    """
    nCr - combination or number of ways of picking r items from n

    OR

    nCr = n!/r!(n-r)!
    Ex:
        4C2 ---> 6
        6C3 ---> 20
    """
    return (factorial(n, n-r+1) // factorial(r))


def pascal_triangle_entry(nth, rth):
    """
    acquires the entry in the pascal's triangle at the nth row and rth term
    Ex:
        4th row, 2nd term ---> 3
    """
    return combinations(nth-1, rth-1)


def pascal_triangle_level(level):
    """
    acquires an entire row in the pascal triangle designated by the level number, where 0 is [1], and 1 is [1, 1]
    Ex:
        5 ---> [1, 5, 10, 10, 5, 1]
        6 ---> [1, 6, 15, 20, 15, 6, 1]
    """
    if level == 0:
        return [1]

    layer = [1, 1]
    for _ in range(level-1):
        current_layer = []
        for pair in seperate_to_pairs(layer):
            current_layer.append(sum(pair))
        layer = [1] + current_layer + [1]
    return layer


def binomial_expand(a, b, n):
    """
    (a + bx)^n = a^n + (nC1) a^(n-1) bx + (nC2) a^(n-2) (bx)^2 + ... + (nCr) a^(n-r) (bx)^r + ... + (bx)^n

    Ex:
        a = 3, b = 2, n = 4 # example values for (3 + 2x)^4
        OUTPUT FORMAT:

        [4C0] --> 81.0
        (3.0)^4
        ...
        [nCr] --> Term_Value
        nCr_value (a)^(n-r) (b)^(r)
        ...
        [4C4] --> 16.0
        (2.0)^4

    """
    terms = []
    coefficients = pascal_triangle_level(n)[1:-1]

    for r, coefficient in zip(range(1, len(coefficients)+1), coefficients):
        term_value = binomial_term_finder(a, b, n, r, coefficient)
        terms.append("[{5}C{4}] --> {6}\n |{0}| ({1})^{2} ({3})^{4}".format(coefficient, a, n-r, b, r, n, term_value))
    return "\n".join(["[{1}C0] --> {2}\n |1| ({0})^{1}".format(a, n, a**n)] + terms + ["[{1}C{1}] --> {2}\n |1| ({0})^{1}".format(b, n, b**n)])


def binomial_term_finder(a, b, n, r, coefficient=None):
    """
    calculates the coefficient of the rth term in (a + bx)^n

    if coefficient is given, it skips calculating it.
    Ex:
        a = 3, b = 2, n = 4, r = 2 # example values for (3 + 2x)^4
        ---> 216

    """
    if coefficient:
        return coefficient * a**(n - r) * b**r
    return combinations(n, r) * a**(n - r) * b**r


def first_rth_terms(a, b, n, rth):
    """
    calculates the coefficients of x for the first rth terms in (a + bx)^n
    Ex:
        a = 3, b = 2, n = 4, rth = 3 # example values for (3 + 2x)^4
        ---> [81, 216, 216]
    """
    return [binomial_term_finder(a, b, n, r) for r in range(rth)]


class BIOS:
    """
    responsible for input and output operations
    Hence called BIOS - Basic Input and Output System
    """

    prompt = "\n".join(["a: pascal tri. entry", "b: pascal tri. row", "c: binomial expand", "d: binomial term finder", "e: first rth terms", "f: combinations"])

    def __init__(self):
        self.running = True
        self.choices = {'a': self.pascal_triangle_entry, 'b': self.pascal_triangle_level, 'c': self.binomial_expand, 'd': self.binomial_term_finder, 'e': self.first_rth_terms, 'f': self.combinations}


    def stop_decorator(func):
        """
        Decorator for stopping certain functions, after they're done by asking with a prompt
        """
        def wrapper(self):
            func(self)
            command = input("Enter nothing to stop: ")
            if command == '':
                self.running = False
        return wrapper


    def INPUT_a_b(self):
        """
        input a and b for (a + bx)^n, using only one line
        """
        return float_integer(float(input("Enter a: "))), float_integer(float(input("Enter b: ")))


    @stop_decorator
    def pascal_triangle_entry(self):
        nth = int(input("Enter row number(n): "))
        rth = int(input("Enter entry number(r): "))
        print(pascal_triangle_entry(nth, rth))


    @stop_decorator
    def pascal_triangle_level(self):
        level = int(input("Enter level: "))
        print(pascal_triangle_level(level))


    def binomial_expand(self):
        a, b = self.INPUT_a_b()
        nth = int(input("Enter nth: "))
        self.running = False
        print(binomial_expand(a, b, nth))
        print(first_rth_terms(a, b, nth, nth+1))


    @stop_decorator
    def binomial_term_finder(self):
        a, b = self.INPUT_a_b()
        nth = int(input("Enter nth: "))
        rth = int(input("Enter rth: "))
        print(binomial_term_finder(a, b, nth, rth))


    @stop_decorator
    def first_rth_terms(self):
        a, b = self.INPUT_a_b()
        nth = int(input("Enter nth: "))
        rth = int(input("Enter first num terms: "))
        print("First {} terms:".format(rth))
        print(first_rth_terms(a, b, nth, rth))


    @stop_decorator
    def combinations(self):
        nth = int(input("Enter nth: "))
        rth = int(input("Enter rth: "))
        print(combinations(nth, rth))


    def main(self):
        """
        main program loop, uses a dictionary as an alternative for a switch case
        """
        while self.running:
            print(self.prompt)
            self.choices.get(input(">> "), lambda: None)()


program = BIOS()
program.main()

