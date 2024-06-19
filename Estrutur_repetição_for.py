#Utilizado para repetir todas as vezes que se sabe quantas vezes ira repetir o codigo

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


#Exemplo utilizando um itervel 
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: 
    print()
    print("Fim do codigo")

#Exemplo Utilizando a funçao built-in Range 
# expl: range(Inicio,final,passos): 
for numero in range(0,51,5):
    print(numero, end= " ")