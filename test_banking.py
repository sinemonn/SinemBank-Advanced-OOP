import unittest
from banking_modules import (
    SavingsAccount,
    CheckingAccount,
    Customer,
    Money,
    InsufficientFundsError
)

class TestSinemBank(unittest.TestCase):

    def setUp(self):
        self.cust = Customer("Sinem", 2422)
        self.savings = SavingsAccount(1, self.cust, Money(1000))
        self.checking = CheckingAccount(2, self.cust, Money(500), Money(200))

    def test_savings_deposit(self):
        self.savings.deposit(Money(500))
        self.assertEqual(self.savings.balance, 1500)

    def test_savings_withdraw_success(self):
        self.savings.withdraw(Money(400))
