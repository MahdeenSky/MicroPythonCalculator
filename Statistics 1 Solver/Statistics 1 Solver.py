def find_median(lst): # finds the median of a sorted_list
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return lst[quotient]
    return sum(lst[quotient - 1:quotient + 1]) / 2


def find_mode(listed_data): # finds the mode for listed data
    counter = dict()
    for value in listed_data:
        if value not in counter:
            counter[value] = 0
        counter[value] += 1

    m = max(counter.values())
    if m <= 1:
        return None

    return [x for x, occurance in counter.items() if occurance == m]


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
    """
    given x and y data, it codes various operations on the data, and returns the coded data, and potentially it's statistics.
    """
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
            '/': lambda n1, n2: n1/n2,
            '^': lambda n1, n2: n1**n2}


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


def normal_distribution():
    """
    Acquires a, given x [and y], for a standard Normal Distribution of mean 0, and standard deviation 1
    1) P(Z < x) = a
    2) P(Z > x) = a
    3) P(x < Z < y) = a
    4) P(Z < a) = x
    5) P(Z > a) = x
    6) P(-a < x < a) = x
    """
    from math import sqrt, exp
    mean = 0
    standard_dev = 1
    percentage_points = {0.5000: 0.0000, 0.4000: 0.2533, 0.3000: 0.5244, 0.2000: 0.8416, 0.1500: 1.0364, 0.1000: 1.2816, 0.0500: 1.6449, 0.0250: 1.9600, 0.0100: 2.3263, 0.0050: 2.5758, 0.0010: 3.0902, 0.0005: 3.2905}

    def erf(x):
        """
        python implementation of math.erf() as it is not available in micropython
        """
        # save the sign of x
        sign = 1 if x >= 0 else -1
        x = abs(x)

        # constants
        a1 =  0.254829592
        a2 = -0.284496736
        a3 =  1.421413741
        a4 = -1.453152027
        a5 =  1.061405429
        p  =  0.3275911

        # A&S formula 7.1.26
        t = 1.0/(1.0 + p*x)
        y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*exp(-x*x)
        return sign*y # erf(-x) = -erf(x)

    def get_z_less_than(x=None, digits=4):
        """
        P(Z < x) = a
        """
        if x is None:
            x = float(input("Enter x: "))

        res = 0.5 * (1 + erf((x - mean) / sqrt(2 * standard_dev ** 2)))
        return round(res, digits)

    def get_z_greater_than(x=None):
        """
        P(Z > x) = a
        """
        if x is None:
            x = float(input("Enter x: "))

        return round(1 - get_z_less_than(x), 4)

    def get_z_in_range(lower_bound=None, upper_bound=None):
        """
        P(lower_bound < Z < upper_bound) = a
        """
        if lower_bound is None and upper_bound is None:
            lower_bound = float(input("Enter lower_bound: "))
            upper_bound = float(input("Enter upper_bound: "))

        return round(get_z_less_than(upper_bound) - get_z_less_than(lower_bound), 4)

    def get_z_less_than_a_equal(x=None, digits=4, round_=2):
        """
        P(Z < a) = x
        """
        if x is None:
            x = float(input("Enter x: "))

        if x <= 0.0 or x >= 1.0:
            raise ValueError("x must be >0.0 and <1.0")
        min_res, max_res = -10, 10
        while max_res - min_res > 10 ** -(digits * 2):
            mid = (max_res + min_res) / 2
            if get_z_less_than(mid, digits*2) < x:
                min_res = mid
            else:
                max_res = mid
        return round((max_res + min_res) / 2, round_)

    def get_z_greater_than_a_equal(x=None):
        """
        P(Z > a) = x
        """
        if x is None:
            x = float(input("Enter x: "))

        if x in percentage_points:
            return percentage_points[x]
        else:
            return get_z_less_than_a_equal(1-x, 4, 4)

    def get_z_in_range_a_b_equal(x=None):
        """
        P(-a < Z < a) = x
        acquires a
        """
        if x is None:
            x = float(input("Enter x: "))
                    
        return get_z_less_than_a_equal(0.5 + x/2, 4, 4)

    norm_choices = {'1': get_z_less_than, 
                    '2': get_z_greater_than, 
                    '3': get_z_in_range, 
                    '4': get_z_less_than_a_equal, 
                    '5': get_z_greater_than_a_equal, 
                    '6': get_z_in_range_a_b_equal}

    option = input("1: P(Z < x) = a\n2: P(Z > x) = a\n3: P(-x < Z < x) = a\n4: P(Z < a) = x\n5: P(Z > a) = x\n6: P(-a < Z < a) = x\n: ")

    # if not a valid option, then do nothing and naturally exit    
    print(norm_choices.get(option, lambda: None)())
    again = input("Try again? 1 = Yes\n: ")
    if again == '1':
        normal_distribution()


def statistics(): # checks for what you want
    choices = {'1': linear_interpolation, 
               '2': listed_data_statistics, 
               '3': continuous_grouped_data_statistics, 
               '4': discrete_grouped_data_statistics,
               '5': histogram_calculator,
               '6': code_data,
               '7': normal_distribution}
    choice = input("1: Interpolation\n2: Listed Data\n3: Continuous Data\n4: Discrete Data\n5: Histogram\n6: Code Data\n7: Norm_Dist : ")
    choices.get(choice, lambda: None)()


statistics()
