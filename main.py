database = []

class Produto:
    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo


class Carrinho:
    def __init__(self):
        self.itens = []
        self.total = 0

    def adicionar(self, produto):
        self.itens.append(produto)
        self.total += produto.preco
        if produto.tipo == 'perecivel':
            print("Adicionar embalagem especial")
        elif produto.tipo == 'digital':
            print("Gerar link de download")
        else:
            print("Produto adicionado ao carrinho.")

    def remover(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)
            self.total -= produto.preco
            print(f"{produto.nome} removido do carrinho.")
        else:
            print(f"{produto.nome} não está no carrinho.")

    def calcular_desconto(self, cupom):
        if cupom == 'BLACKFRIDAY':
            self.total *= 0.5
        elif cupom == 'NATAL':
            self.total *= 0.9
        else:
            print("Cupom inválido")

    def finalizar_compra(self):
        print(f"Total a pagar: R${self.total}")
        self.salvar_database()
        print("Email enviado com confirmação!")

    def salvar_database(self):
        database.append(self.itens)
        print("Itens do carrinho salvos no banco de dados.")

    def send_sms(self, mensagem):
        print(mensagem)

    def send_email(self, mensagem):
        print(mensagem)

    def send_whatsapp(self, mensagem):
        print(mensagem)

    def notificar_cliente(self, itens, total, canal):
        message = f"Seus {itens}, estão a caminho, já finalizamos sua compra no total de {total}"
        if canal == "sms":
            self.send_sms(message)
        elif canal == "email":
            self.send_email(message)
        elif canal == "whatsapp":
            self.send_whatsapp(message)
        else:
            raise  TypeError("modelo ainda não implementado")

