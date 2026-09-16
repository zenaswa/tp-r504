def puissance(a, b):
	if not type(a) is int and not type(b) is int:
		raise TypeError("Only integers are allowed") #inutile car input a besoin de typecasting pour fonctionner
	if a == 0 and b < 0:
		raise ValueError("0 cannot have a negative exponent")
	else:
		return a**b
