dia = int(input("Digite um dia da semana: "))

match dia:
    case "segunda":
        print("Dia útil")
    case "terça":
        print("Dia útil")
    case "quarta":
        print("Dia útil")
    case "quinta":
        print("Dia útil")
    case "sexta":
        print("Dia útil")
    case "sábado":
        print("Fim de semana")
    case "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")