def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    
    primes = [True] * (n + 1)
    p = 2
    
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

n = 30
prime_numbers = sieve_of_eratosthenes(n)
print(f"List of prime numbers (up to {n}): {prime_numbers}")
