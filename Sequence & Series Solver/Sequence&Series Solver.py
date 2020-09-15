from math import sqrt, log


def take_inputs(*args):
    """
    takes a list of variable names, and sets it up so that that input is carried out, and
    a list is returned with the numerical values, to be used for unpacking into their variables

    Ex:
        take_inputs('a', 'b', 'c')
        a = 4
        b = 2
        c = 3
        - [4, 2, 3] -

    """
    values = []
    for prompt in args:
        values.append(eval(str(input(prompt + " = "))))
    return values


def check_for_L():
    """
    checks if an 'x' was inputted at L.

    if 'x', then return None (L wasn't inputted)
    if any other value, then return the float form of that value
    Ex:
        check_for_L()
        Enter x if L not present!
        Enter L: 5
        - 5.0 -

    """
    L = input("Enter x if L not present!\nEnter L: ")
    return None if L == 'x' else float(L)


class Arithmetic:

    def a_nth(self):
        print("An = a1 + (n-1)d")
        a1, n, d = take_inputs('a1', 'n', 'd')
        print(round(a1 + (n - 1) * d, 5))


    def sum(self):
        print("Sn = n/2(2a1+(n-1)d)", "Sn = n/2(a1+L)", sep="\n")
        L = check_for_L()
        if not L:
            a1, n, d = take_inputs('a1', 'n', 'd')
            print(round((n/2) * (2 * a1 + (n - 1) * d), 5))

        else:
            a1, n = take_inputs('a1', 'n')
            print(round((n/2) * (a1 + L), 5))


    def exceed_nth(self):
        print("a+(n-1)d > Value")
        a1, d, value = take_inputs('a1', 'd', 'value')
        n = round(( (value - a1) / d ) + 1, 5)
        print("n to exceed = " + str(n))


    def exceed_sum_to_nth(self):
        print("n/2(2a1+(n-1)d)>Value", "n/2(a1+L)>Value", sep="\n")
        L = check_for_L()
        if L:
            a1, value = take_inputs('a1', 'value')
            n = round((2 * value) / (a1 + L), 5)
            print("n to exceed = " + str(n))

        else:
            a1, d, value = take_inputs('a1', 'd', 'value')
            n = round((-2*a1 + d + sqrt(4*(a1**2) - 4*a1*d + d**2 + 8*d*value))/(2*d), 5)
            print("n to exceed = " + str(n))



class Geometric:

    def a_nth(self):
        print("An = ar^(n-1)")
        a1, r, n = take_inputs('a1', 'r', 'n')
        print(round(a1 * r ** (n - 1), 5))


    def sum(self):
        print("Sn = a(1-r^n)/(1-r)")
        a1, r, n = take_inputs('a1', 'r', 'n')
        print( round((a1 * (1 - r**n) )/(1 - r), 5))


    def sum_to_infinity(self):
        print("S(inf) = a/(1-r)")
        a1, r = take_inputs('a1', 'r')
        print(round(a1/(1-r), 5))


    def exceed_nth(self):
        print("ar^(n-1) > Value")
        a1, r, value = take_inputs('a1', 'r', 'value')
        n = round(log( r*(value/a1) ) / log(r), 5)
        print("n to exceed = " + str(n))


    def exceed_sum_to_nth(self):
        print("a(1-r^n)/(1-r)>Value")
        a1, r, value = take_inputs('a1', 'r', 'value')
        n = round(log( (a1 + r*value - value) / a1) / log(r), 5)
        print("n to exceed = " + str(n))



class BIOS:

    choices_prompt = "a for arithmetic\nb for geometric\n>> "

    def __init__(self):
        """
        responsible for handling basic input and output, for the terminal, and options/choices.
        """
        self.running = True
        self.arithmetic = Arithmetic()
        self.geometric = Geometric()

        self.choices = {'a': self.arithmetic_sequences, 'b': self.geometric_sequences}
        self.arithmetic_choices        = {'a': self.arithmetic.a_nth, 'b': self.arithmetic.sum, 'c': self.arithmetic_exceed}
        self.geometric_choices         = {'a': self.geometric.a_nth, 'b': self.geometric.sum, 'c': self.geometric.sum_to_infinity, 'd': self.geometric_exceed}
        self.arithmetic_exceed_choices = {'a': self.arithmetic.exceed_nth, 'b': self.arithmetic.exceed_sum_to_nth}
        self.geometric_exceed_choices = {'a': self.geometric.exceed_nth, 'b': self.geometric.exceed_sum_to_nth}


    @staticmethod
    def menu(*args):
        """
        a list of prompts is given as arguments,
        and a menu like input system is made.

        Ex:
            menu('a for apple', 'b for bye', 'c for cat')
            a for apple
            b for bye
            c for cat
            >> a
            - a -
        """
        return input("\n".join(list(args) + [">> "]))


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


    @stop_decorator
    def arithmetic_sequences(self):
        sub_choice = self.menu("Arithmetic:", "a for a_nth term", "b for sum", "c for min_term_exceed")
        self.arithmetic_choices.get(sub_choice, lambda: None)()


    @stop_decorator
    def geometric_sequences(self):
        sub_choice = self.menu("Geometric:", "a for a_nth term", "b for sum", "c for sum to infinity", "d for min terms exceed")
        self.geometric_choices.get(sub_choice, lambda: None)()


    def arithmetic_exceed(self):
        sub_choice = self.menu("Exceed Arithmetic:", "a for nth", "b for sum_to_nth")
        self.arithmetic_exceed_choices.get(sub_choice, lambda: None)()


    def geometric_exceed(self):
        sub_choice = self.menu("Exceed Geometric:", "a for nth", "b for sum_to_nth")
        self.geometric_exceed_choices.get(sub_choice, lambda: None)()


    def main(self):
        """
        runs the program indefinitely as long as the user wants.
        """
        while self.running:
            self.choices.get(input(self.choices_prompt), lambda: None)()
            print()


program = BIOS()
program.main()