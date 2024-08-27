from ast import Try
from dataclasses import dataclass


@dataclass
class Customer:
    id: str
    debt: float

class CustomerNotFoundException:
    pass


class CustomerDebtService:
    def __init__(self) -> None:
        self.__fakeCustomers = [Customer(1, 2), Customer(2, 3), Customer(3, 4)]

    def get_debt_of_customer(self, id: str) -> float:
        try:
            customer = self.__get_customer(id)
            return customer.debt
        except StopIteration:
            return 0 # skilar núna 0 hér

    def set_debt_of_customer(self, id: str, debt: float) -> bool:
        try:
            customer = self.__get_customer(id)
            customer.debt = debt
        except StopIteration:
            raise CustomerNotFoundException()

    def __get_customer(self, id: str) -> Customer:
        return next((customer for customer in self.__fakeCustomers if customer.id == id))


def print_debt(customerId: str, debt: float):
    print(f"Debt of customer with id: {customerId} is {debt}")


if __name__ == '__main__':
    service = CustomerDebtService()

    customer_id = 1
    debt = service.get_debt_of_customer(customer_id)
    print_debt(customer_id, debt)

    status = service.set_debt_of_customer(customer_id, 10)
    debt = service.get_debt_of_customer(customer_id)
    print(status)
    print_debt(customer_id, debt)


