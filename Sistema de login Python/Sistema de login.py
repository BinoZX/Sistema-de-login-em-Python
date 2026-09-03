#Bibliotecas

from time import sleep

# Variaveis de login armazenada

usuario = 0
usuario2 = 0
senha = 0
senha2 = 0

# Sistema do menu
while True:
    print("""\033[34m
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    [1] Criar uma conta
    [2] Entrar 
    [3] Sair do programa
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m""")

# Criação da conta

    menu = int(input("\033[35mOpção: \033[m"))
    if menu == 2 and usuario == 0 and usuario2 == 0:
        print("\033[31mCrie sua conta primeiro!\033[m")
        sleep(1)

    elif menu == 1:
        while True:

            usuario = input("\033[35mEscolha um nome de usuário: \033[m")
            usuario2 = input("\033[35mConfirme o nome de usuário: \033[m")
            sleep(1)
            if usuario == usuario2:
                print("\033[32mUsuario criado com sucesso!\033[m")
                sleep(1)
                print("\033[32mAgora crie sua senha.\033[m")
                sleep(1)
                while True:
                    senha = input("\033[35mEscolha uma senha: \033[m")
                    senha2 = input("\033[35mConfirme sua senha: \033[m")
                    if senha == senha2:
                        sleep(1)
                        print("\033[32mSenha criada com sucesso!\033[m")
                        sleep(1)
                        break
                    else:
                        print("\033[31mAs senhas precisam ser iguais!\033[m")
                        sleep(1)
                break

            else:
                print("\033[31mOs dois usuarios precisam ser iguais!\033[m")
                sleep(1)

# Sistema de login

    elif menu == 2:
        while True:
            validar_login = input("\033[35mUsuario: \033[m")
            if validar_login == usuario:
                while True:
                    validar_senha = input("\033[35mSenha: \033[m")
                    if validar_senha == senha:
                        print("\033[32mLogado com Sucesso!\033[m")
                        break
                    else:
                        print("\033[31mSenha ou login incorretos, tente novamente!\033[m")
                        sleep(1)
                break
            else:
                print("\033[31mLogin ou senha incorretos, tente novamente!\033[m")
                sleep(1)
# Encerrando o programa
    elif menu == 3:
        print("\033[31mSaindo do programa!\033[m")
        break
    else:
        print("\033[31mDigite uma opção válida!\033[m")
        sleep(1)

