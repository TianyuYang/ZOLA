Homework 4, problem 2, part 1
y = prime_range(10^7)
n = len(prime_range(10^7))
p = []
x = []
for i in range(n):
    m = mod(y[i],15)
    p.append(m)
p
stats.TimeSeries(p).plot_histogram()


Homework 4, problem 2, part 2
#From the graph that we can see the results that we get are [1,2,4,7,8,11,13,14], this
# is only happened when the number is greater than 15. Thus, when the sequences of number starts greater
# than 15 then the result of the number are prime relative to the number n, which is 15.
# for the number less than 15, we have the same number. Of course all the results we get will less than 15.
# example: [1,2,4,7,8,11,13,14] are all prime relative to 15.

Homework 4, problem 2, part 3
r = 33
y = prime_range(10^7)
n = len(prime_range(10^7))
p = []
x = []
for i in range(n):
    m = mod(y[i],r)
    p.append(m)
stats.TimeSeries(p).plot_histogram()
# Output results for n = 20  :[1,3,7,9,11,13,17,19]
# Output results for n = 33 :[1,2,4,5,7,8,10,13,14,16,17,19,20,23,25,26,28,29,31,32]
# After trying several numbers, all the results prove that my conjecture, that the results are  all the numbers
# whivh less than the givan the given number n, and prime relative to the nan the given number n, and prime relative to the n.