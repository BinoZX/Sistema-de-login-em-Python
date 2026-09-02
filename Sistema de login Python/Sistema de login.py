#Bibliotecas
import time

#Menu
while True:
    print("""\033[34mEscolha uma opção.
[1] Criar uma conta
[2] Entrar 
[3] Sair do programa\033[m""")

    #Criação da conta

    menu = int(input("Opção: "))
    if menu == 1:
        while True:

            usuario = str(input("\033[35mEscolha um nome de usuário: \033[m"))
            usuario2 = str(input("\033[35mConfirme o nome de usuário: \033[m"))

            time.sleep(1)

            if usuario == usuario2:
                print("\033[32mUsuario criado com sucesso!\033[m")
                time.sleep(1)
                print("\033[32mAgora crie sua senha.\033[m")
                time.sleep(1)
                while True:
                    senha = str(input("\033[35mEscolha uma senha: \033[m"))
                    senha2 = str(input("\033[35mConfirme sua senha: \033[m"))
                    if senha == senha2:
                        time.sleep(1)
                        print("\033[32mSenha criada com sucesso!\033[m")
                        time.sleep(1)
                        break
                    else:
                        print("\033[31mAs senhas precisam ser iguais!\033[m")
                        time.sleep(1)
                break


            else:
                print("\033[31mOs dois usuarios precisam ser iguais!\033[m")
                time.sleep(1)

#Sistema de login

    elif menu == 2:
        while True:
            validar_login = str(input("\033[35mUsuario: \033[m"))
            if validar_login == usuario:
                while True:
                    validar_senha = str(input("\033[35mSenha: \033[m"))
                    if validar_senha == senha:
                        print("\033[32mLogado com Sucesso!\033[m")
                        break
                    else:
                        print("\033[31mSenha incorreta, tente novamente!\033[m")
                        time.sleep(1)
                break
            else:
                print("\033[31mLogin incorreto, tente novamente!\033[m")
                time.sleep(1)
#Encerrando o programa
    else:
        print("\033[31mSaindo do programa!\033[m")

        break

