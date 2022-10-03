from statistics import median
rv = []

for i in range(7):
    element = int(input('enter the number :'))
    rv.append(element)

print(median(rv))
