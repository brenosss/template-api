from carts.domain.repositories import cart_repository


class DeleteCartCommand:
    def __init__(self, uuid: str):
        self.uuid = uuid


def DeleteCartCommandHandler(command: DeleteCartCommand) -> str:
    cart_repository.delete(command.uuid)
    return command.uuid
