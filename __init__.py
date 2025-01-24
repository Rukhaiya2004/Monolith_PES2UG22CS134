import json
from cart import dao
from products import Product, get_product


class Cart:
    def _init_(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if not cart_details:  # Avoid redundant checks
        return []
    
    items = []
    for cart_detail in cart_details:
        contents = json.loads(cart_detail['contents'])  # Use json.loads instead of eval
        items.extend(contents)

    # Use a list comprehension for concise and efficient product retrieval
    return [get_product(product_id) for product_id in items]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)