import sys

def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            print(x)
            return False
    return True


number = int(sys.argv[1])

print(is_prime(number))
