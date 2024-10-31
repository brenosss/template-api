from carts.domain.repositories import cart_repository


class UpdateCartCommand:
    def __init__(self, uuid: str, total_amount: float = None, closed: bool = None):
        self.uuid = uuid
        self.total_amount = total_amount
        self.closed = closed


def UpdateCartCommandHandler(command: UpdateCartCommand) -> str:
    cart = cart_repository.get(command.uuid)

    cart.total_amount = command.total_amount or cart.total_amount
    cart.closed = command.closed or cart.closed

    cart_repository.update(cart)
    return cart.uuid
