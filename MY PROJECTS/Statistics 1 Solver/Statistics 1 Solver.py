"""
1) Linear Interpolation
2) 
"""
import math


def interpolation_grouped_data(grouped_data, cumulative_frequencies, position):
    if cumulative_frequencies[0] > position:
        mn_cu_freq = 0
        mx_cu_freq = cumulative_frequencies[0]
        mid_cu_freq = position
        interval_index = 0
    else:
        for index in range(len(cumulative_frequencies) - 1):
            if cumulative_frequencies[index+1] > position >= cumulative_frequencies[index]:
                mn_cu_freq = cumulative_frequencies[index]
                mx_cu_freq = cumulative_frequencies[index + 1]
                mid_cu_freq = position
                interval_index = index + 1
                break
    lower_bound = grouped_data[interval_index][0]
    higher_bound = grouped_data[interval_index][1]
    return interpolation(mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, higher_bound)


def interpolation(mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, higher_bound):
    result = lower_bound + ( ( (mid_cu_freq - mn_cu_freq)/(mx_cu_freq - mn_cu_freq) ) * (higher_bound - lower_bound) )
    return result


def listed_data_stats(listed_data):
    sum_listed_data = sum(listed_data)
    number_of_data = len(listed_data)
    mean = sum_listed_data / number_of_data

    squared_listed_data = [i**2 for i in listed_data]
    sum_squared_listed_data = sum(squared_listed_data)

    variance = (sum_squared_listed_data / number_of_data) - (mean)**2
    standard_deviation = math.sqrt(variance)

    median_position = (50/100) * number_of_data
    if median_position % 1 == 0:
        median = (listed_data[median_position - 1] + listed_data[median_position])/2
    else:
        median = listed_data[math.ceil(median_position) - 1]

    number_count = {}
    for value in listed_data:
        number_count.setdefault(value, 1)
        if number_count.get(value) != None:
            number_count[value] += 1
    most_counts = 0
    for value, count in number_count.items():
        if count > most_counts:
            most_counts = count
            mode = value

    return sum_listed_data, sum_squared_listed_data, number_of_data, mean, median, mode, round(variance, 5), round(standard_deviation, 5)


def grouped_data_stats(grouped_data): # [(0, 10, 16), (10, 15, 18), (15, 20, 50)]
    midpoints = []
    cumulative_frequencies = []
    sum_x = 0
    sum_x_squared = 0
    number_of_data = 0
    if grouped_data[1][0] - grouped_data[0][1] != 0:
        gap = (grouped_data[1][0] - grouped_data[0][1])/2
        for data in grouped_data:
            if data[0] != 0:
                data[0] -= gap
            data[1] += gap
            
    for index, data in enumerate(grouped_data):
        midpoints.append((data[0] + data[1])/2)
        number_of_data += data[2]
        sum_x += (midpoints[index] * data[2])
        sum_x_squared += (midpoints[index]**2 * data[2])
        if index == 0:
            cumulative_frequencies.append(data[2])
        else:
            cumulative_frequencies.append(cumulative_frequencies[index-1] + data[2])

    mean = sum_x / number_of_data

    variance = (sum_x_squared / number_of_data) - (sum_x / number_of_data)**2
    standard_deviation = math.sqrt(variance)

    lower_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, (25/100) * number_of_data)
    median = interpolation_grouped_data(grouped_data, cumulative_frequencies, (50/100) * number_of_data)
    upper_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, (75/100) * number_of_data)
    interquartile_range = upper_quartile - lower_quartile

    return sum_x, sum_x_squared, number_of_data, mean, variance, standard_deviation, lower_quartile, median, upper_quartile, interquartile_range
    
        
def statistics():
    choice = input("a for\nInterpolation\nb for\nListed Data\nc for Grouped Data\n: ")

    if choice == "a":
        mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, higher_bound = None, None, None, None, None
        variables = [mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, higher_bound]
        variables_names = ["mn_cu_freq", "mid_cu_freq", "mx_cu_freq", "lower_bound", "higher_bound"]
        for index in enumerate(variables):
            variables[index] = input("Enter {}: ".format(variables_names[index]))
        print("x = ", interpolation(mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, higher_bound))

    elif choice == "b":
        listed_data, results = [], []
        while True:
            value = input("Enter Values: ")
            if value == "x":
                break
            value = int(value)
            listed_data.append(value)
        results.extend(listed_data_stats(listed_data))
        results = [str(value) for value in results]
        print("", "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "n = " + results[2], "Mean = " + results[3], "Median = " + results[4],
        "Mode = " + results[5], "Variance = " + results[6], "Standard_Deviation = " + results[7], sep="\n")

    elif choice == "c":
        grouped_data, results = [], []
        while True:
            start_boundary = input("Start Bound: ")
            if start_boundary == "x":
                break
            end_boundary = input("End Bound: ")
            frequency = input("Frequency: ")
            grouped_data.append([int(start_boundary), int(end_boundary), int(frequency)])
        results.extend(grouped_data_stats(grouped_data))
        results = [str(value) for value in results]
        print("", "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "n = " + results[2], "Mean = " + results[3], "Variance = " + results[4],
        "Standard Deviation = " + results[5], "Lower Quartile = " + results[6], "Median = " + results[7], "Upper Quartile = " + results[8],
         "IQR = " + results[9], sep="\n")


statistics()




    










