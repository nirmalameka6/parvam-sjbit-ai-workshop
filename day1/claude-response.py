def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def print_primes(limit):
    """Print all prime numbers up to a given limit."""
    primes = [n for n in range(2, limit + 1) if is_prime(n)]
    print(f"Prime numbers up to {limit}:")
    print(primes)


# Example usage
print_primes(50)
