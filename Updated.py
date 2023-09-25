# Hardcode lots of different parameters. If there is no value for a parameter, let it equal 0.
# Depending on what parameters we have, depends on what method we will call in order to calculate the necessary calculation. 
# This means that the code can function fine without having to have to change the calculation if we don't have certain parameters.

def add_two_parameters(a, b, c, d, e):
    return a + b + c + d + e

a, b = 1, 1
c, d, e = 0, 0, 0

if a != 0 and b != 0:
    result1 = add_two_parameters(a, b)
    print(f"{a} + {b} = {result1}")

if a != 0 and c != 0:
    result2 = add_two_parameters(a, c)
    print(f"{a} + {c} = {result2}")

if a != 0 and d != 0:
    result3 = add_two_parameters(a, d)
    print(f"{a} + {d} = {result3}")

if a != 0 and e != 0:
    result4 = add_two_parameters(a, e)
    print(f"{a} + {e} = {result4}")

if b != 0 and c != 0:
    result5 = add_two_parameters(b, c)
    print(f"{b} + {c} = {result5}")

if b != 0 and d != 0:
    result6 = add_two_parameters(b, d)
    print(f"{b} + {d} = {result6}")

if b != 0 and e != 0:
    result7 = add_two_parameters(b, e)
    print(f"{b} + {e} = {result7}")
