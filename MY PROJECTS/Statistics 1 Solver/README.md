# Statistics 1 Calculator for MicroPython

Allows you to calculate statistics 1 (A Level) from your calculator itself.

For input, you'll be given 3 options "a", "b" or "c":
a is for interpolation
b is for listed data stats Ex: 1, 2, 3, 4, 7, 9
c is for grouped data stats Ex: (1->10, freq = 20), (10->20, freq = 5)

interpolation asks for 5 values:
1) minimum cumulative frequency, mid cumulative frequency, maximum cumulative frequency, lower bound, and upper bound for a given interval.

Listed Data Stats asks for as much data as you like:
enter value: 1
enter value: 2 - - - keeps looping
enter value: 3
To stop entering values at any time, enter 'x'.

Grouped Data Stats asks for as much data as well:
start bound: 0
end bound: 10 - - - keeps looping
frequency: 18
To stop entering values at any time, enter 'x' when it's start bound.

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
