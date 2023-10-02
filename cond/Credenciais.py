login = str(input("Digite seu login: "))
senha = str(input("Digite a sua senha: "))
match(login, senha):
    case ("Emilly", "123"):
        print("Usuario logado com sucesso")

    case ("Gabrielly", "192"):
        print("Administradora logada com sucesso")

    case _:
        print("Login ou senha incorreto")
