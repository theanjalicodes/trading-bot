from bot.clint import client
import logging

def place_market_order(symbol, side, quantity):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"Market Order Response: {order}")
    return order


def place_limit_order(symbol, side, quantity, price):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logging.info(f"Limit Order Response: {order}")
    return order