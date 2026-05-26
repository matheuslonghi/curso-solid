from src.domain.entities.produto import Produto
from typing import List
from enum import StrEnum, auto
import uuid


class CarrinhoStatus(StrEnum):
    ATIVO = auto()
    FINALIZADO = auto()
    EXPIRADO = auto()


class Carrinho:
    def __init__(self, produtos, carrinho_id: str):
        self._produtos = produtos
        self._carrinho_id = carrinho_id
        self._status = CarrinhoStatus.ATIVO

    def get_id(self):
        if not self._carrinho_id:
            self._carrinho_id = uuid.uuid4()
        return self._carrinho_id
    
    def add_novo_produto(self, produto: Produto):
        self._produtos.append(produto)

    def remover_produto(self, produto: Produto):
        self._produtos.remove(produto)

    def switch(self, new_status: CarrinhoStatus):
        self._status = new_status
        return self._status
    
    def get_status(self):
        return self._status
    
    def calc_subtotal(self):
        precos = [
            produto.get_preco() for produto in self._produtos
            if produto.is_available()
        ]
        return sum(precos)
    
    def get_subtotal(self):
        return self.calc_subtotal()