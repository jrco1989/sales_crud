#Declaración que se debe realizar en todos los programas de python 
#el id es la direccion en donde lAS Cvariables o caracteres viven o reposan en la memoria del compurador 
#en las listas, para copiar un alista es mejor user el módulo copy (import copy) y evitar problemas al alterar la lista original pero no queremos uqe la copoia cambie 
#los strings no se dejan cambian remplazando su indice (string[0]=x esto me genera un error)
# la funcion get para diccionarois no spermite manejar los erroeros para evitarlos (ficcionarios.get/('valor a buscar', 'valor por defecto '))
import random #para manejar nuomeros aleatrorios, se usa por ejemolo s.append(random.randint(0,15))
import sys
#clients='javier,ricardo,'primera manera de realizar en ejercicio
clients=['javier','ricardo,']

#

def create_client(client_name):
	global clients #nos permite trabajar o traer una variable global
	if client_name not in clients:
		#clients +=client_name se concatenava para strings 
		clients.append(client_name)
		#_add_comma() #forma de modificar el flujo de trabajo
	else:
		print ('client alrady exist in historial')
"""def _add_comma():
	global clients
	clients+=','"""


def update_client(client_name,update_client_name):
	global clients

	if client_name in clients:#pregunta por una secuencia de caracgteres en otra string 
		#clients=clients.replace(client_name + ',',update_client_name + ',')
		index=clients.index(client_name)
		clients[index]=update_client_name
	
	else:
		print ('client is not in clients list')


def list_clients():
	global clients
	#print (clients)
	for idx, client in enumerate(clients):#enumerate m emuestra la el indice y la variable 
		print ('{}: {}'.format(idx,client))


def _get_name():
	client_name=None #para declarar variables vacias
	while not client_name:#pregunta mientas cliente sea vacio haga....
		client_name= input('what is the client\'s name ')
		if client_name=='exit':#forma no elegante de termina run ciclo
			client_name=None
			break;
	if not client_name:
		sys.exit()#se usa para salir del programa usando el módulo del sistema 
	return client_name


def delete_client(client_name):
	global clients
	if client_name in clients:
		#clients=clientes.replace(client_name+',','')
		clients.remove(client_name)
	else:
		print('cliente existente ')


def search(client_name):
	global clients
	#clients=clients.split(',')#funcion split permite dividir unstring en una lista y recibe un parametro de separador 
	for i in clients:
		"""if i ==client_name:
			return True primer amanera de realizarlo"""
		if i != client_name:
			continue #permite que el programa continue ejecutandose sin realizar ninguna acción 
		else:
			return True


def welcome():
	print ('Wlecome')
	print ('*'*50)
	print ('what would you like to do today?')
	print ('[C] create a new client')
	print ('[D] delete a client')
	print ('[U] Update client')
	print ('[S] search a client')
	print('[L]' 'see the list')

if __name__=='__main__':
	#clients+='castillo' se suprime par auser la función 
	welcome()
	orden=input()
	orden=orden.upper()
	if orden =='C':
		print ('estos son los clientes iniciales: ')
		list_clients()
		client_name=_get_name()
		create_client(client_name)
		list_clients()
	elif orden=='D':
		client_name=_get_name()
		delete_client(client_name)
		list_clients()

	elif orden=='L':
		list_clients()
		
	elif orden=='U':
		client_name=_get_name()
		update_client_name=input('what is the updated client name')
		update_client(client_name,update_client_name)
		list_clients()
	elif orden=='S':
		client_name=_get_name()
		found=search(client_name)
		if found:
			print ('the client is in the clients list')
		else:
			print ('the client: {} is not in clients list'.format(client_name))		


	else:
		print ('invalid command')

	#print ('estos son los clientes iniciales: ')
	
	pass #placehokder para determinar en dónde termina n bloque	



