print("Factorial Calculator: ")
term = []

# loops through the terms to print them
def term_list_looper(num):
    for i in range(num):
        print(term[i])

# finds the factorial of a certain number (!)
def factorial(num):
    result = 1
    if type(num) == str:
        num = int(eval(num))
    else:
        pass

    for i in range(1, num+1):
        result *= i
    return result

# find the combination of a nth and r  (nCr)
def combination(nth, rth):
    coefficient = (factorial(nth) / (factorial(rth) * factorial(nth - rth)))
    return coefficient

# finds a certain entry of the pascal's triangle using rows and columns 
def pascal_triangle_c_entry(nth, rth):
    coefficient = (factorial(nth-1)/(factorial(rth-1)*factorial((nth-1)-(rth-1))))
    return int(coefficient)

# finds the working and and coefficent of a term in (a+bx)^n
def binomial_term_coefficient_finder(nth, rth, a, b_coefficient, output):
    diff_nth_rth = nth - rth
    comb = combination(nth, rth)
    a_result = a**diff_nth_rth
    b_result = b_coefficient**rth
    resultant_coefficient = comb * a_result * b_result
    group = str("("+str(nth)+"C"+str(rth)+") ("+str(a)+")^"+str(diff_nth_rth)+" ("+str(b_coefficient)+"x)^"+str(rth))
    if output == 0:
        return group
    elif output == 1:
        print("work: ("+str(nth)+"C"+str(rth)+") ("+str(a)+")^"+str(diff_nth_rth)+" ("+str(b_coefficient)+"x)^"+str(rth))
        print("Coefficient of x^"+str(rth)+"\n:", resultant_coefficient)
    elif output == 2:
        if rth == 0:
            return resultant_coefficient
        else:
            return ("("+str(resultant_coefficient)+")"+'x^'+str(rth))
    

# finds the unsimplified form of (a + bx)^n
def first_count_terms(nth, count, a, b_coefficient):
    for r in range(count):
        term.insert(r, binomial_term_coefficient_finder(nth, r, a, b_coefficient, 0))
    print(str(count)+" Terms are:")
    term_list_looper(count)

# finds all the coeffients from when x is to the power 0 to n
def first_terms_with_coefficients(nth, count, a, b_coefficient):
    terms = []
    terms = [binomial_term_coefficient_finder(nth, rth, a, b_coefficient, 2) for rth in range(count)]
    print(terms)

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

while True:
    print("Choose a for Pas_Tri entry(C)\nChoose b for term coefficient finder\nChoose c for first nth terms\nChoose d for c but with coeff")
    choice = input(">> ")
    while choice != "a" or choice != "b" or choice != "c" or choice != "d":
        if choice == "a":
            nth = int(input("Enter nth: "))
            rth = int(input("Enter rth: "))
            print(pascal_triangle_c_entry(nth, rth))

        elif choice == "b":
            nth = int(input("Enter nth: "))
            rth = int(input("Enter rth: "))
            a = int(input("Enter a: "))
            b_coefficient = input("Enter b's coeff: ")
            if type(b_coefficient) == str:
                b_coefficient = eval(b_coefficient)
            binomial_term_coefficient_finder(nth, rth, a, b_coefficient, 1)

        elif choice == "c":
            nth = int(input("Enter nth: "))
            count = int(input("Enter first nth term num: "))
            a = int(input("Enter a: "))
            b_coefficient = input("Enter b's coeff: ")
            if type(b_coefficient) == str:
                b_coefficient = eval(b_coefficient)
            first_count_terms(nth, count, a, b_coefficient)

        elif choice == "d":
            nth = int(input("Enter nth: "))
            count = int(input("Enter first nth term num: "))
            a = int(input("Enter a: "))
            b_coefficient = input("Enter b's coeff: ")
            if type(b_coefficient) == str:
                b_coefficient = eval(b_coefficient)
            first_terms_with_coefficients(nth, count, a, b_coefficient)
             
        stopper()
        print("Choose a for Pas_Tri entry(C)\nChoose b for term coefficient finder\nChoose c for first nth terms\nChoose d for c but with coeff")
        choice = input(">> ")
   