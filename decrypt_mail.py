# -*- coding: utf-8 -*-
# codigo por BirkhSoft
# birkhsoft.sytes.net

import os

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
	
	os.system("cls") #si se usa en sistemas unix canviar cls por clear

	print ""
	print ""
	
	print "                  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"
	print "                  |-|                               |-|"
	print "                  |-|         DeCrypt_Mail          |-|"
	print "                  |-|                               |-|"
	print "                  |-|   http://birkhsoft.sytes.net  |-|"
	print "                  |-|                               |-|"
	print "                  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"
	print ""
	print ""

	c = str(raw_input('Introduce el texto a descifrar: ')).lower()
	clave = str(raw_input('clave: ')).lower()
	print descifrar(c,clave)

if __name__ == '__main__':
	main()

