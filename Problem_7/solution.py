# Since the 10001st prime should not be very large, several solutions can be employed.
# Here, Sieve of Eratosthenes (SoE) will be used in a modified form for better efficiency.
# Other possible solutions could be brute force ones like Trial Division in its many forms or elaborate primality tests like Miller-Rabin.
# The modifications being employed are leveraging the efficiency of boolean values manipulation and the distribution of primes over even and odd numbers.

limit = 150000      # Arbitrary limit to ensure that the prime is within its range
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

count = 1     # Number of primes found
result = 2    # The latest prime found, updates iteratively
number = 3    # Latest number being checked

while count < 10001 and number < limit:
    if is_prime[number]:
        count += 1
        result = number

        # Even multiples are skipped, odd multipes are marked false starting from the square of the newly located prime
        is_prime[number*number:limit:number*2] = [False] * ((limit - 1 - number*number) // (number*2) + 1)
    number += 2

print(result)