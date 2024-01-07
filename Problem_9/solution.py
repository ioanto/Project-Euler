# This problem can be solved by combining what the statement provides.

for alpha in range(1, 334):       # a < b < c and a + b + c = 1000 therefore a < 333.33
    
    # Beta is generated as follows:
    # Using a + b + c = 1000 (1) and a^2 + b^2 = c^2 (2)
    # Solving (1) for c --> c = 1000 - a - b
    # Substituting that into (2) --> a^2 + b^2 = (1000 - a^2 - b^2)^2
    # Solving the above for b yields b = \frac{1000 * (500 - a)}{1000 - a} (3)
    
    beta = (1000 * (500 - alpha)) / (1000 - alpha) 
    if beta.is_integer():       # b needs to be a natural number
        gamma = 1000 - alpha - beta
        print(int(alpha * beta * gamma))
        break       # Equation (3) ensures that only 1 such b exists, thus on the first 'hit' that b is located