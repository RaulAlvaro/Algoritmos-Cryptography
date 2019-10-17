import random
import math

def potenciacion(x,b,n):
	b_to_bin = bin(b)
	b_to_bin = b_to_bin[2:]
	b_to_bin = b_to_bin[::-1]
	z = 1
	for i in range(len(b_to_bin)-1, -1, -1):
		z = z**2 % n
		if b_to_bin[i] == '1':
			z = z * x % n
	return z


n = input("Ingresa el número: ")

if (n[-1] != '1') and (n[-1] != '3') and (n[-1] != '7') and (n[-1] != '9'):
	print("Es compuesto")
else:
	n = int(n)
	#k = 1
	#m = 1
	#ispar = False
	#35797
	#Obtencion de k y m es ineficiente
	"""
	while (2**k)*m < n-1 or (ispar==False):
		print('El valor de k es',k)
		while (2**k)*m < n-1:
			m = m+1
			print('El valor de m es',m)
			print('2**k*m es', (2**k*m))
		if (2**k)*m == n-1 and (m%2 != 0):
			ispar = True
		else:
			k = k+1
			m = 1
	"""
	ntemp = n-1
	k = 0
	m = 0
	while ntemp % 2 == 0:
		if ntemp%2 == 0:
			k = k + 1
			print("El valor de k es: ", k)
			ntemp = ntemp/2
			print("El valor de ntemp es: ", ntemp)
	m = int(ntemp)
	k = int(k)
	print('El valor de k es',k)
	print('El valor de m es', m)

	a = random.randint(1, n-1)
	#a = 10

	#b = (a**m) % n
	b = potenciacion(a,m,n)

	print("El valor de b es", b)

	if b == 1 % n:
		print("El numero es primo")
	
	else:
		i = 0
		iscomp = False

		for i in range(k):
			if b == -1 % n:
				iscomp = True
			else:
				b = b**2 % n
				iscomp = False

		if (iscomp == False):
			print("El numero es compuesto")
		else:
			print("El numero es primo")



