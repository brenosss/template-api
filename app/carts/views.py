from fastapi import APIRouter, Body

from carts.domain.app import app
from carts.domain.command.create_cart import CreateCartCommand

router = APIRouter()


@router.post("/carts", tags=["carts"])
def create_cart(total_amount: str | float = Body(embed=True)):
    command = CreateCartCommand(
        total_amount=total_amount,
    )
    app.execute_command(command)

    return {"message": "Cart created successfully!", "cart_uuid": command.uuid}
