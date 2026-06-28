# Sistema de Controle de Estoque e Vendas
# versao 1.0 - feito rapido pra entregar antes do prazo
# autor: equipe antiga

import datetime

SENHA_ADMIN = "1234"  # senha do admin

produtos = []


# funcao que adiciona produto
def add(n, p, q, hist=[]):
    produtos.append({"nome": n, "preco": p, "qtd": q})
    hist.append(n)
    print("Produto adicionado!")


def vender_produtos(nome, quantidade):

    for produto in produtos:

        # Guard clause: ignora produtos com nome diferente
        if produto["nome"] != nome:
            continue

        # Guard clause: para se não há estoque do produto
        if produto["qtd"] < quantidade:
            print("Estoque insuficiente")
            return 0

        produto["qtd"] -= quantidade

        total = calcular_total(produto["preco"], quantidade)

        print("Venda realizada. Total:", total)
        return total

    print("Produto nao encontrado")
    return 0


# calcula o valor total de uma compra
def calcular_total(preco, quantidade):

    porcentagem_desconto = 0.1
    valor_bruto_minimo = 100

    total = preco * quantidade

    # desconto pra compras grandes
    if total > valor_bruto_minimo:
        total -= total * porcentagem_desconto

    return total


def listar():
    print("=== PRODUTOS ===")
    for x in produtos:
        print(x["nome"] + " - R$" + str(x["preco"]) +
              " - qtd: " + str(x["qtd"]))


def relatorio_estoque_baixo():
    print("=== ESTOQUE BAIXO ===")
    for x in produtos:
        if x["qtd"] < 5:        # estoque baixo
            print(x["nome"] + " esta com estoque baixo (" + str(x["qtd"]) + ")")


# funcao antiga, nao usamos mais
# def exportar():
#     f = open("dados.txt", "w")
#     for x in produtos:
#         f.write(str(x))
#     f.close()


def relatorio_vendas():
    # TODO: implementar de verdade
    pass


# Valida o preço informado, garantindo que seja um número positivo
def ler_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco <= 0:
                print("O preço deve ser maior que zero.")
            else:
                return preco
        except ValueError:
            print("Digite apenas números para o preço.")


# Valida a quantidade informada, garantindo que seja um número inteiro positivo
def ler_quantidade(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                return quantidade
        except ValueError:
            print("Digite apenas números inteiros para a quantidade.")


# Valida textos, garantindo que a entrada não seja vazia
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("O texto não pode estar vazio.")


# valida a opção escolhida pelo o usuário
def ler_opcao_menu():
    while True:
        opcao = input("Opcao: ").strip()
        if opcao in ("0", "1", "2", "3", "4", "5"):
            return opcao
        print("Opção inválida. Digite um valor entre 0 e 5.")


def menu():

    while True:
        print("\n1-Cadastrar  2-Vender  3-Listar  4-Estoque baixo  5-Admin  0-Sair")
        opcao_menu = ler_opcao_menu()

        if opcao_menu == "1":

            nome_produto = ler_texto("Nome: ")
            preco_produto = ler_preco("Preco: ")
            quantidade_produto = ler_quantidade("Quantidade: ")

            add(nome_produto, preco_produto, quantidade_produto)

        elif opcao_menu == "2":

            nome_produto = ler_texto("Nome do produto: ")
            quantidade_produto = ler_quantidade("Quantidade: ")

            vender_produtos(nome_produto, quantidade_produto)

        elif opcao_menu == "3":
            listar()

        elif opcao_menu == "4":
            relatorio_estoque_baixo()

        elif opcao_menu == "5":

            senha = ler_texto("Senha: ")
            if senha == SENHA_ADMIN:
                print("Acesso liberado")
            else:
                print("Senha errada")

        elif opcao_menu == "0":
            break


menu()