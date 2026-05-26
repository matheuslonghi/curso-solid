from src.domain.ports.outbound.repository_protocol import CartRepositoryProtocol
from src.domain.ports.outbound.notifier_protocol import NotifyByCellPhone, NotifyByEmail
from src.domain.entities.carrinho import CarrinhoStatus
from src.domain.value_object.email import Email
from src.domain.value_object.phone import Phone
from typing import List


class SwitchCartUseCase:
    def __init__(self, repository: CartRepositoryProtocol, notiyfy_emails: List[NotifyByEmail], notify_phones: List[NotifyByCellPhone]):
        self._repository = repository
        self._notiyfy_emails = notiyfy_emails
        self._notify_phones = notify_phones

    def execute(self, cart_id: str, cellphone: Phone, email: Email, new_status: CarrinhoStatus):
        cart_entity = self._repository.read(cart_id)
        cart_entity.switch(new_status)
        message = f"cart change status: {new_status}"
        for notify_email in self._notiyfy_emails:
            notify_email.send_message(message, email)

        for notify_cellphone in self._notify_phones:
            notify_cellphone.send_message(message, cellphone)
        return cart_entity