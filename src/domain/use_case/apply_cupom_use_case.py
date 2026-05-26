from src.domain.entities.carrinho import Carrinho
from src.domain.service.cupom.apply_cupom import ApplyCupomStrategy
from src.domain.factories.cupom_strategy_factory import TypeCupom, StrategyCupomFactory


class ApplyCupomUseCase:
    def execute(self, carrinho: Carrinho, type_cupom: TypeCupom) -> dict:
        subtotal = carrinho.get_subtotal()
        strategy = StrategyCupomFactory.create(type_cupom)
        discount = ApplyCupomStrategy(strategy).apply_desconto(subtotal)
        new_subtotal = subtotal - discount
        return {
            "discount_value": discount,
            "new_subtotal": new_subtotal,
            "cart_id": carrinho.get_carrinho_id()
        }