tentativas = []

def registrarTentativas():
    tentativas.clear()
    for i in range(10):
        v = int(input(f"Arremesso {i+1} (0 a 3): "))
        while v not in [0, 1, 2, 3]:
            v = int(input("Inválido! Digite 0, 1, 2 ou 3: "))
        tentativas.append(v)

def calcularPontuacao():
    return sum(tentativas)

def calcularAproveitamento():
    acertos = len([x for x in tentativas if x > 0])
    return (acertos / 10) * 100

def encontrarCestaMaisFrequente():
    qtds = [tentativas.count(1), tentativas.count(2), tentativas.count(3)]
    maior = max(qtds)
    if maior == 0: return "Nenhuma"
    tipos = ["1pt", "2pts", "3pts"]
    return tipos[qtds.index(maior)]

while True:
    print("\n1- Registrar | 2- Ver | 3- Sair")
    op = input("Opção: ")
    if op == "1": registrarTentativas()
    elif op == "2":
        print("Pontos:", calcularPontuacao(), "| Aproveitamento:", calcularAproveitamento(), "%")
        print("Mais frequente:", encontrarCestaMaisFrequente())
    else: break