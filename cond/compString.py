string1 = str(input("Insira a primeira string: "))
string2 = str(input("Insira a segunda string: "))

match string1, string2:
    case ("hello",_):
        print("A primeira string é 'hello' e a segunda é qualquer outra coisa.")
    case (_, "world"):
        print("A segunda string é 'world' e a primeira é qualquer outra coisa.")
    case (string2,string1):
        print("Ambas as strings são iguais.")
    case _:
        print("Nenhuma das condições é satisfeita.")