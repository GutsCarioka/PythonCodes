conta_normal = True
conta_universitaria = False
conta_especial= True 
saldo = 2000
saque = 500 
cheque_especial = 450




if conta_normal:
    if saldo>= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")
    else:
        print("Não pode sacar ")
elif conta_universitaria: 
    if saldo >= saque: 
        print("saque realizado com sucesso ")
    else:
        print("Saldo insuficiente")
elif conta_especial :
    print("Conta Espécial selelcionada com sucesso ")
else:
    print("Favor informar uma conta valida")