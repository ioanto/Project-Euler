numbers = [x for x in range(100, 1000)] # Generate all 3-digit numbers

reversed_numbers = [str(y)[::-1] for y in numbers] # Reverse the above generated numbers

palindromes = [str(num) + rev for num, rev in zip(numbers, reversed_numbers)] # Generate all relevant palindromes

palindromes_as_int = list(map(int, palindromes)) # Cast the palindromes as numbers instead of strings
palindromes_found = []

for i in range(1000, 101, -1): # Reversing the search space might yield faster performance. Larger numbers multipled = larger result
    for k in range(1000, 101, -1):
        product = i * k
        if product in palindromes_as_int and product not in palindromes_found:
            palindromes_found.append(product)
            break # Due to the reversed search space for both outer and inner loop, breaking the inner loop on the first 'hit' ensures we have found the largest palindrome resulting from the current 'i'

palindromes_found.sort()
print(palindromes_found[-1])