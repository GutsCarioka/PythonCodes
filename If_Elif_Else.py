MAIOR_IDADE = 18 
IDADE_ESPECIAL = 12

idade = (int(input("Informe a sua idade: ")))

if idade>= MAIOR_IDADE:
    print("Maior de idade, Pode tirar carteira. ")

if idade < MAIOR_IDADE:
    print("Menor de idade, Não pode tirar carteira.") 


if idade>= MAIOR_IDADE:
    print("Maior de idade, Pode tirar carteira. ")
else:
     print("Menor de idade, Não pode tirar carteira.")
     
     
if idade>= MAIOR_IDADE:
    print("Maior de idade, Pode tirar carteira. ")
elif idade == IDADE_ESPECIAL:
    print("Pode Ter aulas praticas")
else:
     print("Menor de idade, Não pode tirar carteira.")