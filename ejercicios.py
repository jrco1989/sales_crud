mensaje='cántaros vacíos'
codificado=[]
for i in mensaje:
	codificado.append(ord(i))#el método chr() es el inverso de ord()
	print ('la letra {} tiene un unicode de: {}'.format(i,ord(i)))
print ('{}: unicode de cada letra del menaje anterior = {}'.format(mensaje,codificado))
