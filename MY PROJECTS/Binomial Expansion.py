print("Factorial Calculator: ")
term = []


def term_list_looper(num):
    for i in range(num):
        print(term[i])


def factorial(num):
    result = 1
    if type(num) == str:
        num = int(eval(num))
    else:
        pass

    for i in range(1, num+1):
        result *= i
    return result


def combination(nth, rth):
    coefficient = (factorial(nth) / (factorial(rth) * factorial(nth - rth)))
    return coefficient


def pascal_triangle_c_entry(nth, rth):
    coefficient = (factorial(nth-1)/(factorial(rth-1)*factorial((nth-1)-(rth-1))))
    return int(coefficient)


def binomial_term_coefficient_finder(nth, rth, a, b_coefficient, output):
    diff_nth_rth = nth - rth
    comb = combination(nth, rth)
    a_result = a**diff_nth_rth
    b_result = b_coefficient**rth
    resultant_coefficient = comb * a_result * b_result
    group = str("("+str(nth)+"/"+str(rth)+") ("+str(a)+")^"+str(diff_nth_rth)+" ("+str(b_coefficient)+"x)^"+str(rth))
    if output is True:
        print("work: ("+str(nth)+"/"+str(rth)+") ("+str(a)+")^"+str(diff_nth_rth)+" ("+str(b_coefficient)+"x)^"+str(rth))
        print("Coefficient of x^"+str(rth)+"\n:", resultant_coefficient)
    return group


def first_count_terms(nth, count, a, b_coefficient):
    for r in range(count):
        term.insert(r, binomial_term_coefficient_finder(nth, r, a, b_coefficient, False))
    print("4 Terms are:")
    term_list_looper(count)


print("Choose a for Pas_Tri entry(C)\nChoose b for term coefficient finder\nChoose c for first nth terms")
choice = input(": ")
while choice != "a" or choice != "b" or choice != "c":
    if choice == "a":
        nth = int(input("Enter nth: "))
        rth = int(input("Enter rth: "))
        print(pascal_triangle_c_entry(nth, rth))
    if choice == "b":
        nth = int(input("Enter nth: "))
        rth = int(input("Enter rth: "))
        a = int(input("Enter a: "))
        b_coefficient = input("Enter b's coeff: ")
        if type(b_coefficient) == str:
            b_coefficient = eval(b_coefficient)
        binomial_term_coefficient_finder(nth, rth, a, b_coefficient, True)
    if choice == "c":
        nth = int(input("Enter nth: "))
        count = int(input("Enter first nth term num: "))
        a = int(input("Enter a: "))
        b_coefficient = input("Enter b's coeff: ")
        if type(b_coefficient) == str:
            b_coefficient = eval(b_coefficient)
        first_count_terms(nth, count, a, b_coefficient)

    stop_flag = 0
    while True:
        stop_or_continue = input("Stop?\na=yes,b=no : ")
        if stop_or_continue == "a":
            stop_flag = 1
            break
        if stop_or_continue == "b":
            stop_flag = 0
            break

    if stop_flag == 1:
        break
    else:
        pass
    print("Choose a for Pas_Tri entry(C)\nChoose b for term coefficient finder\nChoose c for first nth terms")
    choice = input(": ")
