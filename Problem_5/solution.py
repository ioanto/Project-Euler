# An elegant way to solve this problem is by relying on the Lowest Common Multiplier (LCM) and the Greatest Common Divisor (GCD).
# Specifically: LCM(a, b) * GCD(a, b) = a * b
# Calculating GCD first and with that updating 'result' a.k.a the LCM, iteratively over the for loop search space.

result = 20 # Start with 20, the upper bound of our search space

for current_number in range(11, 21): #No need to check all 20 numbers specifically. Checking 11 - 20 indirectly includes all other checks.
    previous_result = result
    current_factor = current_number
    
    # Calculate the greatest common divisor (GCD)
    while current_factor:
        previous_result, current_factor = current_factor, previous_result % current_factor
    
    # Update result with the least common multiple (LCM)
    result *= current_number // previous_result

print(result)