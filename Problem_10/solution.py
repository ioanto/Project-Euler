# For the solution we can turn to Problem #7's solution and the modified Sieve of Eratosthenes implementation.
# The same approach is used here with some minor changes.
# Instead of a prime counter, now there's a prime summation variable to appropriately handle what is required by the problem.

limit = 2000000
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

primes_sum = 2    # prime summation, updates iteratively
candidate = 3    # prime candidate being checked, increases iteratively

while candidate < limit:
    if is_prime[candidate]:
        primes_sum += candidate

        # Skip even multiples, mark odd multiples as false starting from the square of the newly located prime
        is_prime[candidate*candidate:limit:candidate*2] = [False] * ((limit - 1 - candidate*candidate) // (candidate*2) + 1)
    
    candidate += 2

print(primes_sum)