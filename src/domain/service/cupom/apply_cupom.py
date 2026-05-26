from src.domain.service.cupom.cupom_strategy import CupomStrategy


class ApplyCupomStrategy():
    def __init__(self, strategy: CupomStrategy):
        self._strategy = strategy

    def update_strategy(self, new_strategy: CupomStrategy):
        self._strategy = new_strategy

    def apply_desconto(self, value: float):
        return self._strategy.apply_desconto(value)