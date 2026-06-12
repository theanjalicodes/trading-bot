from bot.validation import *
from bot.orders import *
from bot.logging_config import *
import logging

try:

    symbol = input("Enter Symbol: ").upper()

    side = input("Enter Side (BUY/SELL): ").upper()

    order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()

    quantity = float(input("Enter Quantity: "))

    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)

    print("\n===== ORDER SUMMARY =====")
    print("Symbol:", symbol)
    print("Side:", side)
    print("Type:", order_type)
    print("Quantity:", quantity)

    if order_type == "MARKET":

        order = place_market_order(
            symbol,
            side,
            quantity
        )

    else:

        price = float(input("Enter Price: "))

        validate_price(order_type, price)

        order = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )

    print("\n===== ORDER RESPONSE =====")

    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))

    print("\nSUCCESS")

except Exception as e:

    logging.error(str(e))

    print("\nFAILED")
    print(e)