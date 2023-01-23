import time
import os
import random
""" user_operador_padrao = "ban_0001"
with open("password.txt", "r") as f:
    password_txt = f.read() """

print("-" * 5 + "[Bank of American]" + "-" * 5)
time.sleep(0.5)

user_operador = input("Operador: ")
password_operador_1 = input("Password: ")
if user_operador == "ban_001" and password_operador_1 == "operador2023":
    print("Acesso permitido, carregando sistema...")
    time.sleep(0.3)
    os.system("cls")

    while True:
        print("Menu\n1-Abertura de conta\n2-Emprestimos\n3-Cartão de credito\n4-Sair")
        option = input("Opção: ")
        if option == "1":
            maior_idade = 18
            idade_client = int(input("Informe sua idade: "))
            if idade_client >= maior_idade:
                os.system("cls")
                nome_client = input("Nome completo: ")
                cpf_client = int(input("CPF: "))
                renda_minima = 2400
                renda = int(input("Renda: "))
                if renda >= renda_minima:
                    andress_client = input("Endereço: ")
                    cep_client = input("CEP: ")
                    cidade_client = input("Cidade: ")
                    os.system("cls")
                    print("Confirmação de da dados...\n")
                    print(f"Nome: {nome_client}")
                    print(f"CPF: {cpf_client}")
                    print(f"Idade: {idade_client}")
                    print(f"Renda: R${renda}\n")
                    dados_corretos = input("Os dados estão corretos?[y][n]--->: ")
                    if dados_corretos == "y":
                        print("Enviando dados...\n")
                        time.sleep(0.8)
                        os.system("cls")
                        print("Abertura de conta com sucesso, aqui estão seus dados:\n")
                        print("Banco 018: Bank of American")
                        print(f"Titular {nome_client}")
                        print("Agencia: 0448")
                        conta_corrente = random.randint(64515, 87954)
                        print(f"Conta-corrente: {conta_corrente}")
                        break
                else:
                    print("Sem renda minima")
                    break
            else:
                print("Precisa-se ser maior de idade.")
                break
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            break
        else:
            print("Opção invalida.")
else:
    print("Dados incorretos.")
