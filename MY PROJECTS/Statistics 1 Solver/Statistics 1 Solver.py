
import math


def interpolation_grouped_data(grouped_data, cumulative_frequencies, position): # responsible for using linear interpolation to find the lower quartile, median, and upper quartile of grouped data
    if cumulative_frequencies[0] > position: # if the position of the data required is not in the first interval, then it is between 0 , and the lowest bound in the first interval
        mn_cu_freq = 0
        mx_cu_freq = cumulative_frequencies[0]
        mid_cu_freq = position
        interval_index = 0
    else:
        for index in range(len(cumulative_frequencies) - 1): 
            if cumulative_frequencies[index+1] > position >= cumulative_frequencies[index]: # if the position is within this interval
                mn_cu_freq = cumulative_frequencies[index]
                mx_cu_freq = cumulative_frequencies[index + 1]
                mid_cu_freq = position
                interval_index = index + 1
                break
    lower_bound, upper_bound = grouped_data[interval_index][0:2]
    return interpolation([mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, upper_bound])


def interpolation(data_for_interpolation): # uses interpolation to find the result, cu represents cumulative
    mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, upper_bound = data_for_interpolation
    result = lower_bound + ( ( (mid_cu_freq - mn_cu_freq)/(mx_cu_freq - mn_cu_freq) ) * (upper_bound - lower_bound) )
    return result


def listed_data_stats(listed_data): # for dealing with listed data Ex: 1,2,3,4 or 5,1,4,2,6,7
    # sum of data, number of data, mean
    sum_listed_data = sum(listed_data)
    number_of_data = len(listed_data)
    mean = sum_listed_data / number_of_data

    # sum of each data squared
    sum_squared_listed_data = sum(i**2 for i in listed_data)

    # variance, and standard deviation
    variance = (sum_squared_listed_data / number_of_data) - mean**2
    standard_deviation = round(math.sqrt(variance), 5)

    # median
    sorted_listed_data = listed_data[:] 
    sorted_listed_data.sort()
    if number_of_data % 2 == 0:
        median1 = sorted_listed_data[number_of_data//2] 
        median2 = sorted_listed_data[number_of_data//2 - 1] 
        median = round((median1 + median2)/2, 5)
    else:
        median = round(sorted_listed_data[number_of_data//2], 5)

    # mode
    m = max(listed_data.count(value) for value in listed_data)
    mode = set(str(x) for x in listed_data if listed_data.count(x) == m) if m>1 else None

    return [sum_listed_data, sum_squared_listed_data, number_of_data, mean, median, mode, round(variance, 5), round(standard_deviation, 5)]


def grouped_data_stats(grouped_data): # for dealing with grouped data ex: [[lower bound, upper bound, frequency], [...], [...]] etc. in [[0, 10, 16], [10, 15, 18], [15, 20, 50]] in the first list, 0 and 10 represents the interval 0 -> 10, and 16 is the frequency of numbers in this range
    midpoints = []
    cumulative_frequencies = []
    sum_x = 0
    sum_x_squared = 0
    number_of_data = 0
    if grouped_data[1][0] != grouped_data[0][1]: # if there are gaps in data
        gap = (grouped_data[1][0] - grouped_data[0][1])/2
        for data in grouped_data:
            if data[0] != 0:
                data[0] -= gap
            data[1] += gap

    for index, data in enumerate(grouped_data):
        midpoints.append((data[0] + data[1])/2) # acquires a list of midpoints for the each interval/tuple
        number_of_data += data[2] # acquires the number of data/ total frequency of all intervals
        sum_x += (midpoints[index] * data[2]) # gets the sum of all midpoints x frequency
        sum_x_squared += (midpoints[index]**2 * data[2]) # gets the sum of all midpoints^2 x frequency
        if index == 0: # if it is the first loop, then add the first value of cumulative frequency to the list
            cumulative_frequencies.append(data[2]) 
        else: # if it is not, then get the value of the previous cumulative frequency and add to it the frequency of the current data, and append it
            cumulative_frequencies.append(cumulative_frequencies[index-1] + data[2])

    # mean
    mean = sum_x / number_of_data 

    # variance, and standard deviation
    variance = (sum_x_squared / number_of_data) - mean**2
    standard_deviation = math.sqrt(variance)

    # lower quartile, median, and upper quartile, and interquartile range
    lower_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, (25/100) * number_of_data) # performs interpolation to acquire it
    median = interpolation_grouped_data(grouped_data, cumulative_frequencies, (50/100) * number_of_data)
    upper_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, (75/100) * number_of_data)
    interquartile_range = upper_quartile - lower_quartile

    return [sum_x, sum_x_squared, number_of_data, mean, variance, standard_deviation, lower_quartile, median, upper_quartile, interquartile_range]
    
        
def statistics(): # checks for what you want
    choice = input("a for\nInterpolation\nb for\nListed Data\nc for Grouped Data\n: ")

    if choice == "a": # interpolation
        mn_cu_freq = mid_cu_freq = mx_cu_freq = lower_bound = upper_bound = None
        variables = [mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, upper_bound] # values to be inputted for interpolation
        variables_names = ["mn_cu_freq", "mid_cu_freq", "mx_cu_freq", "lower_bound", "upper_bound"]
        for index, _ in enumerate(variables): 
            variables[index] = float(input("Enter {}: ".format(variables_names[index])))
        print("x = ", interpolation(variables))

    elif choice == "b": # listed data statistics
        listed_data, results = [], []
        while True:
            value = input("Enter Values: ")
            if value == "x": # enter x when no more data available
                break
            value = int(value)
            listed_data.append(value)
        results = [str(value) for value in listed_data_stats(listed_data)]
        print("", "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "n = " + results[2], "Mean = " + results[3], "Median = " + results[4],
        "Mode = " + results[5], "Variance = " + results[6], "Standard_Deviation = " + results[7], sep="\n")

    elif choice == "c": # grouped data statistics
        grouped_data, results = [], []
        while True:
            start_boundary = input("Start Bound: ")
            if start_boundary == "x": # enter x when no more data available
                break
            end_boundary = input("End Bound: ")
            frequency = input("Frequency: ")
            grouped_data.append([int(start_boundary), int(end_boundary), int(frequency)]) # each row in the grouped data is a list
        results = [str(round(value, 5)) for value in grouped_data_stats(grouped_data)]
        print("", "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "n = " + results[2], "Mean = " + results[3], "Variance = " + results[4],
        "Standard Deviation = " + results[5], "Lower Quartile = " + results[6], "Median = " + results[7], "Upper Quartile = " + results[8],
         "IQR = " + results[9], sep="\n")


statistics()