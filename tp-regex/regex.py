#!/usr/bin/python3
import re
id=input("\nentrez votre identifiant: ")
cond=0
while(cond==0):
	
	password=input("\nentrez votre mot de passe: ")
	if not re.fullmatch('^.{6,11}$',password):
		print("\nle mdp doit contenir entre 6 et 12 caracteres")
	elif not re.search('\d+', password):
		print("\nle mdp doit contenir au moins un chiffre")
	elif not re.search('[a-z]+', password):
		print("\nle mdp doit contenir au moins une minuscule")
	elif not re.search('[A-Z]+', password):
		print("\nle mdp doit contenir au moins une majuscule")
	elif not re.search('[#%{}@]',password):
		print("\nle mdp doit contenir au moins un de ces caracteres #%{}@")
	else:
		cond=1

print("compte enregistre")
