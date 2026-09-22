jogadores = ["Lucas", "flury", "Pietro+Pietra", "Enzo Candido", "Viadante"]
gols = [4, 7, 2, 7, 5]

def calcularTotalGols():
    return sum(gols)

def calcularMediaGols():
    return sum(gols) / len(gols)

def encontrarArtilheiros():
    maior = max(gols)
    return [jogadores[i] for i in range(5) if gols[i] == maior]

def mostrarRelatorio():
    for i in range(5):
        print(f"{jogadores[i]}: {gols[i]} gols")
    print("Total:", calcularTotalGols(), "| Média:", calcularMediaGols())
    print("Artilheiro(s):", encontrarArtilheiros())

while True:
    print("\n1- Relatório | 2- Sair")
    if input("Opção: ") == "1": mostrarRelatorio()
    else: break