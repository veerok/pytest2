import math
def square(w,h):
	perimeter = w*2 + h*2
	sqr = w*h
	diag = math.sqrt(w*2 + h*2)
	return (perimeter, sqr, diag)

print( square(10, 10) )
