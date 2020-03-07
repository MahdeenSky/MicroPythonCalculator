# Original SUVAT equations
# v = u + at
# s = 0.5(u+v)*t
# v^2 = u^2 + 2a*s
# s = ut + 0.5at^2
from math import sqrt, pi

# replaces "pi" with the symbol of pi if inputted from a calculator
def input_pi_replacer(prompt):
    return input(prompt).replace("pi", str(pi))


def stopper():
    stop_or_continue = input("Stop?: ")
    if stop_or_continue == "x":
        raise SystemExit  

print("Suvat Calculator:")
print("if variable not\ngiven then type\n'x'\n")


def suvatsolver():

    while True:
        # this will keep track of how many variables are known, since three are required.
        variable_count = 0
        [s_known, u_known, v_known, a_known, t_known] = [False, False, False, False, False]

        distance = input_pi_replacer("Distance in metres\n:  ")
        # this assumes that the input is actually acceleration number.
        # then it says the variable is known and adds 1 to the variable count.
        if distance != "x":
            s_known = True
            distance = float(eval(distance))
            variable_count += 1

        initial_velocity = input_pi_replacer("Initial velocity\nin metres/second\n: ")
        if initial_velocity != "x":
            u_known = True
            initial_velocity = float(eval(initial_velocity))
            variable_count += 1

        final_velocity = input_pi_replacer("Final velocity\n in metres/second\n: ")
        if final_velocity != "x":
            v_known = True
            final_velocity = float(eval(final_velocity))
            variable_count += 1
        else:
            pass

        acceleration = input_pi_replacer("Acceleration\n in metres/second squared\n: ")
        if acceleration != "x":
            a_known = True
            acceleration = float(eval(acceleration))
            variable_count += 1
        else:
            pass

        time = input_pi_replacer("Time\nin seconds\n: ")
        if time != "x":
            t_known = True
            time = float(eval(time))
            variable_count += 1
        else:
            pass

        if variable_count < 3:
            print("not enough variables")
            break

        # this next bunch of statements pretty much goes through
        # all possible combinations of three variables
        # and calculates the remaining unknowns (I solved the equations myself)
        if s_known and u_known and v_known:
            acceleration = (final_velocity ** 2 - initial_velocity ** 2) / (2 * distance)
            time = 2 * distance / (initial_velocity + final_velocity)
            print("")
            print("Acceleration =\n", acceleration)
            print("Time =\n", time)

        elif s_known and u_known and a_known:
            final_velocity = sqrt(initial_velocity ** 2 + 2 * acceleration * distance)
            t1 = -initial_velocity / acceleration + sqrt(2 * acceleration * distance + initial_velocity ** 2) / acceleration
            t2 = -initial_velocity / acceleration - sqrt(2 * acceleration * distance + initial_velocity ** 2) / acceleration
            print("")
            print("Final velocity =\n", final_velocity, "\nor ", -final_velocity)
            print("Time =\n", t1, "\nor ", t2)

        elif s_known and u_known and t_known:
            final_velocity = 2 * distance / time - initial_velocity
            acceleration = 2 * (distance - initial_velocity * time) / time ** 2
            print("")
            print("Final velocity =\n", final_velocity)
            print("Acceleration =\n", acceleration)

        elif s_known and v_known and a_known:
            initial_velocity = sqrt(final_velocity ** 2 - 2 * acceleration * distance)
            t1 = 2 * distance / (final_velocity + sqrt(final_velocity ** 2 - 2 * acceleration * distance))
            t2 = 2 * distance / (final_velocity - sqrt(final_velocity ** 2 - 2 * acceleration * distance))
            print("")
            print("Initial velocity =\n", initial_velocity, "\nor", -initial_velocity)
            print("Time =\n", t1, "\nor", t2)

        elif s_known and v_known and t_known:
            initial_velocity = 2 * distance / time - final_velocity
            acceleration = (final_velocity - initial_velocity) / time
            print("")
            print("Initial velocity =\n", initial_velocity)
            print("Acceleration =\n", acceleration)

        elif s_known and a_known and t_known:
            initial_velocity = (distance - 0.5 * acceleration * time ** 2) / time
            final_velocity = initial_velocity + acceleration * time
            print("")
            print("Initial velocity =\n", initial_velocity)
            print("Final velocity =\n", final_velocity)

        elif u_known and v_known and a_known:
            distance = (final_velocity ** 2 - initial_velocity ** 2) / (2 * acceleration)
            time = (final_velocity - initial_velocity) / acceleration
            print("")
            print("Distance =\n", distance)
            print("Time =\n", time)

        elif u_known and v_known and t_known:
            distance = 0.5 * (initial_velocity + final_velocity) * time
            acceleration = (final_velocity - initial_velocity) / time
            print("")
            print("Distance =\n", distance)
            print("Acceleration =\n", acceleration)

        elif u_known and a_known and t_known:
            final_velocity = initial_velocity + acceleration * time
            distance = initial_velocity * time + 0.5 * acceleration * time ** 2
            print("")
            print("Final velocity =\n", final_velocity)
            print("Distance =\n", distance)

        elif v_known and a_known and t_known:
            initial_velocity = final_velocity - acceleration * time
            distance = 0.5 * (2 * final_velocity - acceleration * time) * time
            print("")
            print("Initial velocity =\n", initial_velocity)
            print("Distance =\n", distance)

        print("")
        break

while True:
    suvatsolver()
    stopper()
