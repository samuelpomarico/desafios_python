menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
                saldo += valor
                extrato += f"Depósito : R$ {valor: .2f} \n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_valor_saque = valor > 500
        excedeu_limite_saque = numero_saques > LIMITE_SAQUE

        if valor <= 500:
              saldo -= valor
              numero_saques += 1
              extrato += f"Saque : R$ {valor: .2f} \n"
        
        elif excedeu_saldo:
              print("O saque excede o valor disponóivel em conta.")
    
        elif excedeu_valor_saque:
                print("O saque limite é de R$500,00")

        elif excedeu_limite_saque:
                print("Você atingiu o número máximo de saques por dia.")
        
        else:
            print("Operação falou, valor informado é inválido!")
    
    elif opcao == "e":
          print("\n========== EXTRATO ==========")
          print("Não houve movimentações" if not extrato else extrato)
          print(f"\n Saldo: R${saldo:.2f}\n")
          print("===============================")

    elif opcao == "q":
          print("Obrigado por usar nosso banco!")
          break

    else:
        print("Operação falou, slecione uma operação válida!")     
        
         