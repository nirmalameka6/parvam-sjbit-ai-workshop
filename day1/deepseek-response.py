def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes(limit):
    """Return a list of prime numbers up to a given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def print_primes(limit):
    """Print all prime numbers up to a given limit."""
    primes = get_primes(limit)
    print(f"Prime numbers up to {limit}:")
    for prime in primes:
        print(prime, end=" ")
    print(f"\nTotal: {len(primes)} primes")

# Example usage
if __name__ == "__main__":
    # Print primes up to 50
    print_primes(50)
    
    # Get primes as a list
    primes_list = get_primes(100)
    print(f"\nFirst 10 primes from 0-100: {primes_list[:10]}")