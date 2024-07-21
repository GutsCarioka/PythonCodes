import textwrap
def menu():
 menu = """
  [1] Depositar 
  [2] Sacar
  [3] Extrato
  [4] Nova conta
  [5] listar Contatos
  [6] Novo usuario
  [0] Sair 
  """
 return input(textwrap.dedent(menu))
















def main(): 
saldo = 0
AGENCIA = "0001"
usuarios = []
contas = []
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 
while True: 
    
    opcao = menu()
  
    if opcao == "1": #Deposito
        deposito = float(input("me informe qual o valor do deposito: "))
        
        if deposito > 0:
            saldo += deposito
            # em extrato ele adicionou o valor de deposito a uma String em uma variavel vazia fazendo com que essa str possa mostrar valores diferentes dependendo de onde forem puxadas.
            extrato, extrato = depositar (saldo,valor,extrato) 
        else:
            print("Valor invalido")

    elif opcao == "2": #saque
       valor = float(input("Informe o valor de saque"))
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite 
       excedeu_saques = numero_saques >= LIMITE_SAQUES 
       
       if excedeu_saldo:
           print("Sem saldo suficiente na conta")
       elif excedeu_limite: 
           print("Você excedeu o valor maximo de saque")    
       elif excedeu_saques:
           print("Você alcançou o nivel maximo de saques ") 
       elif valor > 0 :
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}"
           numero_saques +=1   
       else: 
           print("Favor informar valor valido")
    elif opcao == "3": #extrato
        print("\n============== Extrato ================")
        print("Não foram realizadas movimentaçoes."if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == "0": 
        print("Saiindo..")
        break
    else: 
        print("Por favor escolha uma das opçoes abaixo ")
        