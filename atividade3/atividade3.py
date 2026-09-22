nomes = ["Dipirona", "Paracetamol", "Loratadina", "Ibuprofeno", "Omeprazol"]
precos = [12.50, 9.90, 18.75, 15.00, 22.00]
estoques = [20, 15, 8, 3, 2]

def listarMedicamentos():
    for i in range(len(nomes)):
        print(i, "-", nomes[i], "| R$", precos[i], "| Estoque:", estoques[i])

def pesquisarMedicamento():
    nome = input("Nome: ")
    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            print(nomes[i], "- R$", precos[i], "| Estoque:", estoques[i])
            return
    print("Não encontrado!")

def registrarVenda():
    nome = input("Nome do medicamento: ")
    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            qtd = int(input("Quantidade: "))
            if qtd <= estoques[i] and qtd > 0:
                estoques[i] -= qtd
                print("Venda OK! Total: R$", qtd * precos[i])
            else:
                print("Estoque insuficiente ou quantidade inválida!")
            return
    print("Não encontrado!")

def reporEstoque():
    nome = input("Nome do medicamento: ")
    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            qtd = int(input("Quantidade a adicionar: "))
            if qtd > 0:
                estoques[i] += qtd
                print("Estoque atualizado!")
            return
    print("Não encontrado!")

def verificarEstoqueBaixo():
    print("--- ESTOQUE BAIXO (< 5) ---")
    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(nomes[i], "-", estoques[i], "unidades")

opcao = ""
while opcao != "6":
    print("\n1-Listar 2-Pesquisar 3-Vender 4-Repor 5-Estoque Baixo 6-Sair")
    opcao = input("Opção: ")
    if opcao == "1": listarMedicamentos()
    elif opcao == "2": pesquisarMedicamento()
    elif opcao == "3": registrarVenda()
    elif opcao == "4": reporEstoque()
    elif opcao == "5": verificarEstoqueBaixo()
matriz = [
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L"]
]

colunas = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

def mostrarAssentos():
    print("\n   A B C D E F")
    for i in range(5):
        print(i + 1, " ".join(matriz[i]))

def calcularPreco(f):
    if f == 0: return "Executiva", 850.0
    if f == 1 or f == 2: return "Espaço extra", 600.0
    return "Econômica", 400.0

def comprarAssento():
    a = input("Assento (ex: 2C): ").upper()
    f = int(a[0]) - 1
    c = colunas[a[1]]
    
    if matriz[f][c] == "O":
        print("Assento ocupado!")
    else:
        cat, preco = calcularPreco(f)
        print("Categoria:", cat, "| Preço: R$", preco)
        conf = input("Confirmar? (S/N): ").upper()
        if conf == "S":
            matriz[f][c] = "O"
            print("Vendido!")

def mostrarResumo():
    livres = 0
    ocupados = 0
    total_r = 0
    for f in range(5):
        for c in range(6):
            if matriz[f][c] == "L":
                livres += 1
            else:
                ocupados += 1
                cat, p = calcularPreco(f)
                total_r += p
    print("Livres:", livres)
    print("Ocupados:", ocupados)
    print("Faturamento: R$", total_r)

opcao = ""
while opcao != "4":
    print("\n1-Mapa 2-Comprar 3-Resumo 4-Sair")
    opcao = input("Opção: ")
    if opcao == "1": mostrarAssentos()
    elif opcao == "2": comprarAssento()
    elif opcao == "3": mostrarResumo()