nome =  "Gabriel" 
idade = 28
profissao = "Programador" 
linguagem = "Python"
saldo = 45.435
dados = {"nome: ": "Gabriel","idade":22} 

print("Nome:%s idade: %d " % (nome,idade)) # format usando o % Antigo e pouco utilizado, tem que estar no seguimento certo 
print("Nome:{} idade: {}".format(nome,idade)) #Format com .format, tem que estar no seguimento certo.

print("Nome:{1} idade: {0}".format(nome,idade)) #Format com .format e numeros. Não precisa seguir sequencia alguma só ter o numero referente a variavel
print("Nome:{1} idade: {0} Nome {1} {1}".format(nome,idade)) #Não causa erro por sequencias ou repetiçoes 
print("Nome:{nome} idade: {idade}".format(nome=nome,idade=idade)) 
print("Nome:{name} idade: {age}".format(age=idade,name=nome)) 
print("Nome:{nome} idade: {idade}".format(**dados)) #usando Dicionario
print(f"Nome:{nome} idade: {idade}")# mais usado basta usar o F e o nome das variaveis 
print(f"Nome:{nome} idade: {idade} saldo:{saldo: 10.2f}")# formataçãp de numeros com 10 = espaços antes da virgula "." =  sendo a virgula e 2f sendo qantos pontos mostrara antes da virgula 
