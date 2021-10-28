from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from src.repository.order_detail import OrderDetailRepository
from src.dependency.container import Container
from src.repository.product import ProductRepository
from src.repository.order import OrderRepository
from src.model.order import OrderRequestSchema, Order, OrderIn, OrderDetail
from src.model.product import ProductOut

order_in_cart_status = "IN_CART"


@inject
async def add_to_cart(
    payload: OrderRequestSchema,
    order_repo: OrderRepository = Depends(Provide[Container.order_repo]),
    order_detail_repo: OrderDetailRepository = Depends(
        Provide[Container.order_detail_repo]
    ),
    product_repo: ProductRepository = Depends(Provide[Container.product_repo]),
):
    # Check if order with status "IN_CART" exist
    # The status indicate order that has not been checked out by user / still in cart
    order: Order = await order_repo.get_by_status_and_user_id(
        status=order_in_cart_status, user_id=payload.user_id
    )

    # Check the availability of the product
    # If the stock of the product are 0, return message
    # If product is available, calculate the total amount of the product price
    total_amount = 0
    order_detail_arr = []
    for item in payload.order_detail:
        product: ProductOut = await product_repo.get_one(item.product_id)
        if not product:
            return {"message": "product not exist!"}

        if product.stock - item.quantity <= 0:
            return {"message": f"{product.name} is out of stock!"}

        order_detail_arr.append(
            OrderDetail(
                **item.dict(exclude=False),
                sub_total=product.price * item.quantity,
                order_id=order.id if order else None,
            )
        )

        total_amount += product.price * item.quantity

    # If the order with status IN_CART not exist, create new order data
    # If the order with status exist, add the product / item to detail order
    if not order:
        order_db_payload = OrderIn(**payload.dict(exclude=False))
        order_id = await order_repo.insert(order_db_payload)

        # Update the order detail by adding the order id
        for item in order_detail_arr:
            item.order_id = order_id
            status = await order_detail_repo.insert(item)
            if not status:
                return {"message": "Can't add this product"}
    else:
        for item in order_detail_arr:
            item.order_id = order.id
            # Check if item is already in cart
            # If exist, update the item in cart
            item_in_cart = await order_detail_repo.get_by_order_id_and_product_id(
                order.id, item.product_id
            )

            if item_in_cart:
                status = await order_detail_repo.update(item, order.id)
            else:
                status = await order_detail_repo.insert(item)

            if not status:
                return {"message": "Can't add this product"}

    return True
