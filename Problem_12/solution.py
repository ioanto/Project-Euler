# An elegant solution for this problem is leveraging the fact that the nth triangular number can be expressed as n * (n + 1) / 2
# The numerator is a product, for which the nth triangular number is present in both terms
# Generating the divisors of the two terms of the product provides an efficient solution

target_divisors = 500
n = 1

while True:
    # Calculate divisors for n and (n + 1)
    divisors_n = sum(2 for i in range(2, int(pow(n, 0.5)) + 1) if n % i == 0)
    divisors_n_plus_1 = sum(2 for i in range(2, int(pow(n, 0.5)) + 1) if (n + 1) % i == 0)

    # Calculate the total number of divisors
    total_divisors = divisors_n * divisors_n_plus_1

    if total_divisors > target_divisors:
        # Calculate the corresponding triangular number
        triangular_number = n * (n + 1) // 2
        # Print the result and break out of the loop
        print(triangular_number)
        break

    n += 1