def func(*args):
	lst = args
	if type(args[0]) == tuple:
		lst = args[0]
	summa = 0
	for i in lst:
		summa = summa + i
	return summa

print(func((1,2,4,2))) 
