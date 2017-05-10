def fn(a,b,c):
	if c == "+":
		return a+b;
	elif c == "-":
		return a-b;
	elif c == "*":
		return a*b;
	elif c == "/":
		return a/b;
	else:
		return "Unknown"

print(fn(2,3,"+"))
