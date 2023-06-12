import math
from custom_exceptions import NullStrArgument


class Category:

    def __init__(self, my_category: str):
        try:
            if my_category == "":
                raise NullStrArgument("Category.__init__",
                                      "trying to create a Category object without name")
            pass
        except NullStrArgument as e:
            print(f"In {e.function} you are {e.message}")
            pass
        else:
            self.name = my_category
            self.balance = 0
            self.ledger = list({})
        pass

    def deposit(self, amount: int, description: str = None):
        """
A deposit method that accepts an amount and description. If no description is given,
it should default to an empty string. The method should append an object to the ledger list
in the form of {"amount": amount, "description": description}
        :param amount:
        :param description:
        """
        if description is None:
            self.ledger.append({"amount": amount, "description": ""})
            pass
        else:
            self.balance += amount
            self.ledger.append({"amount": amount, "description": description})
            pass
        pass

    def withdraw(self, amount: int, description: str = None) -> bool:
        """
A withdraw method that is similar to the deposit method,
but the amount passed in should be stored in the ledger
as a negative number. If there are not enough funds,
nothing should be added to the ledger.
        :param amount: amount to withdraw
        :param description: a short description of the operation
        :return: bool: return True if the withdrawal took place, and False otherwise.
        """
        if description is None:
            self.ledger.append({"amount": amount, "description": ""})
            return False
            pass
        elif self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        pass

    def get_balance(self):
        return self.balance

    def transfer(self, amount: int, budget) -> bool:
        """
A transfer method that accepts an amount and another budget category as arguments.
The method should add a withdrawal with the amount and the description "Transfer to
[Destination Budget Category]". The method should then add a deposit to the other
budget category with the amount and the description "Transfer from [Source Budget Category]".
If there are not enough funds, nothing should be added to either ledgers.
        :param amount: amount to transfer
        :param budget: another budget to transfer funds
        :return: return True if the transfer took place, and False otherwise.
        """
        self.withdraw(amount, f"Transfer to {budget.name}]")
        if self.check_funds(amount):
            budget.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        pass

    def check_funds(self, amount: int) -> bool:
        """
A check_funds method that accepts an amount as an argument.
This method should be used by both the withdraw method and transfer method.
        :param amount: amount to check
        :return: It returns False if the amount is greater than the balance
                 of the budget category and returns True otherwise.
        """
        if amount > self.balance:
            return False
        else:
            return True
        pass

    def print_category(self):
        """
Properly print this category
        """
        print('\n{:*^30}'.format(self.name))
        for ledger_item in self.ledger:
            print(f"{ledger_item['description']:<22} {ledger_item['amount']:>-7}")
        pass
        print(f'Total = {self.get_balance()}')

    pass


def create_spend_chart(categories_list: list[Category]) -> str:
    """
create_spend_chart takes a list of categories as an argument.
It should return a string that is a bar chart.
    :param categories_list:
    :return: a string bar chart.
    """
    to_print = list()
    chart = "\nPercentage spent by category\n"
    for this_category in categories_list:
        deposits = spent = 0
        for this_ledger in this_category.ledger:
            if this_ledger["amount"] > 0:
                deposits += this_ledger["amount"]
                pass
            else:
                spent += abs(this_ledger["amount"])
                pass
            pass
        n = math.ceil(10 * spent / deposits)
        to_print.append([n, f"{' ' * (11 - n)}{'o' * n}-{this_category.name}{' ' * (13 - len(this_category.name))}"])
        pass
    to_print = sorted(to_print, key=None, reverse=True)
    it = 1
    while it <= len(to_print):
        to_print.insert(it, list([0, f"{' ' * 11}-{' ' * 13}"]))
        it += 1
        to_print.insert(it, list([0, f"{' ' * 11}-{' ' * 13}"]))
        it += 2
    to_print.insert(0, list([0, f"{' ' * 11}-{' ' * 13}"]))
    to_print.insert(0, [0, f"{'|' * 11}{' ' * 14}"])
    to_print.insert(0, [0, f"{'0' * 11}{' ' * 14}"])
    to_print.insert(0, [0, f"0987654321{' ' * 14}"])
    to_print.insert(0, [0, f"1{' ' * 24}"])
    for ite in range(0, 24):
        for every_list in to_print:
            chart += every_list[1][ite]
            pass
        chart += "\n"
        pass
    return chart
