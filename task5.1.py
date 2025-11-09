x = 2

result = 0
if x >= 0:
    result = x**0.5 + x**2
else:
    result = 1/x

print("{:.2f}".format(float(result)))