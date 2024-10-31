from carts.domain.command.create_cart import CreateCartCommand, CreateCartCommandHandler
from carts.domain.command.update_cart import UpdateCartCommand, UpdateCartCommandHandler
from carts.domain.command.delete_cart import DeleteCartCommand, DeleteCartCommandHandler

from carts.domain.query.get_all_carts import GetAllCarts, GetAllCartsHandler
from carts.domain.query.get_cart_by_uuid import GetCartByUUID, GetCartByUUIDHandler


class App:
    command_handlers = {
        CreateCartCommand: CreateCartCommandHandler,
        UpdateCartCommand: UpdateCartCommandHandler,
        DeleteCartCommand: DeleteCartCommandHandler,
    }

    query_handlers = {
        GetAllCarts: GetAllCartsHandler,
        GetCartByUUID: GetCartByUUIDHandler,
    }

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)

    def execute_query(self, query):
        handler = self.query_handlers[type(query)]
        return handler(query)


app = App()
