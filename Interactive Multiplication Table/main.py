while True:
    try:
        numero = int(input("Digite um número para ver sua tabuada: "))
        print(f"\nTabuada de {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    continuar = input("\nDeseja ver outra tabuada? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Obrigado por usar!")
        break
