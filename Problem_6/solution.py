# The most elegant solution possible for this problem is to directly leverage the following 2 formulas
# A = \frac{n (n + 1)}{2} and B = \frac{n (n + 1) (2n + 1)}{6}
# Expression A or better known as Gauss Sum provides us the sum of the first n natural numbers, Expression B provides the sum of their squares

sum_of_squares = (100 * (100 + 1) * (2 * 100 + 1)) / 6

square_of_sum = pow((100 * (100 + 1)) / 2, 2)

print(int(square_of_sum - sum_of_squares))