lista = [1, "Python", [40, 30 , 20] ]

l2 = lista.copy () 

print(lista) 

print(id(l2), id(lista)) #Mostrara identificadores diferentes comprovando que realmente foi feito uma copia da lista 

l2[0] = 2 

print(l2)