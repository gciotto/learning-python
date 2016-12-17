from math import sqrt
v = [2, 4, 9, 16, 25]

# Alternative 1
res = []
for x in v:
    res.append(sqrt(x))
print ("Alternative 1: ", res)

# Alternative 2
res = list(map (sqrt, v))
print ("Alternative 2: ", res)

# Alternative 3
res = [sqrt(x) for x in v]
print ("Alternative 3: ", res)