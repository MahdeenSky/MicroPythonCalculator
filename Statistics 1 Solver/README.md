# Statistics 1 Calculator for MicroPython

Allows you to calculate statistics 1 (A Level) from your calculator itself.

For input, you'll be given these possible options:
1 is for linear interpolation.
2 is for listed data stats Ex: 1, 2, 3, 4, 7, 9
3 is for continuous grouped data stats Ex: (1->10, freq = 20), (10->20, freq = 5)
4 is for discrete grouped data stats Ex: (5, freq = 10), (6, freq = 5)
5 is for histogram bar width and height finder from continous data table.
6 is for coding data
7 is for normal distribution stats


1 - interpolation asks for 5 values:
- minimum cumulative frequency, mid cumulative frequency, maximum cumulative frequency, lower bound, and upper bound for a given interval.


2 - Listed Data Stats asks for as much data as you like:
enter value: 1
enter value: 2 - - - keeps looping
enter value: 3
To stop entering values at any time, enter 'x'.


3 - Continuous Grouped Data Stats asks for as much data as well:
start bound: 0
end bound: 10 - - - keeps looping
frequency: 18
To stop entering values at any time, enter 'x' when it's start bound.
- Dont worry, it takes care of gaps in data by itself!


4 - Discrete Grouped Data Stats asks for as much data too:
Value: 1
Frequency: 5 - - - - - keeps looping
to stop entering values at any time, enter 'x' when it is at Value.


5 - Histogram height and width finder asks for 6 values:
- frequency 1, class width 1, frequency 2, class width 2, height 1, width 1.
+ the numbers is given to know that there is a given bar height and width.


6 - coding data 
given x and y data, it codes various operations on the data, and returns the coded data, and potentially it's statistics.
Output:
    X1: 2
    Y1: 4
    X2: 6
    Y2: 8
    X3: 10
    Y3: 12
    X4: 14
    Y4: 16
    X5: x
    Y5: x

    Coding X values - - - -
    Enter Operation: *
    Enter Value: 10
    Enter Operation: /
    Enter Value: 2
    Enter Operation: x

    Coding Y values - - - -
    Enter Operation: +
    Enter Value: 20
    Enter Operation: -
    Enter Value: 16
    Enter Operation: x
    Coded X: [10, 30, 50, 70]
    Coded Y: [8, 12, 16, 20]

    Stats?: x=yes: x
    -- With Coding --

    Sum = 2640
    Sum^2 = 149600
    n = 56
    Cum. Freq = [8, 20, 36, 56]
    Mean = 47.14286
    Lower Quartile = 30
    Median = 50
    Upper Quartile = 70
    IQR = 40
    Range = 60
    Variance = 448.97959
    Standard Deviation = 21.18914
    Lower Outlier = -1.78371
    Upper Outlier = 101.78371
    Skewness = negative
    Skewness Value = -0.40452
    Sample_n = 4
    Sum_x = 160
    Sum_x^2 = 8400
    Sum_y = 56
    Sum_y^2 = 864
    Sum_xy = 2640
    Mean_x = 40
    Mean_y = 14
    Sxx = 2000
    Syy = 80
    Sxy = 400
    b = 0.2
    a = 6
    Reg. Eq = ['y = 6.0 + 0.2x']
    Prod. Momen. Coeff = 1


    -- Without Coding --

    Sum = None
    Sum^2 = None
    n = None
    Cum. Freq = None
    Mean = None
    Lower Quartile = None
    Median = None
    Upper Quartile = None
    IQR = None
    Range = None
    Variance = 16
    Standard Deviation = 4
    Lower Outlier = None
    Upper Outlier = None
    Skewness = None
    Skewness Value = None
    Sample_n = 4
    Sum_x = 32
    Sum_x^2 = 336
    Sum_y = 40
    Sum_y^2 = 480
    Sum_xy = 400
    Mean_x = 8
    Mean_y = 10
    Sxx = 80
    Syy = 80
    Sxy = 80
    b = 1
    a = 2
    Reg. Eq = ['y = 2.0 + 1.0x']
    Prod. Momen. Coeff = 1

7 - normal_distribution stats ask for a what to be calculated from a standard normal distribution.
Acquires a, given x [and y], for a standard Normal Distribution of mean 0, and standard deviation 1
    1) P(Z < x) = a
    2) P(Z > x) = a
    3) P(x < Z < y) = a
    4) P(Z < a) = x
    5) P(Z > a) = x
    6) P(-a < x < a) = x


Gives a wide range of output, which include:
1) sum of values
2) sum of each values squared
3) number of data
4) mean
5) mode
6) median
7) lower quartile
8) upper quartile
9) interquartile range
10) Variance
11) Standard Deviation 
12) Range
13) lower outlier (based on 1.5 x standard deviation)
14) upper outlier (based on 1.5 x standard deviation)
15) measure of skewness
16) skewness (positive, negative, symmetrical)
17) middle values for each class in continuous
18) Sorted Listed Data from smallest to greatest
19) all the cumulative frequencies for each interval consecutively
20) sum of x data
21) sum of y data
22) sum of x^2 data
23) sum of y^2 data
24) sum of x*y
25) mean of x
26) mean of y
27) Sxx (summation of xx)
28) Syy (summation of yy)
29) Sxy (summation of xy)
30) Regression line equation
31) Product Moment Coefficient
32) Normal Distribution Values from the standard normal distribution