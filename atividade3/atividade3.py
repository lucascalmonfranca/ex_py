nomes = ["Dipirona", "Paracetamol", "Loratadina", "Ibuprofeno", "Omeprazol"]
precos = [12.50, 9.90, 18.75, 15.00, 22.00]
estoques = [20, 15, 8, 3, 2]

def pesquisarMedicamento(nome):
    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower(): return i
    return -1

def registrarVenda():
    i = pesquisarMedicamento(input("Nome: "))
    if i != -1:
        q = int(input("Qtd: "))
        if 0 < q <= estoques[i]:
            estoques[i] -= q
            print("Vendido! Total: R$", q * precos[i])
        else: print("Qtd inválida/sem estoque!")
    else: print("Não achou!")

def reporEstoque():
    i = pesquisarMedicamento(input("Nome: "))
    if i != -1:
        q = int(input("Qtd pra adicionar: "))
        if q > 0: estoques[i] += q
    else: print("Não achou!")

def verificarEstoqueBaixo():
    for i in range(len(nomes)):
        if estoques[i] < 5: print(f"{nomes[i]}: {estoques[i]} uni (BAIXO)")

while True:
    print("\n1-Listar 2-Pesquisar 3-Vender 4-Repor 5-Baixo 6-Sair")
    op = input("Opção: ")
    if op == "1":
        for i in range(len(nomes)): print(f"{nomes[i]} - R${precos[i]} - Qtd: {estoques[i]}")
    elif op == "2":
        i = pesquisarMedicamento(input("Nome: "))
        if i != -1: print(f"{nomes[i]} - R${precos[i]} - Qtd: {estoques[i]}")
    elif op == "3": registrarVenda()
    elif op == "4": reporEstoque()
    elif op == "5": verificarEstoqueBaixo()
    else: break