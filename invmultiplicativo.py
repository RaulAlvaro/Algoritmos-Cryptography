import math
#a1 = r0 && b1 = r1
#Hallando los q's
r0 = int(input("Ingresa el módulo: "))
r1 = int(input("Ingrese el número: "))

a1 = r0
b1 = r1
lq = []
while (a1 % b1 != 0):
	q1 = math.floor(a1/b1)
	c1 = math.floor(a1%b1)
	lq.append(q1)
	a1 = b1
	b1 = c1

# Hallando el inverso multiplicativo
lt = [0,1]
print(lq)
for j in range(2,(len(lq)+2)):
	num = (lt[j-2] - lq[j-2]*lt[j-1]) % r0
	lt.append(num)
pass

print(lt)
print("El resultado es: ", lt[-1])