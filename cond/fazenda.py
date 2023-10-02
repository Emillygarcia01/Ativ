animal =str(input("Digite o nome de um animal: "))

match animal:
    case "vaca":
        print("É uma vaca.")
    case "galinha":
        print("É uma galinha.")
    case "ovelha":
        print("É uma ovelha.")
    case _:
        print("Animal desconhecido.")