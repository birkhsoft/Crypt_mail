# codigo por BirkhSoft
# birkhsoft.sytes.net

print "@@@@@@@@@@@@@@@@@@@@@@@@@"
print "@.........code..........@"
print "@                       @"
print "@..........by...........@"
print "@                       @"
print "@.......BirkhSoft.......@"
print "@@@@@@@@@@@@@@@@@@@@@@@@@"
print ""
print ""

abc = 'abcdefghijklmnopqrstuvwxyz1234567890*+-/%&()=:"!?,.@;-¿¡ '

def descifrar(cadena, clave):
	text_cifrar = ''

	i = 0
	for letra in cadena:
		suma = abc.find(letra) - abc.find(clave[i % len(clave)])
		modulo = int(suma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1

	return text_cifrar

def main():
	c = str(raw_input('cadena a descifrar: ')).lower()
	clave = str(raw_input('clave: ')).lower()
	print descifrar(c,clave)

if __name__ == '__main__':
	main()

