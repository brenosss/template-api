from carts.domain.command.create_cart import CreateCartCommand, CreateCartCommandHandler


class App:
    command_handlers = {
        CreateCartCommand: CreateCartCommandHandler,
    }

    def execute_command(self, command):
        handler = self.command_handlers[type(command)]
        return handler(command)


app = App()
