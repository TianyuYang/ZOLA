Homework 4, problem 1
Since the n in in z, the set of f(n) will be infinite set.
thus i took a example that range n from -500000 to 500000
i = 1
x = []
for i in [-500000..500000]:
    y = i*i + 2*i + 3
    i = i+1
    if y.is_prime() == true:
        x.append(y)
x
