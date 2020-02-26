# just to make the input_checker function smaller and to eliminate repeated code
def three_variables_looper_arithmetic():
    a = input("enter a1: ")
    b = input("enter n: ")
    c = input("enter d: ")
    original = 0
    count_list = [[a], [b], [c]]
    loop = 0
    for count in count_list:
        if isinstance(count[0], str):
            original = float(eval(count[0]))
            count_list[loop][0] = original
        loop += 1
    return count_list[0][0], count_list[1][0], count_list[2][0]

# just to make the input_checker function smaller and to eliminate repeated code
def three_variables_looper_geometric():
    a = input("enter a1: ")
    b = input("enter r: ")
    c = input("enter n: ")
    original = 0
    count_list = [[a], [b], [c]]
    loop = 0
    for count in count_list:
        if isinstance(count[0], str):
            original = float(eval(count[0]))
            count_list[loop][0] = original
        loop += 1
    return count_list[0][0], count_list[1][0], count_list[2][0]


# loops through all the inputs of a given situation based on whether its arithmetic
# or not, and checks whether the input is string like "6/2" so it could evaluate it, allows input of fractions
def input_checker(arithmetic_1_geometric_2, formula_num, L):
    if arithmetic_1_geometric_2 == 1:
        if formula_num == 1:
            return three_variables_looper_arithmetic()


        elif formula_num == 2:
            return three_variables_looper_arithmetic()

        elif formula_num == 3:
            a1 = input("enter a1: ")
            b = input("enter n: ")
            c = input("enter d: ")
            original = 0
            count_list = [[a1], [b], [c], [L]]
            loop = 0
            for count in count_list:
                if isinstance(count[0], str):
                    original = float(eval(count[0]))
                    count_list[loop][0] = original
            return count_list[0][0], count_list[1][0], count_list[2][0], count_list[3][0]
            
    elif arithmetic_1_geometric_2 == 2:
        if formula_num == 1:
            return three_variables_looper_geometric()
        
        elif formula_num == 2:
            return three_variables_looper_geometric()

        elif formula_num == 3:
            a1 = input("enter a1: ")
            b = input("enter n: ")
            original = 0
            count_list = [[a1], [b]]
            loop = 0
            for count in count_list:
                if isinstance(count[0], str):
                    original = float(eval(count[0]))
                    count_list[loop][0] = original
            return count_list[0][0], count_list[1][0]

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
    choice = ""
    choices = ["a", "b"]
    while choice not in choices:
        choice = input("a for arithmetic\nb for geometric\n>> ")

    if choice == "a":
        arithmetic_1_geometric_2 = 1
        choice_2 = input("a for a_nth term\nb for sum\n>> ")

        # the variable arithmetic_1_geometric_2 refers to whether the inputs are for arithmetic hence it is 1, or the inputs
        # are for geometric hence 2
        # formula_num refers to the types of formulas you'll use in sequences/series
        if choice_2 == "a":
            print("a_nth=a1+(n-1)d")
            formula_num = 1
            a1, n, d = input_checker(arithmetic_1_geometric_2, formula_num, 0)
            result = a1+(n-1)*d
            print(result)

        elif choice_2 == "b":
            print("Sn=(n/2)(2a1+(n-1)d)\nSn=(n/2)(a1+L)\nEnter x if L is unknown")
            L = input("Enter L: ")
            if L == "x":
                formula_num = 2
                a1, n, d = input_checker(arithmetic_1_geometric_2, formula_num, L)
                result = (n/2)*(2*a1+(n-1)*d)
                print(result)
            else:
                formula_num = 3
                a1, n, d, L = input_checker(arithmetic_1_geometric_2, formula_num, L)
                result = (n/2)*(a1+L)
                print(result)
    
    elif choice == "b":
        arithmetic_1_geometric_2 = 2
        choice_2 = input("a for a_nth term\nb for sum\nc for sum_to_inf")

        if choice_2 == "a":
            print("a_nth=a1(r)^(n-1)")
            formula_num = 1
            a1, r, n = input_checker(arithmetic_1_geometric_2, formula_num, 0)
            result = a1*(r)**(n-1)
            print(result)

        elif choice_2 == "b":
            print("Sn=(a1(1-(r)^n))/(1-r)")
            formula_num = 2
            a1, r, n = input_checker(arithmetic_1_geometric_2, formula_num, 0)
            result = (a1(1-(r)**n))/(1-r)
            print(result)

        elif choice_2 == "c":
            print("S_inf=a1/(1/r)")
            formula_num = 3
            a1, r = input_checker(arithmetic_1_geometric_2, formula_num, 0)
            result = a1/(1-r)
            print(result)
    
    stopper()