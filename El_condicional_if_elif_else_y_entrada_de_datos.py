edad = int(input("¿Cual es tu edad?"))   #pide la edad 
if edad <= 0:
	print("Nadie puede tener esa edad.")   #esta condicion es para si tiene igual o amro que a 0
elif edad <= 1 and edad <= 18:
	print('Eres menor de edad.')    #esta condicion es para si es menor que 18
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')   #este es cuando la edad se msaoy que 100
else:
	print('Edad no valida.')
