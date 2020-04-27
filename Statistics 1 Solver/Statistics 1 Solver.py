
import math

def find_median(List): # finds the median of a sorted_list
    number_of_data = len(List)
    if number_of_data % 2 == 0:
        median = (List[(number_of_data//2)]+List[(number_of_data//2-1)])/2
    else:
        median = List[(number_of_data//2)]
    return median


def find_mode(listed_data):
    m = max(listed_data.count(value) for value in listed_data)
    mode = set(str(x) for x in listed_data if listed_data.count(x) == m) if m>1 else None
    return mode


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

    # data sorted for finding measure of locations
    sorted_listed_data = listed_data[:] 
    sorted_listed_data.sort()
    middle = number_of_data//2

    # minimum, and maximum value
    minimum = sorted_listed_data[0]
    maximum = sorted_listed_data[-1]

    # lower quartile, median, upper quartile
    LQ_list, Median_list = sorted_listed_data[:middle], sorted_listed_data
    UQ_list =  sorted_listed_data[middle:] if number_of_data % 2 == 0 else sorted_listed_data[middle+1:]
    lower_quartile = find_median(LQ_list)
    median = find_median(Median_list)
    upper_quartile = find_median(UQ_list)

    # Interquartile Range
    IQR = upper_quartile - lower_quartile
    Range = sorted_listed_data[-1] - sorted_listed_data[0]

    # Outliers
    lower_outlier_bound = lower_quartile - (1.5*standard_deviation)
    upper_outlier_bound = upper_quartile + (1.5*standard_deviation)

    # Skewness
    skewness_quantity = (3*(mean-median))/standard_deviation
    if skewness_quantity > 0:
        skewness = "positive"
    elif skewness_quantity < 0:
        skewness = "negative"
    else:
        skewness = "symmetrical"

    # mode
    mode = find_mode(sorted_listed_data)

    return [sum_listed_data, sum_squared_listed_data, number_of_data, round(mean, 5), median, mode, round(variance, 5), round(standard_deviation, 5), lower_quartile, upper_quartile, IQR, Range, round(lower_outlier_bound, 5), round(upper_outlier_bound, 5), skewness, round(skewness_quantity, 5), minimum, maximum, sorted_listed_data]


def continuous_grouped_data_stats(grouped_data): # for dealing with grouped data ex: [[lower bound, upper bound, frequency], [...], [...]] etc. in [[0, 10, 16], [10, 15, 18], [15, 20, 50]] in the first list, 0 and 10 represents the interval 0 -> 10, and 16 is the frequency of numbers in this range
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

    count = 0
    for data in grouped_data:
        start_bound = data[0]
        end_bound = data[1]
        frequency = data[2]
        midpoints.append((start_bound + end_bound)/2) # acquires a list of midpoints for the each interval/tuple
        current_midpoint = midpoints[count]
        number_of_data += frequency # acquires the number of data/ total frequency of all intervals
        sum_x += (current_midpoint * frequency) # gets the sum of all midpoints x frequency
        sum_x_squared += (current_midpoint**2 * frequency) # gets the sum of all midpoints^2 x frequency
        if count == 0: # if it is the first loop, then add the first value of cumulative frequency to the list
            cumulative_frequencies.append(frequency) 
        else: # if it is not, then get the value of the previous cumulative frequency and add to it the frequency of the current data, and append it
            cumulative_frequencies.append(cumulative_frequencies[count-1] + frequency)
        count += 1

    # mean
    mean = sum_x / number_of_data 

    # variance, and standard deviation
    variance = (sum_x_squared / number_of_data) - mean**2
    standard_deviation = math.sqrt(variance)

    # lower quartile, median, and upper quartile, interquartile range, Range, and outlier
    lower_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, (25/100) * number_of_data) # performs interpolation to acquire it
    median = interpolation_grouped_data(grouped_data, cumulative_frequencies, (50/100) * number_of_data)
    upper_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, (75/100) * number_of_data)
    interquartile_range = upper_quartile - lower_quartile
    Range = grouped_data[-1][1] - grouped_data[0][0]
    lower_outlier_bound = lower_quartile - (1.5*standard_deviation)
    upper_outlier_bound = upper_quartile + (1.5*standard_deviation)
    
    # Skewness
    skewness_quantity = (3*(mean-median))/standard_deviation
    if skewness_quantity > 0:
        skewness = "positive"
    elif skewness_quantity < 0:
        skewness = "negative"
    else:
        skewness = "symmetrical"
    
    return [sum_x, sum_x_squared, number_of_data, round(mean, 5), round(variance, 5), round(standard_deviation, 5), round(lower_quartile, 5), round(median, 5), round(upper_quartile, 5), round(interquartile_range, 5), skewness, round(skewness_quantity, 5), round(lower_outlier_bound, 5), round(upper_outlier_bound, 5), Range, midpoints]


def discrete_grouped_data_stats(grouped_data):
    cumulative_frequencies = []
    sum_x = 0
    sum_x_squared = 0
    number_of_data = 0
    
    count = 0
    for data in grouped_data:
        value = data[0]
        frequency = data[1]
        number_of_data += frequency
        sum_x += (value * frequency)
        sum_x_squared += (value**2 * frequency)
        if count == 0: # if it is the first loop, then add the first value of cumulative frequency to the list
            cumulative_frequencies.append(frequency) 
        else: # if it is not, then get the value of the previous cumulative frequency and add to it the frequency of the current data, and append it
            cumulative_frequencies.append(cumulative_frequencies[count-1] + frequency)
        count += 1

    # mean
    mean = sum_x / number_of_data

    # variance, and standard deviation
    variance = (sum_x_squared / number_of_data) - mean**2
    standard_deviation = math.sqrt(variance)

    # data sorted for finding measure of locations
    sorted_listed_data = []
    for value, frequency in grouped_data:
        calc = ((str(value) + " ")*frequency).strip()
        finalised_list = calc.split()
        sorted_listed_data.extend([float(i) for i in finalised_list])
    middle = len(sorted_listed_data)//2
    sorted_listed_data.sort()

    # mode
    mode = find_mode(sorted_listed_data)

    # lower quartile, median, upper quartile
    LQ_list, Median_list = sorted_listed_data[:middle], sorted_listed_data
    UQ_list =  sorted_listed_data[middle:] if number_of_data % 2 == 0 else sorted_listed_data[middle+1:]
    lower_quartile = find_median(LQ_list)
    median = find_median(Median_list)
    upper_quartile = find_median(UQ_list)

    # Interquartile Range
    IQR = upper_quartile - lower_quartile
    Range = sorted_listed_data[-1] - sorted_listed_data[0]

    # Outliers
    lower_outlier_bound = lower_quartile - (1.5*standard_deviation)
    upper_outlier_bound = upper_quartile + (1.5*standard_deviation)

    # Skewness
    skewness_quantity = (3*(mean-median))/standard_deviation
    if skewness_quantity > 0:
        skewness = "positive"
    elif skewness_quantity < 0:
        skewness = "negative"
    else:
        skewness = "symmetrical"

    return [sum_x, sum_x_squared, number_of_data, round(mean, 5), median, mode, round(variance, 5), round(standard_deviation, 5), lower_quartile, upper_quartile, IQR, Range, round(lower_outlier_bound, 5), round(upper_outlier_bound, 5), skewness, round(skewness_quantity, 5)]



def statistics(): # checks for what you want
    choice = input("a for Interpolation\nb for Listed Data\nc for Continuous Data\nd for Discrete Data\ne for Histogram\n: ")


    if choice == "a": # linear interpolation
        mn_cu_freq = mid_cu_freq = mx_cu_freq = lower_bound = upper_bound = None
        variables = [mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, upper_bound] # values to be inputted for interpolation
        variables_names = ["mn_cu_freq", "mid_cu_freq", "mx_cu_freq", "lower_bound", "upper_bound"]
        for index in range(len(variables)): 
            variables[index] = float(input("Enter {}: ".format(variables_names[index])))
        print("x = ", interpolation(variables))


    elif choice == "b": # listed data statistics
        listed_data = []
        while True:
            value = input("Enter Values: ")
            if value == "x": # enter x when no more data available
                break
            value = float(value)
            listed_data.append(value)
        results = [str(value) for value in listed_data_stats(listed_data)] # for concatonation
        print("", results[18], "Minimum = " + results[16], "Maximum = " + results[17], "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "n = " + results[2], "Mean = " + results[3], "Mode = " + results[5],
        "Lower Quartile = " + results[8], "Median = " + results[4], "Upper Quartile = " + results[9], "IQR = " + results[10],
         "Range = " + results[11], "Variance = " + results[6], "Standard_Deviation = " + results[7], "Lower outlier = " + results[12],
         "Upper outlier = " + results[13], "Skewness is " + results[14], "Skewness count = " + results[15], sep="\n")


    elif choice == "c": # continuous grouped data statistics
        grouped_data = []
        while True:
            start_boundary = input("Start Bound: ")
            if start_boundary == "x": # enter x when no more data available
                break
            end_boundary = input("End Bound: ")
            frequency = input("Frequency: ")
            grouped_data.append([float(start_boundary), float(end_boundary), int(frequency)]) # each row in the grouped data is a list
        results = [str(value) for value in continuous_grouped_data_stats(grouped_data)]
        print("", "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "Midpoints are " + results[15], "n = " + results[2], "Mean = " + results[3], "Variance = " + results[4],
        "Standard Dev. = " + results[5], "Lower Quartile = " + results[6], "Median = " + results[7], "Upper Quartile = " + results[8],
         "IQR = " + results[9], "Range = " + results[14], "Skewness is " + results[10], "Skewness count = " + results[11], 
         "Lower outlier = " + results[12], "Upper outlier = " + results[13], sep="\n")


    elif choice == "d": # discrete grouped data statistics 
        grouped_data = []
        while True:
            value = input("Value: ")
            if value == "x":
                break
            frequency = input("Frequency: ")
            grouped_data.append([float(value), int(frequency)])
        results = [str(value) for value in discrete_grouped_data_stats(grouped_data)]
        print("", "Sum_x = " + results[0], "Sum_x^2 = " + results[1], "n = " + results[2], "Mean = " + results[3], "Mode = " + results[5],
        "Lower Quartile = " + results[8], "Median = " + results[4], "Upper Quartile = " + results[9], "IQR = " + results[10],
         "Range = " + results[11], "Variance = " + results[6], "Standard_Deviation = " + results[7], "Lower outlier = " + results[12],
         "Upper outlier = " + results[13], "Skewness is " + results[14], "Skewness count = " + results[15], sep="\n")


    elif choice == "e": # height and width calculator of histogram
        names = ["Freq. 1 : ", "ClassWidth 1 : ", "Freq. 2 : ", "ClassWidth 2 : ", "Height 1 : ", "Width 1 : "]
        prompts = [float(input(prompt)) for prompt in names]
        Frequency_1, Class_Width_1, Frequency_2, Class_Width_2, Height_1, Width_1 = prompts[0], prompts[1], prompts[2], prompts[3], prompts[4], prompts[5]

        Freq_Dens_1 = Frequency_1/Class_Width_1
        Freq_Dens_2 = Frequency_2/Class_Width_2
        Width_2 = (Class_Width_2*Width_1)/Class_Width_1
        Height_2 = (Freq_Dens_2*Height_1)/Freq_Dens_1
        print("", "Other Width = " + str(Width_2), "Other Height = " + str(Height_2), sep="\n")

    
        
statistics()