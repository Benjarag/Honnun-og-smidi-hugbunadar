from dataclasses import dataclass, asdict
import json
from typing import List, Dict

@dataclass
class Buyer:
    username: str
    allowed_products: List[str]

    @staticmethod
    def from_dict(data: Dict) -> 'Buyer':
        return Buyer(
            username=data['username'],
            allowed_products=data['allowed_products']
        )

@dataclass
class Merchant:
    username: str
    name: str
    product: str

    @staticmethod
    def from_dict(data: Dict) -> 'Merchant':
        return Merchant(
            username=data['username'],
            name=data['name'],
            product=data['product']
        )

@dataclass
class Order:
    merchant_username: str
    buyer_username: str
    price: float
    product: str
    description: str

    @staticmethod
    def from_dict(data: Dict) -> 'Order':
        return Order(
            merchant_username=data['merchant_username'],
            buyer_username=data['buyer_username'],
            price=data['price'],
            product=data['product'],
            description=data['description']
        )

class ApplicationException(Exception):
    """
    Base exception class for the application
    """
    pass

class EntityNotFound(ApplicationException):
    """
    Exception raised when an entity is not found
    """
    def __init__(self, entity_type: str, entity_id: str) -> None:
        super().__init__(f"{entity_type} with id {entity_id} not found")

def read_json(file_path: str) -> List[Dict]:
    """
    Reads JSON data from a file
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ApplicationException(f"Error reading file {file_path}: {e}")

def write_json(file_path: str, data: List[Dict]) -> None:
    """
    Writes JSON data to a file
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4, separators=(',', ': '))
    except IOError as e:
        raise ApplicationException(f"Error writing file {file_path}: {e}")

class OrderService:
    """
    Service class for managing orders
    """
    def __init__(self, merchants_file: str, buyers_file: str, orders_file: str):
        self.merchants_file = merchants_file
        self.buyers_file = buyers_file
        self.orders_file = orders_file

    def _load_entities(self, file_path: str, entity_class):
        """
        Load entities from a JSON file
        """
        data = read_json(file_path)
        return [entity_class.from_dict(item) for item in data]

    def _save_entities(self, file_path: str, entities):
        """
        Save entities to a JSON file
        """
        data = [asdict(entity) for entity in entities]
        write_json(file_path, data)

    def create_order(self, merchant_username: str, buyer_username: str, product: str, order_price: float, order_description: str) -> None:
        """
        Create an order if the merchant and buyer are valid
        """
        merchants = self._load_entities(self.merchants_file, Merchant)
        buyers = self._load_entities(self.buyers_file, Buyer)

        merchant = self._find_entity(merchants, merchant_username)
        buyer = self._find_entity(buyers, buyer_username)

        if product == merchant.product and product in buyer.allowed_products:
            order = Order(
                merchant_username=merchant.username,
                buyer_username=buyer.username,
                price=order_price,
                product=product,
                description=order_description
            )
            orders = self._load_entities(self.orders_file, Order)
            orders.append(order)
            self._save_entities(self.orders_file, orders)
        else:
            raise ApplicationException(f"Product {product} is not allowed for buyer {buyer_username} or merchant {merchant_username}")

    def _find_entity(self, entities: List, username: str):
        """
        Find an entity by username
        """
        for entity in entities:
            if entity.username == username:
                return entity
        raise EntityNotFound('Entity', username)

if __name__ == '__main__':
    # initializes the OrderService with the json file paths
    service = OrderService(
        merchants_file="VIKA2/code_skeleton-1/what_is_wrong/merchants.json",
        buyers_file="VIKA2/code_skeleton-1/what_is_wrong/buyers.json",
        orders_file="VIKA2/code_skeleton-1/what_is_wrong/orders.json"
    )
    service.create_order("eggo", "Eleven", "Eggo", 12, "some description")
