alpha = 1; beta = 2   #manually create the first 2 terms of the sequence
fibonacci = []
current_term = 0

while beta <= 4000000:
    current_term = alpha + beta     #update the values of alpha and beta as required
    alpha = beta
    beta = current_term
    if current_term % 2 == 0:     
        fibonacci.append(current_term)

fibonacci.append(2)          #adding the original 2nd term that is not added during the loop
print(sum(fibonacci))