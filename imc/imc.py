import time
while True:
    print("1- Calculadora IMC\n2- Sair")
    option = input("Opção: ")
    if option == "1":
        print("|-=-=-=-Calculadora de IMC-=-=-=-|")
        print("Fonte das classificações www.tuasaude.com/imc/\n")
        time.sleep(0.5)

        nome_paciente = input("Nome Completo: ")
        idade_paciente = int(input("Idade: "))
        altura_paciente = float(input("Altura: "))
        peso_paciente = float(input("Peso: "))

        """ print(type(idade_paciente))
        print(type(peso_paciente))
        print(type(altura_paciente)) """

        imc = peso_paciente / altura_paciente ** 2

        if imc < 18.5:
            tipo_imc = "Magreza"
        elif imc >= 18.5 and imc <= 24.9:
            tipo_imc = "Peso Normal"
        elif imc >= 24.9 and imc <= 30:
            tipo_imc = "Sobrepeso"
        else: # Maior que 110.6kg
            tipo_imc = "Obesidade"

        print(f'Resultado:\nIMC paciente é de {imc:.2f}kg\m²\n')
        
    elif option == "2":
        print("Saindo...")
        break
    else:
        print("Opção invalida.")
        
