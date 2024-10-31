from typing import Annotated
from fastapi import APIRouter, Body, Response

from carts.domain.app import app

from carts.domain.command.create_cart import CreateCartCommand
from carts.domain.command.delete_cart import DeleteCartCommand
from carts.domain.command.update_cart import UpdateCartCommand

from carts.domain.query.get_cart_by_uuid import GetCartByUUID
from carts.domain.query.get_all_carts import GetAllCarts

router = APIRouter()


@router.post("/carts", tags=["carts"], status_code=201)
def create_cart(total_amount: Annotated[float, Body(embed=True)]):
    command = CreateCartCommand(
        total_amount=total_amount,
    )
    app.execute_command(command)
    return {"message": "Cart created successfully!", "cart_uuid": command.uuid}


@router.get("/carts/{cart_uuid}", tags=["carts"])
def get_cart(cart_uuid: str, response: Response):
    query = GetCartByUUID(uuid=cart_uuid)
    result = app.execute_query(query)
    if not result:
        response.status_code = 404
        return {"message": "Cart not found!"}
    return result.to_dict()


@router.get("/carts", tags=["carts"])
def get_carts():
    query = GetAllCarts()
    result = app.execute_query(query)
    return {"carts": [cart.to_dict() for cart in result]}


@router.put("/carts/{cart_uuid}", tags=["carts"])
def update_cart(
    cart_uuid: str,
    response: Response,
    total_amount: Annotated[float, Body(embed=True)] = None,
    closed: Annotated[bool, Body(embed=True)] = None,
):
    query = GetCartByUUID(uuid=cart_uuid)
    result = app.execute_query(query)
    if not result:
        response.status_code = 404
        return {"message": "Cart not found!"}

    command = UpdateCartCommand(
        uuid=cart_uuid,
        total_amount=total_amount,
        closed=closed,
    )
    app.execute_command(command)
    return {"message": "Cart updated successfully!"}


@router.delete("/carts/{cart_uuid}", tags=["carts"])
def delete_cart(cart_uuid: str, response: Response):
    query = GetCartByUUID(uuid=cart_uuid)
    result = app.execute_query(query)
    if not result:
        response.status_code = 404
        return {"message": "Cart not found!"}
    command = DeleteCartCommand(uuid=cart_uuid)
    app.execute_command(command)
    return {"message": "Cart deleted successfully!"}
