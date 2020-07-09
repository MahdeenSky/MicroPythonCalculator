def find_median(lst): # finds the median of a sorted_list
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return lst[quotient]
    return sum(lst[quotient - 1:quotient + 1]) / 2


def find_mode(listed_data): # finds the mode for listed data
    Counter = {value: listed_data.count(value) for value in listed_data}
    m = max(Counter.values())
    mode = [x for x in set(listed_data) if Counter[x] == m] if m>1 else None
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
    return interpolation(mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, upper_bound)


def interpolation(mn_cu_freq, mid_cu_freq, mx_cu_freq, lower_bound, upper_bound): # uses interpolation to find the result, cu represents cumulative
    result = lower_bound + ( ( (mid_cu_freq - mn_cu_freq)/(mx_cu_freq - mn_cu_freq) ) * (upper_bound - lower_bound) )
    return result


def listed_data_stats(listed_data): # for dealing with listed data Ex: 1,2,3,4 or 5,1,4,2,6,7
    # sum of data, number of data, mean
    sum_x = sum(listed_data)
    number_of_data = len(listed_data)
    mean = sum_x / number_of_data

    # sum of each data squared
    sum_x_squared = sum(i**2 for i in listed_data)

    # variance, and standard deviation
    variance = (sum_x_squared / number_of_data) - mean**2
    standard_deviation = round((variance)**0.5, 5)

    # data sorted for finding measure of locations
    sorted_listed_data = sorted(listed_data)
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
    interquartile_range = upper_quartile - lower_quartile
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
    
    return [round(x, 5) if isinstance(x, float) else x for x in (sorted_listed_data, minimum, 
            maximum, sum_x, sum_x_squared, number_of_data, mean, mode, lower_quartile, median, 
            upper_quartile, interquartile_range, Range, variance, standard_deviation, 
            lower_outlier_bound, upper_outlier_bound, skewness, skewness_quantity)]


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
    standard_deviation = (variance)**0.5

    # lower quartile, median, and upper quartile, interquartile range, Range, and outlier
    lower_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, 0.25 * number_of_data) # performs interpolation to acquire it
    median = interpolation_grouped_data(grouped_data, cumulative_frequencies, 0.5 * number_of_data)
    upper_quartile = interpolation_grouped_data(grouped_data, cumulative_frequencies, 0.75 * number_of_data)
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
    
    return [round(x, 5) if isinstance(x, float) else x for x in (sum_x, sum_x_squared, number_of_data, midpoints, cumulative_frequencies, 
            mean, lower_quartile, median, upper_quartile, interquartile_range, 
            Range, variance, standard_deviation, lower_outlier_bound, 
            upper_outlier_bound, skewness, skewness_quantity)]


def discrete_grouped_data_stats(grouped_data):
    cumulative_frequencies = []
    sum_data = 0 
    sum_data_squared = 0

    sum_x = 0
    sum_x_squared = 0
    sum_y_squared = 0
    number_of_data = 0

    count = 0
    for data in grouped_data:
        value, frequency = data
        number_of_data += frequency
        sum_data += (value * frequency)
        sum_data_squared += (value**2 * frequency)
        sum_x += value
        sum_x_squared += value**2
        sum_y_squared += frequency**2

        if count != 0: # if it is not the first loop, then get the value of the previous cumulative frequency and add to it the frequency of the current data, and append it
            cumulative_frequencies.append(cumulative_frequencies[count-1] + frequency) 
        else: # if it is the first loop, then add the first value of cumulative frequency to the list
            cumulative_frequencies.append(frequency) 
        count += 1

    # mean
    mean = sum_data / number_of_data

    # variance, and standard deviation
    variance = (sum_data_squared / number_of_data) - mean**2
    standard_deviation = variance**0.5

    # data sorted for finding measure of locations
    sorted_listed_data = []
    if all((isinstance(freq[1], int) for freq in grouped_data)):
        for value, frequency in grouped_data:
            sorted_listed_data.extend([float(value)] * frequency)
        sorted_listed_data.sort()
    else:
        sorted_listed_data = None

    if sorted_listed_data: # standard discrete data

        # lower quartile, median, upper quartile
        middle = number_of_data//2
        LQ_list = sorted_listed_data[:middle]
        UQ_list =  sorted_listed_data[middle:] if number_of_data % 2 == 0 else sorted_listed_data[middle+1:]
        lower_quartile = find_median(LQ_list)
        median = find_median(sorted_listed_data)
        upper_quartile = find_median(UQ_list)

        # Interquartile Range
        interquartile_range = upper_quartile - lower_quartile
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

    else:  # Path towards regression line related data
        cumulative_frequencies = None

    # Sxx, Syy, Sxy, Regression Line equation (y = a + bx)
    sum_y = number_of_data
    sum_xy = sum_data
    Sxx = sum_x_squared - ( (sum_x**2)/ count )
    Syy = sum_y_squared - ( (sum_y**2)/ count )
    Sxy = sum_xy - ((sum_x * sum_y)/ count  )
    mean_x = sum_x/count
    mean_y = sum_y/count
    b = Sxy/Sxx
    a = mean_y - b*(mean_x)
    regression_line_equation = ['y = {} + {}x'.format(round(a, 5), round(b, 5))]
    if not cumulative_frequencies: # if it is regression related, then no Nones
        lower_quartile = upper_quartile = interquartile_range = lower_outlier_bound = upper_outlier_bound = None
        sum_data = sum_data_squared = number_of_data = mean = skewness = skewness_quantity = median = Range = None

    # Product Moment Coefficient
    product_momentum_correlation_coefficient = Sxy/(Sxx * Syy)**0.5

    return [round(x, 5) if isinstance(x, float) else x for x in (sum_data, sum_data_squared, number_of_data, cumulative_frequencies, 
            mean, lower_quartile, median, upper_quartile, 
            interquartile_range, Range, variance, standard_deviation, 
            lower_outlier_bound, upper_outlier_bound, skewness, 
            skewness_quantity, count, sum_x, sum_x_squared, sum_y, sum_y_squared, sum_xy, mean_x, 
            mean_y, Sxx, Syy, Sxy, b, a, regression_line_equation,
            product_momentum_correlation_coefficient)]


def check_type(x):
    if isinstance(x, float): # if type is list, do not convert to int
        return str(int(x)) if x % 1 == 0 else str(x)
    elif isinstance(x, list):
        if isinstance(x[0], float):
            return str([int(x[i]) if x[i] % 1 == 0 else x[i] for i in range(len(x))])
    return str(x)

def print_stats(results_names, results):
    print("", *(results_names[i] + " = " + check_type(results[i]) for i in range(len(results_names))), sep='\n')


def linear_interpolation(): # a
    variables = [None] * 5 # values to be inputted for interpolation
    variables_names = ["mn_cu_freq", "mid_cu_freq", "mx_cu_freq", "lower_bound", "upper_bound"]
    for index in range(5): 
        variables[index] = float(input("{}: ".format(variables_names[index])))
    print("x = ", interpolation(*variables))

def listed_data_statistics(): # b
    listed_data = [] 
    value = input("Enter Values: ")
    while value != 'x':
        value = float(value)
        listed_data.append(value)
        value = input("Enter Values: ")
    results = listed_data_stats(listed_data) # for concatonation
    results_names = ('Sorted_Data', 'Minimum', 'Maximum', 'Sum_x', 'Sum_x^2', 'n', 'Mean', 'Mode', 'Lower Quartile', 
                     'Median', 'Upper Quartile', 'IQR', 'Range', 'Variance', 'Standard Deviation',
                     'Lower Outlier', 'Upper Outlier', 'Skewness', 'Skewness Value')
    print_stats(results_names, results)

def continuous_grouped_data_statistics(): # c
    grouped_data = []
    while True:
        start_boundary = input("Start Bound: ")
        if start_boundary == "x": # enter x when no more data available
            break
        end_boundary = input("End Bound: ")
        frequency = input("Frequency: ")
        grouped_data.append([float(start_boundary), float(end_boundary), int(frequency)]) # each row in the grouped data is a list
    results = continuous_grouped_data_stats(grouped_data)
    results_names = ('Sum_x', 'Sum_x^2', 'n', 'Midpoints', 'Cum. Freq', 'Mean', 'Lower Quartile', 
                     'Median', 'Upper Quartile', 'IQR', 'Range', 'Variance', 'Standard Deviation',
                     'Lower Outlier', 'Upper Outlier', 'Skewness', 'Skewness Value')
    print_stats(results_names, results)

def discrete_grouped_data_statistics(): # d
    grouped_data = []
    while True:
        value = input("Value: ")
        if value == "x":
            break
        frequency = input("Frequency: ")
        grouped_data.append([float(value), (int(frequency) if float(frequency) % 1 == 0 else float(frequency))])
    results = discrete_grouped_data_stats(grouped_data)
    results_names = ('Sum', 'Sum^2', 'n', 'Cum. Freq', 'Mean', 'Lower Quartile', 
                     'Median', 'Upper Quartile', 'IQR', 'Range', 'Variance', 'Standard Deviation',
                     'Lower Outlier', 'Upper Outlier', 'Skewness', 'Skewness Value', 'Sample_n', 'Sum_x', 'Sum_x^2', 'Sum_y',
                     'Sum_y^2', 'Sum_xy', 'Mean_x', 'Mean_y', 'Sxx', 'Syy', 'Sxy', 'b', 'a', 'Reg. Eq', 'Prod. Momen. Coeff')
    print_stats(results_names, results)

def coded_data_discrete_output(grouped_data, prompt_index):
    prompts = ["-- With Coding --", '-- Without Coding --']
    print(prompts[prompt_index])
    results = discrete_grouped_data_stats(grouped_data)
    results_names = ('Sum', 'Sum^2', 'n', 'Cum. Freq', 'Mean', 'Lower Quartile', 
                     'Median', 'Upper Quartile', 'IQR', 'Range', 'Variance', 'Standard Deviation',
                     'Lower Outlier', 'Upper Outlier', 'Skewness', 'Skewness Value', 'Sample_n', 'Sum_x', 'Sum_x^2', 'Sum_y',
                     'Sum_y^2', 'Sum_xy', 'Mean_x', 'Mean_y', 'Sxx', 'Syy', 'Sxy', 'b', 'a', 'Reg. Eq', 'Prod. Momen. Coeff')
    print_stats(results_names, results)

def histogram_calculator(): # e
    names = ["Freq. 1 : ", "ClassWidth 1 : ", "Freq. 2 : ", "ClassWidth 2 : ", "Height 1 : ", "Width 1 : "]
    Frequency_1, Class_Width_1, Frequency_2, Class_Width_2, Height_1, Width_1 = [float(input(prompt)) for prompt in names]

    Freq_Dens_1 = Frequency_1/Class_Width_1
    Freq_Dens_2 = Frequency_2/Class_Width_2
    Width_2 = (Class_Width_2*Width_1)/Class_Width_1
    Height_2 = (Freq_Dens_2*Height_1)/Freq_Dens_1
    print("", "Other Width = " + str(Width_2), "Other Height = " + str(Height_2), sep="\n")

def code_data(): # f 
    # codes x and y data
    x_lst = []
    y_lst = []
    count = 2
    x = input("X1: ")
    y = input("Y1: ")
    while x != 'x' and y != 'x':
        x_lst.append(x)
        y_lst.append(y)
        x = input("X{}: ".format(count))
        y = input("Y{}: ".format(count))
        count += 1

    x_lst = list(map(float, x_lst))
    y_lst = list(map(float, y_lst))
    original_data = list(zip(x_lst, y_lst))

    choices = {'+': lambda n1, n2: n1+n2,
            '-': lambda n1, n2: n1-n2,
            '*': lambda n1, n2: n1*n2,
            '/': lambda n1, n2: n1/n2}


    prompts = ["Enter Operation: ", "Enter Value: "]

    x_operations = []
    y_operations = []
    count = 0
    print("\nCoding X values - - - -")
    # coding x
    coding = input(prompts[0])
    while coding != 'x':
        count += 1
        x_operations.append(coding)
        coding = input(prompts[count%2])

    count = 0
    print("\nCoding Y values - - - -")
    # coding y
    coding = input(prompts[0])
    while coding != 'x':
        count += 1
        y_operations.append(coding)
        coding = input(prompts[count%2])

    # coding elements in x and y lsts
    for i in range(0, len(x_operations), 2):
        number = float(x_operations[i+1])
        for j in range(0, len(x_lst)):
            x_lst[j] = choices[x_operations[i]](x_lst[j], number)
            x_lst[j] = int(x_lst[j]) if x_lst[j] % 1 == 0 else float(x_lst[j])

    for i in range(0, len(y_operations), 2):
        number = float(y_operations[i+1])
        for j in range(0, len(y_lst)):
            y_lst[j] = choices[y_operations[i]](y_lst[j], number)
            y_lst[j] = int(y_lst[j]) if y_lst[j] % 1 == 0 else float(y_lst[j])

    coded_data = list(zip(x_lst, y_lst))
    print("Coded X: {}".format(x_lst))
    print("Coded Y: {}\n".format(y_lst))

    d = {'x': coded_data_discrete_output}
    c = input("Stats?: x=yes: ")
    choice = d.get(c, lambda a, b: None)(coded_data, 0)
    if c == 'x':
        print("\n")
        coded_data_discrete_output(original_data, 1)

def statistics(): # checks for what you want
    choices = {'a': linear_interpolation, 
               'b': listed_data_statistics, 
               'c': continuous_grouped_data_statistics, 
               'd': discrete_grouped_data_statistics,
               'e': histogram_calculator,
               'f': code_data}
    choice = input("a for Interpolation\nb for Listed Data\nc for Continuous Data\nd for Discrete Data\ne for Histogram\nf for code data\n: ")
    choices.get(choice, lambda: None)()


statistics()