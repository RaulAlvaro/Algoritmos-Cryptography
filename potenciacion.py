x = int(input("Ingresa el número: "))
b = int(input("Ingrese el exponente: "))
n = int(input("Ingresa el módulo: "))

b_to_bin = bin(b)
b_to_bin = b_to_bin[2:]
b_to_bin = b_to_bin[::-1]

z = 1

#print(b_to_bin)

for i in range(len(b_to_bin)-1, -1, -1):
	#print('Estamos en la iteracion: ', i)
	z = z**2 % n
	if b_to_bin[i] == '1':
		z = z * x % n
	#print(z)
print('El valor final de z es:', z)
