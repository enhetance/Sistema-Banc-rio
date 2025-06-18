saldo = 1000.0 # Saldo inicial

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo # Indica que a variável global saldo está sendo modificada
    valor_saque = float(input("Digite o valor a sacar: R$ "))
    if valor_saque <= saldo:
	saldo -= valor_saque
	print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    else:
	print("Saldo insuficiente.")

def depositar():
    """Realiza a operação de depósito."""
    global saldo
    valor_deposito = float(input("Digite o valor a depositar: R$ "))
    saldo += valor_deposito
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")

while True:
	# Exibir mensagem de boas-vindas e as opções do menu
	print("\nOlá! Bem-vindo ao seu banco virtual.")
	print("--------------------------------------")
	print("1 - Consultar Saldo")
	print("2 - Depositar")
	print("3 - Sacar")
	print("4 - Sair")
	print("--------------------------------------")

	# Ler a opção do usuário
	opcao_str = input("Digite a opção desejada: ")

	# Validar a opção do usuário usando um laço while
	while not opcao_str.isdigit() or not (1 <= int(opcao_str) <= 4):
	    print ("Opção inválida. Por favor, digite um número entre 1 e 4.")
	    opcao_str = input("Digite a opção desejada: ")

	opcao = int(opcao_str)

	# Executar a ação com base na opção do usuário
	if opcao == 1:
	   consultar_saldo()
	elif opcao == 2:
	   depositar()
	elif opcao == 3:
	   sacar()
	elif opcao == 4:
	   print("Obrigado por utilizar nosso banco virtual!")
	   break # Sai do laço while, encerrando o programa
