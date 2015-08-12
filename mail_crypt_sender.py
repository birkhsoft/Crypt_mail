# -*- coding: utf-8 -*-
# codigo por BirkhSoft
# birkhsoft.sytes.net

import os
import smtplib
import time

abc = 'abcdefghijklmnopqrstuvwxyz1234567890*+-/%&()=:"!?,.@;-¿¡ '

os.system("cls") #canviar cls por clear si se usa en sistemas UNIX.

print ""
print ""
print "                  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"
print "                  |-|                               |-|"
print "                  |-|          Crypt_Mail           |-|"
print "                  |-|                               |-|"
print "                  |-|   http://birkhsoft.sytes.net  |-|"
print "                  |-|                               |-|"
print "                  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"
print ""
print ""

time.sleep(1.3)

clave = str(raw_input('Introduce la contrasena con la que se cifraran los mensajes que envies: ')).lower()
print "Tu contrasena es: " + clave
print "No olvides la contrasena!"

time.sleep(4)

def cifrar(cadena, clave):
	text_cifrar = ''

	i = 0
	for letra in cadena:
		suma = abc.find(letra) + abc.find(clave[i % len(clave)])
		modulo = int(suma) % len(abc)
		text_cifrar = text_cifrar + str(abc[modulo])
		i=i+1

	return text_cifrar

def menu():
	
	os.system('cls') # Si este escript se usa en linux pongan clear
	print ""
	print ""
	
	print "                  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"
	print "                  |-|                               |-|"
	print "                  |-|          Crypt_Mail           |-|"
	print "                  |-|                               |-|"
	print "                  |-|   http://birkhsoft.sytes.net  |-|"
	print "                  |-|                               |-|"
	print "                  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|"
	print ""
	print ""

	print "Seleccione el tipo de correo que desea usar"
	print "\t1 - Gmail"
	print "\t2 - Hotmail"
	print "\t3 - Yahoo"
	print "\t9 - salir"
 
 
while True:
	
	menu()

	
	opcionMenu = raw_input("inserta un numero del menu >> ")
 
	if opcionMenu=="1":
		print "Ha decidido usar el correo Gmail"
		print "Introduce tu correo eletronico:"
		correo_gmail = raw_input()
		print "El correo introducido es:", correo_gmail 
		print "Introduce tu contrasena:"
		password_gmail = raw_input()
		print "Contrasena introducida con exito!"
		print "Escriba el destinatario del correo:"
		destino_gmail = raw_input()
		print "El correo sera enviado a:", destino_gmail
		print "Ahora solo le queda introducir el mensaje que llevara el correo:"
		content = raw_input()

		c = str(content).lower()

		m_cifrado = cifrar(c,clave)

		mail = smtplib.SMTP('smtp.gmail.com',587)

		mail.ehlo()

		mail.starttls()

		mail.login(correo_gmail,password_gmail)

		mail.sendmail('fromemail',destino_gmail,m_cifrado)
		print "CORREO ENVIADO CON EXITO!"
		mail.close()


	elif opcionMenu=="2":
		print "Ha decidido usar el correo Hotmail"
		print "Introduce tu correo eletronico:"
		correo_hotmail = raw_input()
		print "El correo introducido es:", correo_hotmail
		print "Introduce tu contrasena:"
		password_hotmail = raw_input()
		print "Contrasena introducida con exito!"
		print "Escriba el destinatario del correo:"
		destino_hotmail = raw_input()
		print "El correo sera enviado a:", destino_hotmail
		print "Ahora solo le queda introducir el mensaje que llevara el correo:"
		content_hotmail = raw_input()

		c = str(content_hotmail).lower()

		m_cifrado = cifrar(c,clave)

		mail = smtplib.SMTP('smtp.live.com')

		#debuglevel = True                          #puede desmarcar el comentario si decide ver el proceso que se lleva acabo para enviar su correo
		#mail.set_debuglevel(debuglevel)            #puede desmarcar el comentario si decide ver el proceso que se lleva acabo para enviar su correo

		mail.starttls()

		mail.login(correo_hotmail, password_hotmail)

		mail.sendmail(correo_hotmail, destino_hotmail, m_cifrado)
		print "CORREO ENVIADO CON EXITO!"
		mail.close()

	elif opcionMenu=="3":
		print "Ha decidido usar el correo Yahoo"
		print "Introduce tu correo eletronico:"
		correo_yahoo = raw_input()
		print "El correo introducido es:", correo_yahoo
		print "Introduce tu contrasena:"
		password_yahoo = raw_input()
		print "Contrasena introducida con exito!"
		print "Escriba el destinatario del correo:"
		destino_yahoo = raw_input()
		print "El correo sera enviado a:", destino_yahoo
		print "Ahora solo le queda introducir el mensaje que llevara el correo:"
		content_yahoo = raw_input()

		c = str(content_yahoo).lower()

		m_cifrado = cifrar(c,clave)

		mail = smtplib.SMTP('smtp.mail.yahoo.com',587)

		#debuglevel = True                       #puede desmarcar el comentario si decide ver el proceso que se lleva acabo para enviar su correo
		#mail.set_debuglevel(debuglevel)         #puede desmarcar el comentario si decide ver el proceso que se lleva acabo para enviar su correo

		mail.starttls()

		mail.login(correo_yahoo,password_yahoo)

		mail.sendmail(correo_yahoo, destino_yahoo, m_cifrado)
		
		mail.close()

	elif opcionMenu=="9":
		break
	else:
		print ""
		raw_input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")