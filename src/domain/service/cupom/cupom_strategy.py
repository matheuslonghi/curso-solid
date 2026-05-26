from abc import ABC, abstractmethod


class CupomStrategy(ABC):
    @abstractmethod
    def apply_desconto(self, value: float):
        pass


class BlackFridayCupom(CupomStrategy):
    def apply_desconto(self, value: float):
        if value < 300:
            return 0
        return value * 0.20
    
    
class NatalCupom(CupomStrategy):
    def apply_desconto(self, value: float):
        if value < 800:
            return 0
        return value * 0.30