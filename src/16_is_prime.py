import sys
import math


# initial algorithm
def is_prime_a(number):
    for x in range(2, number):
        if number % x == 0:
            # print(x)
            return False
    return True


# check primality using trial division
def is_prime_b(usr_input):

    n = math.ceil(math.sqrt(usr_input))
    print(n)
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


number = int(sys.argv[1])

print(is_prime_b(number))
