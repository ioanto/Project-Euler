number = 600851475143
divisor = 3 # Starting with 1 is unnecessary for obvious reasons. 2 can be skipped as 600851475143 is an odd number.

while divisor * divisor <= number: # The squared divisor is important due to the property of only needing to check till the square root of 600851475143.
    if number % divisor:
        divisor += 2 #it's possible to increment by 2 because the given number is odd and thus besides 2, all other even numbers can be skipped.
    else:
        number //= divisor # floor division so it's guaranteed that the outcome will never be a float number.

print(number)