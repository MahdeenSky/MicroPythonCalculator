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
    return out[:separator], out[separator:] # return quotient, remainder.

Num_Polynomial, Num_Divisor, N, D, count_N, count_D, coefficient = 0, 0, [], [], 1, 1, "a"
print("POLYNOMIAL SYNTHETIC DIVISION")

while Num_Polynomial != "x":
    Num_Polynomial = input("Enter term {}\n: ".format(count_N))
    if Num_Polynomial != "x":
        N.append(Num_Polynomial)
        count_N += 1
print(N)

print("(ax + b): ")
try:
    a, b = int(input("Enter a: ")), int(input("Enter b: "))
    D.extend([a, b])
except TypeError:
    print("try again, cant be string!")
    pass

print( "  %s / %s =" % (N,D),)
print(" %s remainder %s" % extended_synthetic_division(N, D))
