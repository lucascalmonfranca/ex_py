matriz = [["L"]*6 for _ in range(5)]
cols = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}

def calcularPreco(f):
    return ("Executiva", 850) if f == 0 else ("Espaço extra", 600) if f in [1,2] else ("Econômica", 400)

def comprarAssento():
    a = input("Assento (ex 2C): ").upper()
    f, c = int(a[0])-1, cols[a[1]]
    if matriz[f][c] == "O": print("Ocupado!")
    else:
        cat, preco = calcularPreco(f)
        if input(f"{cat} - R${preco}. Confirmar? (S/N): ").upper() == "S":
            matriz[f][c] = "O"

def mostrarResumo():
    oc = sum(linha.count("O") for linha in matriz)
    total = sum(calcularPreco(f)[1] for f in range(5) for c in range(6) if matriz[f][c] == "O")
    print(f"Livres: {30-oc} | Ocupados: {oc} | Faturamento: R${total}")

while True:
    print("\n1-Mapa 2-Comprar 3-Resumo 4-Sair")
    op = input("Opção: ")
    if op == "1":
        for i, l in enumerate(matriz): print(i+1, " ".join(l))
    elif op == "2": comprarAssento()
    elif op == "3": mostrarResumo()
    else: break