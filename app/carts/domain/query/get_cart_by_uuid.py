from carts.domain.repositories import cart_repository


class GetCartByUUID:
    def __init__(self, uuid: str):
        self.uuid = uuid


def GetCartByUUIDHandler(GetCartByUUID):
    cart = cart_repository.get(GetCartByUUID.uuid)
    return cart
