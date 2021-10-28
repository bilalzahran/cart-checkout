from datetime import datetime
from fastapi import Depends
from dependency_injector.wiring import inject, Provide
from sqlalchemy.sql.expression import update
from src.repository.order_detail import OrderDetailRepository
from src.dependency.container import Container
from src.repository.product import ProductRepository
from src.repository.order import OrderRepository
from src.model.order import (
    OrderRequestSchema,
    OrderCheckoutRequestSchema,
    Order,
    OrderIn,
    OrderDetail,
    DetailOrderRequestSchema,
)
from src.model.product import ProductOut, ProductIn

order_in_cart_status = "IN_CART"
order_waiting_payment_status = "WAITING_PAYMENT"


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

        if product.stock - item.quantity < 0:
            return {"message": f"{product.name} is out of stock!"}

        order_detail_arr.append(
            OrderDetail(
                **item.dict(exclude=False),
                sub_total=product.price * item.quantity,
                order_id=order.id if order else None,
            )
        )

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


@inject
async def checkout(
    payload: OrderCheckoutRequestSchema,
    order_repo: OrderRepository = Depends(Provide[Container.order_repo]),
    order_detail_repo: OrderDetailRepository = Depends(
        Provide[Container.order_detail_repo]
    ),
    product_repo: ProductRepository = Depends(Provide[Container.product_repo]),
):
    # Get order by user id and with status "IN_CART"
    order: Order = await order_repo.get_by_status_and_user_id(
        status=order_in_cart_status, user_id=payload.user_id
    )
    if not order:
        return {"message": "No order in cart for this specified user"}

    # Fetch the detail order
    detail_order = await order_detail_repo.get_by_order_id(order.id)
    if not detail_order:
        return {"message": "The cart is empty"}

    # Get the quantity of checked out product, total amount of the subtotal in detail order
    # and get the list of product id
    detail_order_quantity = dict()
    total_amount = 0
    product_update_arr_id = []

    for item in detail_order:
        detail_order_quantity[item.product_id] = item.quantity
        total_amount += item.sub_total
        product_update_arr_id.append(item.product_id)

    # Get the data of product to be process
    product_arr = await product_repo.get_product_by_id(product_update_arr_id)
    updated_product = []
    for product in product_arr:
        product: ProductOut = product
        if product.stock - detail_order_quantity[product.id] < 0:
            return {"message": f"Can't checkout, {product.name} is out of stock!"}
        product.stock = product.stock - detail_order_quantity[product.id]
        product.version = (
            product.version + 1
        )  # Increase the version field to block any other request
        product.updated_at = datetime.now()
        updated_product.append(product)

    status = await product_repo.bulk_update(updated_product)
    if not status:
        return {"message": "Something went wrong!"}

    order.total_amount = total_amount
    order.status = order_waiting_payment_status
    order_update_status = await order_repo.update(payload=order)
    if not order_update_status:
        return {"message": "Something went wrong!"}

    return True
