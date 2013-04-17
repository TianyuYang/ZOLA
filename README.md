ZOLA
====
def cal_cd(a,b):
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
	#c = n * m / r
	print "The greastest common divisor is %5.1f." % b
	print "The least common multiple is %5.1f." % ((m*n)/b)

def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-2) + fibonacci(n-1)
	print fibonacci(n)


