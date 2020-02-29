print("Factorial Calculator: ")

# finds the factorial of a certain number (!)
def factorial(num, end_point=1):
    # eval() evaluates an expression like "5/7" incase input is a fraction
    if type(num) == str:
        num = int(eval(num))
    else:
        pass

    result = 1
    for i in range(end_point, num+1):
        result *= i
    return result

# find the combination of a nth and r  (nCr)
def combination(nth, rth):
    coefficient = factorial(nth, nth-rth+1) // factorial(rth)
    return coefficient

# finds a certain entry of the pascal's triangle using rows and columns 
def pascal_triangle_c_entry(nth, rth):
    return int(combination(nth-1, rth-1))

# finds the working and and coefficent of a term in (a+bx)^n
def binomial_term_coefficient_finder(nth, rth, a, b_coefficient, output):
    diff_nth_rth = nth - rth
    resultant_coefficient = combination(nth, rth) * (a**diff_nth_rth) * (b_coefficient**rth)
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
    term = [binomial_term_coefficient_finder(nth, rth, a, b_coefficient, 0) for rth in range(count)]
    print(str(count)+" Terms are:")
    for i in range(count):
        print(term[i])
    

# finds all the coeffients from when x is to the power 0 to n
def first_terms_with_coefficients(nth, count, a, b_coefficient):
    terms = [binomial_term_coefficient_finder(nth, rth, a, b_coefficient, 2) for rth in range(count)]
    print(terms)

# as this code is for a calculator the a is very close to your finger so after you find your desired result
# you enter a to stop and anything else will restart it
def stopper():
    stop_or_continue = input("Stop?: ")
    if stop_or_continue == "a":
        raise SystemExit    

while True:
    choice = 'x'
    while choice in ['a', 'b', 'c', 'd', 'x']:
        print("Choose a for Pas_Tri entry(C)\nChoose b for term coefficient finder\nChoose c for first nth terms\nChoose d for c but with coeff")
        choice = input(">> ")
        if choice == "a":
            nth = int(input("Enter row number(n): "))
            rth = int(input("Enter entry number(r): "))
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
        
        else:
            print("unknown letter\n please try again!")
             
        stopper()
        choice = 'x'
   
