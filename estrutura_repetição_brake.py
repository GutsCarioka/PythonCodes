while True: #While infinito.
    numero = int(input("Informe um numero: "))
    
    if numero == 10:
        break #Utilizado para parar a execução assim que receber o numero 10 
    
    if numero %2 == 0: 
        continue #utilizado para pular um numero na execução 
    
    print(numero)