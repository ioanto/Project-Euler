# This problem does not rely on any explicit mathematical insights, but leans more on the algorithmic side.
# The solution here involves slicing the original list and creating a 13 slot window with start and end being the flags alpha and beta respectively.
# The process is dependent on the contents of the window.

number_raw = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

number_sliced = [int(x) for x in number_raw]

alpha = 0     # 1st flag
beta = 13     # 2nd flag

product = 1   # iteratively updated product per current window
result = 0    # stores up to current iteration the highest found product

while beta < len(number_sliced):
    candidates = number_sliced[alpha:beta]
    
    # 1st edge case: if a 0 exist in the window, drop it and increment flags by 13 to completely evade it
    if 0 in candidates:
        alpha += 13
        beta += 13
        continue
    
    # 2nd edge case: if the window is comprised by number entirely, this will lead to the highest possible product
    elif all(x == 9 for x in candidates):
        print(pow(9, 13))
        break
    
    # the expected case, calculate product, evaluate against previous highest product found, increment flags
    else:
        for candidate in candidates:
            product *= candidate
        
        result = max(result, product)    
        
        alpha += 1
        beta += 1
        product = 1

print(result)