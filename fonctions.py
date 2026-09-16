def puissance(a, b):
	res=a
	if not type(a) is int and not type(b) is int:
		raise TypeError("Only integers are allowed") #inutile car input a besoin de typecasting pour fonctionner
	if a == 0 and b < 0:
		raise ValueError("0 cannot have a negative exponent")
	else:
		if b>0:
			for i in range(b):
				res*=a
		if b<0:
			for i in range(b):
				res/=a
		return res
