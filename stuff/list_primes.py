# Section 11 exercice: Given a number, print his primes

def is_prime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True


def get_primes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)

    return list_of_primes


list_primes = get_primes(9)

print(list_primes)

for i in list_primes:
    print(i)
