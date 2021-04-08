# Original SUVAT equations
# v = u + at
# s = 0.5(u+v)*t
# v^2 = u^2 + 2a*s
# s = ut + 0.5at^2
# s = vt - 0.5at^2
from math import sqrt

def stopper():
    stop_or_continue = input("Stop?: ")
    if stop_or_continue == "x":
        raise SystemExit  


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def suvatsolver():

    # this will keep track of how many variables are known, since three are required.
    variables = {'distance': None, 'initial_velocity': None, 'final_velocity': None, 'acceleration': None, 'time': None}

    variables['distance']         = input(("Distance in metres\n: "))
    variables['initial_velocity'] = input(("Initial velocity in m/s\n: "))
    variables['final_velocity']   = input(("Final velocity in m/s\n: "))
    variables['acceleration']     = input(("Acceleration in m/s^2\n: "))
    variables['time']             = input(("Time in seconds\n: "))

    for var_name, value in variables.items():
        if isfloat(value):
            variables[var_name] = float(value)
        else:
            variables[var_name] = None

    if sum(1 if value != None else 0 for value in variables.values()) < 3:
        print("\nNot Enough Variables Known!")
        return    
    print()

    # this next bunch of statements pretty much goes through
    # all possible combinations of three variables
    # and calculates the remaining unknowns (I solved the equations myself)
    if variables['distance'] and variables['initial_velocity'] and variables['final_velocity']:
        variables['acceleration'] = (variables['final_velocity'] ** 2 - variables['initial_velocity'] ** 2) / (2 * variables['distance'])
        variables['time'] = 2 * variables['distance'] / (variables['initial_velocity'] + variables['final_velocity'])
        print("v^2 = u^2 + 2a*s")
        print("Acceleration =\n", variables['acceleration'])
        print("s = 0.5(u+v)*t")
        print("Time =\n", variables['time'])

    elif variables['distance'] and variables['initial_velocity'] and variables['acceleration']:
        variables['final_velocity'] = sqrt(variables['initial_velocity'] ** 2 + 2 * variables['acceleration'] * variables['distance'])
        t1 = -variables['initial_velocity'] / variables['acceleration'] + sqrt(2 * variables['acceleration'] * variables['distance'] + variables['initial_velocity'] ** 2) / variables['acceleration']
        t2 = -variables['initial_velocity'] / variables['acceleration'] - sqrt(2 * variables['acceleration'] * variables['distance'] + variables['initial_velocity'] ** 2) / variables['acceleration']
        print("v^2 = u^2 + 2a*s")
        print("Final velocity =\n", variables['final_velocity'], "\nor ", -variables['final_velocity'])
        print("s = ut + 0.5at^2")
        print("Time =\n", t1, "\nor ", t2)

    elif variables['distance'] and variables['initial_velocity'] and variables['time']:
        variables['final_velocity'] = 2 * variables['distance'] / variables['time'] - variables['initial_velocity']
        variables['acceleration'] = 2 * (variables['distance'] - variables['initial_velocity'] * variables['time']) / variables['time'] ** 2
        print("s = 0.5(u+v)*t")
        print("Final velocity =\n", variables['final_velocity'])
        print("s = ut + 0.5at^2")
        print("Acceleration =\n", variables['acceleration'])

    elif variables['distance'] and variables['final_velocity'] and variables['acceleration']:
        variables['initial_velocity'] = sqrt(variables['final_velocity'] ** 2 - 2 * variables['acceleration'] * variables['distance'])
        t1 = 2 * variables['distance'] / (variables['final_velocity'] + sqrt(variables['final_velocity'] ** 2 - 2 * variables['acceleration'] * variables['distance']))
        t2 = 2 * variables['distance'] / (variables['final_velocity'] - sqrt(variables['final_velocity'] ** 2 - 2 * variables['acceleration'] * variables['distance']))
        print("v^2 = u^2 + 2a*s")
        print("Initial velocity =\n", variables['initial_velocity'], "\nor", -variables['initial_velocity'])
        print("s = vt - 0.5at^2")
        print("Time =\n", t1, "\nor", t2)

    elif variables['distance'] and variables['final_velocity'] and variables['time']:
        variables['initial_velocity'] = 2 * variables['distance'] / variables['time'] - variables['final_velocity']
        variables['acceleration'] = (variables['final_velocity'] - variables['initial_velocity']) / variables['time']
        print("s = 0.5(u+v)*t")
        print("Initial velocity =\n", variables['initial_velocity'])
        print("s = vt - 0.5at^2")
        print("Acceleration =\n", variables['acceleration'])

    elif variables['distance'] and variables['acceleration'] and variables['time']:
        variables['initial_velocity'] = (variables['distance'] - 0.5 * variables['acceleration'] * variables['time'] ** 2) / variables['time']
        variables['final_velocity'] = variables['initial_velocity'] + variables['acceleration'] * variables['time']
        print("s = ut + 0.5at^2")
        print("Initial velocity =\n", variables['initial_velocity'])
        print("s = vt - 0.5at^2")
        print("Final velocity =\n", variables['final_velocity'])

    elif variables['initial_velocity'] and variables['final_velocity'] and variables['acceleration']:
        variables['distance'] = (variables['final_velocity'] ** 2 - variables['initial_velocity'] ** 2) / (2 * variables['acceleration'])
        variables['time'] = (variables['final_velocity'] - variables['initial_velocity']) / variables['acceleration']
        print("v^2 = u^2 + 2a*s")
        print("Distance =\n", variables['distance'])
        print("v = u + at")
        print("Time =\n", variables['time'])

    elif variables['initial_velocity'] and variables['final_velocity'] and variables['time']:
        variables['distance'] = 0.5 * (variables['initial_velocity'] + variables['final_velocity']) * variables['time']
        variables['acceleration'] = (variables['final_velocity'] - variables['initial_velocity']) / variables['time']
        print("s = 0.5(u+v)*t")
        print("Distance =\n", variables['distance'])
        print("v = u + at")
        print("Acceleration =\n", variables['acceleration'])

    elif variables['initial_velocity'] and variables['acceleration'] and variables['time']:
        variables['final_velocity'] = variables['initial_velocity'] + variables['acceleration'] * variables['time']
        variables['distance'] = variables['initial_velocity'] * variables['time'] + 0.5 * variables['acceleration'] * variables['time'] ** 2
        print("v = u + at")
        print("Final velocity =\n", variables['final_velocity'])
        print("s = ut + 0.5at^2")
        print("Distance =\n", variables['distance'])

    elif variables['final_velocity'] and variables['acceleration'] and variables['time']:
        variables['initial_velocity'] = variables['final_velocity'] - variables['acceleration'] * variables['time']
        variables['distance'] = 0.5 * (2 * variables['final_velocity'] - variables['acceleration'] * variables['time']) * variables['time']
        print("v = u + at")
        print("Initial velocity =\n", variables['initial_velocity'])
        print("s = vt - 0.5at^2")
        print("Distance =\n", variables['distance'])


print("Suvat Calculator:")
print("if variable not\ngiven then type\n'x'\n")
while True:
    suvatsolver()
    stopper()
