def Pitagoras(co,ca):
    hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
    print(f"\nValor da hipotenusa é: {hipotenusa}")

if __name__ == '__main__':
    while True:
        print("Calculando a hipotenusa\n")

        co = float(input("Digite o valor do Cateto Oposto: "))
        ca = float(input("Digite o valor do Cateto Adjacente: "))

        Pitagoras(co,ca)

        continua = input("\nDeseja sair? Digite s ou Enter para um novo cálculo: \n")
        if (continua == 's'):
            break