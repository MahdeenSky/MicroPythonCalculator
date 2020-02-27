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
            
    elif choice_main == 'geometric':
        if choice_sub == 'a_nth':
            return three_variables_looper_geometric()
        
        elif choice_sub == 'sum_to_nth':
            return three_variables_looper_geometric()

        elif choice_sub == 'sum_to_infinity':
            count_list = [input("enter a1: "), input("enter r: ")]
            count_list = [float(eval(count)) for count in count_list if isinstance(count, str)]
            return count_list

# as this code is for a calculator the a and b buttons are right beside each other, so after you find your desired result
# you enter a to stop and b to continue 
def stopper():
    stop_flag = False
    stop_or_continue = ""
    while stop_or_continue != "a" or "b":
        stop_or_continue = input("Stop?: ")
        if stop_or_continue == "a":
            stop_flag = True
            break
        if stop_or_continue == "b":
            stop_flag = False
            break
    if stop_flag:
        raise SystemExit


print("Sequence & Series Solver")

# asks whether you want to solve arithmetically or geometrically, depends on the sequence/series
while True:
    choice_main , choice_input_main = None, None
    choices_main = {'a','b'}
    choice_map_main ={"a": 'arithmetic', "b": 'geometric'}
    while choice_input_main not in choices_main:
        choice_input_main = input("a for arithmetic\nb for geometric\n>> ")
        choice_main = choice_map_main[choice_input_main]

    if choice_main == "arithmetic":
        choice_sub, choice_input_sub = None, None
        choices_sub = {'a', 'b'}
        choice_map_sub = {'a': 'a_nth', 'b': 'sum_to_nth_without_L', 'c': 'sum_to_nth_with_L'}
        choice_input_sub = input("a for a_nth term\nb for sum\n>> ")
        choice_sub = choice_map_sub[choice_input_sub]

        # the variable choice_main refers to whether the choice is arithmetic or geometric
        # choice_sub refers to the types of formulas you'll use in sequences/series
        if choice_sub == "a_nth":
            print("a_nth=a1+(n-1)d")
            a1, n, d = input_checker(choice_main, choice_sub, 0)
            result = a1+(n-1)*d
            print(result)

        elif choice_sub == "sum_to_nth_without_L":
            print("Sn=(n/2)(2a1+(n-1)d)\nSn=(n/2)(a1+L)\nEnter x if L is unknown")
            L = input("Enter L: ")
            if L == "x":
                a1, n, d = input_checker(choice_main, choice_sub, L)
                result = (n/2)*(2*a1+(n-1)*d)
                print(result)
            else:
                choice_sub = choice_map_sub['c']
                a1, n, L = input_checker(choice_main, choice_sub, L)
                result = (n/2)*(a1+L)
                print(result)

    elif choice_main == "geometric":
        choice_sub, choice_input_sub = None, None
        choices_sub = {'a', 'b'}
        choice_map_sub = {'a': 'a_nth', 'b': 'sum_to_nth', 'c': 'sum_to_infinity'}
        choice_input_sub = input("a for a_nth term\nb for sum\nc for sum to infinity\n>> ")
        choice_sub = choice_map_sub[choice_input_sub]

        if choice_sub == "a_nth":
            print("a_nth=a1(r)^(n-1)")
            a1, r, n = input_checker(choice_main, choice_sub, 0)
            result = a1*(r)**(n-1)
            print(result)

        elif choice_sub == "sum_to_nth":
            print("Sn=(a1(1-(r)^n))/(1-r)")
            a1, r, n = input_checker(choice_main, choice_sub, 0)
            result = (a1*(1-(r)**n))/(1-r)
            print(result)

        elif choice_sub == "sum_to_infinity":
            print("S_inf=a1/(1-r)")
            a1, r = input_checker(choice_main, choice_sub, 0)
            result = a1/(1-r)
            print(result)
    
    stopper()