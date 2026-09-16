def puissance(a, b):
	if not type(a) is int and not type(b) is int:
		raise TypeError("Only integers are allowed") #inutile car input a besoin de typecasting pour fonctionner
	else:
		return a**b
