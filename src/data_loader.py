import pandas as pd


def load_orders():
    orders = pd.read_csv("data/orders.csv")

    return orders


def find_order(order_id):
    orders = load_orders()

    order = orders[orders["order_id"] == order_id]

    if order.empty:
        return None

    return order.iloc[0]

