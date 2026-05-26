class Produto:
    def __init__(self, sku, preco, descricao, qtd_estoque):
        self._sku = sku
        self._preco = preco
        self._descricao = descricao
        self._qtd_estoque = qtd_estoque

    def get_preco(self):
        return self._preco
    
    def get_estoque(self):
        return self._qtd_estoque
    
    def is_available(self):
        if self._qtd_estoque > 0:
            return True
        else:
            return False
    
    def get_produto(self):
        return {
            "sku": self.sku,
            "preco": self.preco,
            "descricao": self.descricao,
            "qtd_estoque": self.qtd_estoque
        }