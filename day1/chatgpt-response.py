def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

# Input
limit = int(input("Enter a number: "))
print_primes(limit)