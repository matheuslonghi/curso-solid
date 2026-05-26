from src.domain.service.cupom.cupom_strategy import BlackFridayCupom, NatalCupom, CupomStrategy
from enum import StrEnum, auto


class TypeCupom(StrEnum):
    BLACK_FRIDAY = auto()
    NATAL = auto()


class StrategyCupomFactory:
    _strategy_map = {
        TypeCupom.BLACK_FRIDAY: BlackFridayCupom(),
        TypeCupom.NATAL: NatalCupom()
    }

    @classmethod
    def create(cls, type_cupom: TypeCupom) -> CupomStrategy:
        try:
            return cls._strategy_map[type_cupom]
        except KeyError:
            raise ValueError(f'Type {type_cupom} not supported')