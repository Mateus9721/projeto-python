gastos = []

while True:
    print("=== MENU ===")
    print("1 - Adicionar gasto")
    print("2 - Ver todos os gastos")
    print("3 - Ver total por categoria")
    print("4 - Sair")
    
    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        nome = input("Digite o nome do gasto: ")
        valor = float(input("Digite o valor (R$): "))
        tipo = input("Digite a categoria (exemplo: comida, transporte): ")
        gasto = {"nome": nome, "valor": valor, "tipo": tipo}
        gastos.append(gasto)
        print("Gasto salvo!\n")

    elif escolha == "2":
        print("Lista de gastos:")
        for item in gastos:
            print(f"{item['nome']} - R${item['valor']} ({item['tipo']})")
        print()

    elif escolha == "3":
        print("Total por categoria:")
        totais = {}
        for gasto in gastos:
            categoria = gasto["tipo"]
            valor = gasto["valor"]
 
            if categoria not in totais:
                totais[categoria] = 0
   
            totais[categoria] += valor

        for categoria in totais:
            print(f"{categoria}: R${totais[categoria]}")
        print()

    elif escolha == "4":
        print("Saindo... até mais!")
        break

    else:
        print("Opção inválida. Tente de novo.\n")