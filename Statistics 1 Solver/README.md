# Statistics 1 Calculator for MicroPython

Allows you to calculate statistics 1 (A Level) from your calculator itself.

For input, you'll be given 3 options "a", "b" or "c":
a is for linear interpolation.
b is for listed data stats Ex: 1, 2, 3, 4, 7, 9
c is for continuous grouped data stats Ex: (1->10, freq = 20), (10->20, freq = 5)
d is for discrete grouped data stats Ex: (5, freq = 10), (6, freq = 5)
e is for histogram bar width and height finder from continous data table.

interpolation asks for 5 values:
- minimum cumulative frequency, mid cumulative frequency, maximum cumulative frequency, lower bound, and upper bound for a given interval.

Listed Data Stats asks for as much data as you like:
enter value: 1
enter value: 2 - - - keeps looping
enter value: 3
To stop entering values at any time, enter 'x'.

Continuous Grouped Data Stats asks for as much data as well:
start bound: 0
end bound: 10 - - - keeps looping
frequency: 18
To stop entering values at any time, enter 'x' when it's start bound.

Discrete Grouped Data Stats asks for as much data too:
Value: 1
Frequency: 5 - - - - - keeps looping
to stop entering values at any time, enter 'x' when it is at Value.

Histogram height and width finder asks for 6 values:
- frequency 1, class width 1, frequency 2, class width 2, height 1, width 1.
+ the numbers is given to know that there is a given bar height and width.


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