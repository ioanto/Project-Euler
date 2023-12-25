i = 1
multiples = []

while i < 1000:
    if i % 5 == 0 or i % 3 == 0:
        multiples.append(i)
    i += 1

print(sum(multiples))