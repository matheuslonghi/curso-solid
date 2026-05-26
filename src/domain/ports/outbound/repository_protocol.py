from src.domain.entities.carrinho import Carrinho
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List


T = TypeVar('T')

class GetRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def read(self, item_id: str) -> T:
        pass


class GetAllRepositoryProtocols(ABC, Generic[T]):
    @abstractmethod
    def read_all(self) -> List[T]:
        pass


class InsertRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def save(self, data: T):
        pass


class DeleteRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def delete(self, item_id: str):
        pass


class UpdateRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def update(self, data: T, item_id: str):
        pass

class CartRepositoryProtocol(GetRepositoryProtocol[Carrinho], DeleteRepositoryProtocol[Carrinho], InsertRepositoryProtocol[Carrinho], UpdateRepositoryProtocol[Carrinho], ABC):
    pass