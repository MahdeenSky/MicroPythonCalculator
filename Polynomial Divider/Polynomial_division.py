def is_integer(num):
    """
    returns True if a float is considered an integer/whole number.
    """
    return num == int(num)


def conv_int(num):
    """
    returns the integer form of the float is possible, else returns the float
    """
    if is_integer(num):
        return int(num)
    return num


def map_integer(iterable):
    """
    changes all the floats which can become an integer, into an integer.
    """
    for i in range(len(iterable)):
        iterable[i] = conv_int(iterable[i])
    return iterable


def expression(terms):
    """
    changes an iterable of terms, into an iterable with x to the power of their respective place in the iterable.
    """
    expression = [conv_int(terms[-1])]
    power = 1
    for term in terms[-2::-1]:
        if term != 0:
            term = conv_int(term) if term != -1 else '-'
            if power != 1:
                expression.append("{}x^{}".format(term, power))
            else:
                expression.append("{}x".format(term))
        power += 1
    return expression[::-1]


def get_terms(prompt, count=1):
    """
    acquires the terms for the respective prompt, and returns them.
    """
    print("\n", prompt)

    terms = []
    coeff = input("Term 1: ")
    while coeff != 'x':
        terms.append(float(coeff))
        count += 1
        coeff = input("Term {}: ".format(count))

    # shows how the input looks like in expression
    print(expression(terms))

    return terms


def extended_synthetic_division(dividend, divisor):
    '''Fast polynomial division by using Extended Synthetic Division. Also works with non-monic polynomials.'''
    # dividend and divisor are both polynomials, which are here simply lists of coefficients. Eg: x^2 + 3x + 5 will be represented as [1, 3, 5]

    out = list(map(int, dividend)) # Copy the dividend and changes the strings into integers for each value
    normalizer = divisor[0]
    for i in range(len(dividend)-(len(divisor)-1)):
        out[i] /= normalizer # for general polynomial division (when polynomials are non-monic),
                                 # we need to normalize by dividing the coefficient with the divisor's first coefficient
        coef = out[i]
        if coef != 0: # useless to multiply if coef is 0
            for j in range(1, len(divisor)): # in synthetic division, we always skip the first coefficient of the divisor,
                                              # because it's only used to normalize the dividend coefficients
                out[i + j] += -divisor[j] * coef

    # The resulting out contains both the quotient and the remainder, the remainder being the size of the divisor (the remainder
    # has necessarily the same degree as the divisor since it's what we couldn't divide from the dividend), so we compute the index
    # where this separation is, and return the quotient and remainder.
    separator = -(len(divisor)-1)
    return map_integer(out[:separator]), map_integer(out[separator:]) # return quotient, remainder.


print("Polynomial Synthetic Division")

dividend = get_terms("Dividend Terms: - - -")
divisor = get_terms("Divisor Terms: - - -")
quotient, remainder = extended_synthetic_division(dividend, divisor)
print("", "Quotient: ", expression(quotient), "Remainder: ", expression(remainder), sep="\n")



