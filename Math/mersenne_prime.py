def is_prime(num):
    """Function to check if a given number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_mersenne_prime(n):
    """Function to determine if the given n is a Mersenne prime."""
    if is_prime(n):  # First, check if n is prime
        mersenne_prime = 2**n - 1  # Calculate the Mersenne number
        return is_prime(mersenne_prime)  # Check if the Mersenne number is prime
    return False

# User input
n = int(input("Enter a value for n: "))
if is_mersenne_prime(n):
    print(f"The Mersenne prime M_{n} = 2^{n} - 1 is prime.")
else:
    print(f"The Mersenne prime M_{n} = 2^{n} - 1 is not prime.")
