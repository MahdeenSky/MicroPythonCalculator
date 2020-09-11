def seperate_to_pairs(iterator):
    """
    changes it so that each item in the list pairs with its neighbor items.
    Ex:
        [1, 2, 1]       ---> [[1, 2], [2, 1]]
        [1, 2, 3, 1]    ---> [[1, 2], [2, 3], [3, 1]]
        [1, 2, 3, 2, 1] ---> [[1, 2], [2, 3], [3, 2], [2, 1]]
    """
    return [iterator[i:i+2] for i in range(0, len(iterator)-1)]


def factorial(n, endpoint=1):
    """
    acquires the factorial of n
    """
    res = 1
    for i in range(endpoint, n+1):
        res *= i
    return res


def combinations(nth, rth):
    """
    nCr - combination or number of ways of picking r items from n

    OR

    nCr = n!/r!(n-r)!
    """
    return (factorial(nth, nth-rth+1) // factorial(rth))


def pascal_triangle_entry(nth, rth):
    """
    acquires the entry in the pascal's triangle at the nth row and rth term
    """
    return combinations(nth-1, rth-1)


def pascal_triangle_level(level):
    """
    acquires an entire row in the pascal triangle designated by the level number, where 0 is [1], and 1 is [1, 1]
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
    """
    terms = []
    coefficients = pascal_triangle_level(n)[1:-1]

    for r, coefficient in zip(range(1, len(coefficients)+1), coefficients):
        terms.append("[{}] ({})^({}) ({})^({})".format(coefficient, a, n-r, b, r))
    return ["({})^{}".format(a, n)] + terms + ["({})^{}".format(b, n)]


def binomial_term_finder(a, b, n, r):
    """
    calculates the coefficient of the rth term in (a + b)^n
    """
    return combinations(n, r) * a**(n - r) * b**r


def first_rth_terms(a, b, n, rth):
    """
    calculates the coefficients for the first rth terms in (a + b)^n
    """
    return [binomial_term_finder(a, b, n, r) for r in range(rth)]


class BIOS:
    """
    responsible for input and output operations
    Hence called BIOS - Basic Input and Output System
    """

    prompt = "\n".join(["a: pascal tri. entry", "b: pascal tri. row", "c: binomial expand", "d: binomial term finder", "e: first rth terms", "f: combinations"])

    def __init__(self):
        self.choices = {'a': self.pascal_triangle_entry, 'b': self.pascal_triangle_level, 'c': self.binomial_expand, 'd': self.binomial_term_finder, 'e': self.first_rth_terms, 'f': self.combinations}

    def pascal_triangle_entry(self):
        nth = int(input("Enter row number(n): "))
        rth = int(input("Enter entry number(r): "))
        print(pascal_triangle_entry(nth, rth))


    def pascal_triangle_level(self):
        level = int(input("Enter level: "))
        print(pascal_triangle_level(level))


    def binomial_expand(self):
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        nth = int(input("Enter nth: "))
        print(binomial_expand(a, b, nth))


    def binomial_term_finder(self):
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        nth = int(input("Enter nth: "))
        rth = int(input("Enter rth: "))
        print(binomial_term_finder(a, b, nth, rth))


    def first_rth_terms(self):
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        nth = int(input("Enter nth: "))
        rth = int(input("Enter first rth terms: "))
        print("First {} terms:".format(rth))
        print(first_rth_terms(a, b, nth, rth))


    def combinations(self):
        nth = int(input("Enter nth: "))
        rth = int(input("Enter rth: "))
        print(combinations(nth, rth))


    def main(self):
        while True:
            print(self.prompt)
            self.choices.get(input(">> "), lambda: None)()
            command = input("Enter nothing to stop: ")
            if command == '':
                break


program = BIOS()
program.main()

