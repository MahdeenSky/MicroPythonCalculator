# just to make the input_checker function smaller and to eliminate repeated code, responsible for iterating through a list of inputs
def three_variables_looper_arithmetic():
    count_list = [input("enter a1: "), input("enter n: "), input("enter d: ")]
    count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
    return count_list

# just to make the input_checker function smaller and to eliminate repeated code, responsible for iterating through a list of inputs
def three_variables_looper_geometric():
    count_list = [input("enter a1: "), input("enter r: "), input("enter n: ")]
    count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
    return count_list


# loops through all the inputs of a given situation based on whether its arithmetic
# or not, and checks whether the input is string like "6/2" so it could evaluate it, allows input of fractions
def input_checker(choice_main, choice_sub, L):
    if choice_main == 'arithmetic':
        if choice_sub == 'a_nth':
            return three_variables_looper_arithmetic()

        elif choice_sub == 'sum_to_nth_without_L':
            return three_variables_looper_arithmetic()

        elif choice_sub == 'sum_to_nth_with_L':
            count_list = [input("enter a1: "), input("enter n: "), L]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

        elif choice_sub == "a_nth_exceed":
            count_list = [input("enter a1: "), input("enter r/d: ")]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

        elif choice_sub == "sum_to_nth_without_L_exceed":
            count_list = [input("enter a1: "), input("enter r/d: ")]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

        elif choice_sub == "sum_to_nth_with_L_exceed":
            count_list = [input("enter a1: "), L]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list


    elif choice_main == 'geometric':
        if choice_sub == 'a_nth':
            return three_variables_looper_geometric()
        
        elif choice_sub == 'sum_to_nth':
            return three_variables_looper_geometric()

        elif choice_sub == 'sum_to_infinity':
            count_list = [input("enter a1: "), input("enter r: ")]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

        elif choice_sub == "a_nth_exceed":
            count_list = [input("enter a1: "), input("enter r/d: ")]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

        elif choice_sub == "sum_to_nth_without_L_exceed":
            count_list = [input("enter a1: "), input("enter r/d: ")]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

def L_evaluator(L, option, choice_n, value):
    if option == "normal":
        if L == "x":
                    a1, n, d = input_checker(choice_main, choice_n, L)
                    result = (n/2)*(2*a1+(n-1)*d)
                    return result
        else:
                    choice_n = choice_map_sub['x']
                    a1, n, L = input_checker(choice_main, choice_n, L)
                    result = (n/2)*(a1+L)
                    return result
   
    if option == "exceed":
        if L == "x":
                    a1, d = input_checker(choice_main, choice_n, 0)
                    a1, d = float(a1), float(d)
                    n = 1
                    while True:
                        result = (n/2)*(2*a1+(n-1)*d)
                        if (result >= float(value)):
                            break
                        n += 1
                    return n
        else:
                    choice_n = choice_map_exceed['c']
                    a1, L = input_checker(choice_main, choice_n, L)
                    n = 1
                    while True:
                        result = (n/2)*(a1+L)
                        if (result >= float(value)):
                            break
                        n += 1
                    return n


def minimum_n_finder(choice_main, choice_map_exceed):
    choice_n_input = None
    if choice_main == "arithmetic":
        while choice_n_input not in ['a', 'b']:
            choice_n_input = input("Enter a for nth\nEnter b for sum\n>> ")
        choice_n = choice_map_exceed[choice_n_input]
        print("enter x in n")

        if choice_n == "a_nth_exceed":
            print("a1+(n-1)d > Value")
            a1, d = input_checker(choice_main, choice_n, 0)
            n = 1
            value = input("Enter the value to exceed: ")
            while True:
                result = a1+(n-1)*d
                if (result >= float(value)):
                    break
                n += 1
            print("The minimum n to exceed is " + str(n))

        if choice_n == "sum_to_nth_without_L_exceed":
            n = 1
            print("Sn=(n/2)(2a1+(n-1)d)>Value\nSn=(n/2)(a1+L)>Value\nEnter x if L is unknown")
            L = input("Enter L: ")
            value = input("Enter the value to exceed: ")
            result = L_evaluator(L, "exceed", choice_n, value)
            print("The minimum n to exceed is " + str(result))



    elif choice_main == 'geometric':

        while choice_n_input not in ['a', 'b']:
            choice_n_input = input("Enter a for nth\nEnter b for sum_to_nth\n>> ")
        choice_n = choice_map_exceed[choice_n_input]

        if choice_n == "a_nth_exceed":
            print("a1(r)^(n-1)>Value")
            a1, r = input_checker(choice_main, choice_n, 0)
            if a1 == 0:
                print("a cannot be 0")
                raise SystemExit
            n = 1
            value = input("Enter the value to exceed: ")
            while True:
                result = a1*(r)**(n-1)
                if (result >= float(value)):
                    break
                n += 1
            print("The minimum n to exceed is " + str(n))

        elif choice_n == "sum_to_nth_without_L_exceed":
            print("Sn=(a1(1-(r)^n))/(1-r)")
            a1, r = input_checker(choice_main, choice_n, 0)
            if a1 == 0:
                print("a cannot be 0")
                raise SystemExit
            n = 1
            value = input("Enter the value to exceed: ")
            while True:
                result = (a1*(1-(r)**n))/(1-r)
                if (result >= float(value)):
                    break
                n += 1
            print("The minimum n to exceed is " + str(n))


# as this code is for a calculator the a and b buttons are right beside each other, so after you find your desired result
# you enter a to stop and b to continue 
def stopper():
    stop_or_continue = input("Stop?: enter x then\n>>>  ")
    if stop_or_continue == "x":
        raise SystemExit  

print("Sequence & Series Solver")

# asks whether you want to solve arithmetically or geometrically, depends on the sequence/series
while True:
    choice_main , choice_input_main = None, None
    choices_main_options = ['a','b']
    choice_map_main ={"a": 'arithmetic', "b": 'geometric'}
    while choice_input_main not in choices_main_options:
        choice_input_main = input("a for arithmetic\nb for geometric\n>> ")
    choice_main = choice_map_main[choice_input_main]

    if choice_main == "arithmetic":
        print("Arithmetic: ")
        choice_sub, choice_input_sub = None, None
        choices_sub_options = ['a', 'b', 'c']
        choice_map_sub = {'a': 'a_nth', 'b': 'sum_to_nth_without_L', 'x': 'sum_to_nth_with_L', 'c':'minimum_number_of_terms_to_exceed'}
        while choice_input_sub not in choices_sub_options:
            choice_input_sub = input("a for a_nth term\nb for sum\nc for min_term_to_exceed\n>> ")
        choice_sub = choice_map_sub[choice_input_sub]

        # the variable choice_main refers to whether the choice is arithmetic or geometric
        # choice_sub refers to the types of formulas you'll use in sequences/series
        if choice_sub == "a_nth":
            print("a_nth=a1+(n-1)d")
            a1, n, d = input_checker(choice_main, choice_sub, 0)
            result = a1+(n-1)*d
            print(round(result,4))

        elif choice_sub == "sum_to_nth_without_L":
            print("Sn=(n/2)(2a1+(n-1)d)\nSn=(n/2)(a1+L)\nEnter x if L is unknown")
            L = input("Enter L: ")
            print(round(L_evaluator(L, "normal", choice_sub, 0), 4))

        elif choice_sub == "minimum_number_of_terms_to_exceed":
            choice_map_exceed = {'a': 'a_nth_exceed', 'b': 'sum_to_nth_without_L_exceed', 'c': 'sum_to_nth_with_L_exceed'}
            minimum_n_finder("arithmetic", choice_map_exceed)


    elif choice_main == "geometric":
        print("Geometric: ")
        choice_sub, choice_input_sub = None, None
        choices_sub_options = ['a', 'b', 'c', 'd']
        choice_map_sub = {'a': 'a_nth', 'b': 'sum_to_nth', 'c': 'sum_to_infinity', 'd': 'minimum_number_of_terms_to_exceed'}
        while choice_input_sub not in choices_sub_options:
            choice_input_sub = input("a for a_nth term\nb for sum\nc for sum to infinity\nd for min_terms_exceed\n>> ")
        choice_sub = choice_map_sub[choice_input_sub]

        if choice_sub == "a_nth":
            print("a_nth=a1(r)^(n-1)")
            a1, r, n = input_checker(choice_main, choice_sub, 0)
            result = a1*(r)**(n-1)
            print(round(result,4))

        elif choice_sub == "sum_to_nth":
            print("Sn=(a1(1-(r)^n))/(1-r)")
            a1, r, n = input_checker(choice_main, choice_sub, 0)
            try:
                result = (a1*(1-(r)**n))/(1-r)
                print(round(result,4))
            except (ZeroDivisionError, NameError):
                print("r cannot be 1!")
            
        elif choice_sub == "sum_to_infinity":
            print("S_inf=a1/(1-r)")
            a1, r = input_checker(choice_main, choice_sub, 0)
            if (r > 1):
                print("r cannot be greater than 1")
                raise SystemExit
            try:
                result = a1/(1-r)
                print(round(result,4))
            except (ZeroDivisionError, NameError):
                print("r cannot be 1!")

        elif choice_sub == "minimum_number_of_terms_to_exceed":
            choice_map_exceed = {'a': 'a_nth_exceed', 'b': 'sum_to_nth_without_L_exceed', 'c': 'sum_to_nth_with_L_exceed'}
            minimum_n_finder("geometric", choice_map_exceed)
    
    stopper()