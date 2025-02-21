opcao = -1

while opcao != 0:
    opcao = int(input("[1] recarregar \n[2] falar com a atendente \n[0] Sair \n: "))

    if opcao == 1:
        print("recarregando...")
    elif opcao == 2:
        print("chamando a atendente...")
else:
    print("Obrigado por usar nossa operadora, até logo!")