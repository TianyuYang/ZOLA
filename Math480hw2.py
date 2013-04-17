
def factors(n):
	result = []
	for i in range(1, n+1):
		if n % i == 0:
			result.append(i)
	return result
	
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-2) + fibonacci(n-1)
	print fibonacci(n)
	
	
def cal_cd_cm(a,b):
  	n = min(a,b)
	m = max(a,b)
	r = 0
	if (a < b):
		t = a
		a = b
		b = t
	r = a % b
	while( r != 0):
		a = b
		b = r
		r = a % b
	print "The greatest common divisor is %5.1f." % b
	print "The least common multiple is %5.1f." % ((m*n)/b)
	print "The factors of two input numbers :"
	print factors(m)
	print factors(n)
	print "The fibonacci numbers of two input numbers :"
	print fibonacci(m)
	print fibonacci(n)



