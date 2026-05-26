from src.domain.ports.outbound.repository_protocol import CartRepositoryProtocol
from src.domain.entities.carrinho import Carrinho
from typing import List


LIST_CART: List[Carrinho] = []

class CartRepository(CartRepositoryProtocol):
    def __init__(self):
        self._carts = LIST_CART

    def delete(self, item_id: str):
        result = [
            unique for unique in self._carts 
            if unique.get_id() == item_id
        ]
        self._carts.remove(result[0])

    def read(self, item_id: str):
        result = [
            unique for unique in self._carts 
            if unique.get_id() == item_id
        ]
        return result

    def save(self, data: Carrinho):
        self._carts.append(data)

    def update(self, item_id: str, data: Carrinho):
        result = [
            unique for unique in self._carts 
            if unique.get_id() == item_id
        ]
        self._carts.remove(result[0])
        self.save(data)