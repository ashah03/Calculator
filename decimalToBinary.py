dec = int(input("Enter a decimal number: "))
which_place = []
bin = 0
while dec > 0:
    i = 1
    while 2**i <= dec:
        i += 1
    i -= 1
    which_place.append((i))
    dec -= 2**i
for i in which_place:
    bin += 10**i
print(bin)