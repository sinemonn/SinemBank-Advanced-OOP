import unittest
from banking_modules import SavingsAccount, CheckingAccount, Customer, InsufficientFundsError

class TestSinemBank(unittest.TestCase):
    def setUp(self):
        self.cust = Customer("Sinem", 2422)
        self.savings = SavingsAccount(1, self.cust, 1000.0)
        self.checking = CheckingAccount(2, self.cust, 500.0, 200.0)

    def test_savings_deposit(self):
        self.savings.deposit(500)
        self.assertEqual(self.savings.balance, 1500.0)

    def test_savings_withdraw_success(self):
        self.savings.withdraw(400)
        self.assertEqual(self.savings.balance, 600.0)

    def test_savings_withdraw_fail(self):
        with self.assertRaises(InsufficientFundsError):
            self.savings.withdraw(2000)

    def test_checking_overdraft_success(self):
        # 500 bakiye + 200 limit = 700 çekebilir
        self.assertTrue(self.checking.withdraw(650))
        self.assertEqual(self.checking.balance, -150.0)

    def test_checking_overdraft_limit_fail(self):
        with self.assertRaises(InsufficientFundsError):
            self.checking.withdraw(800)

if __name__ == '__main__':
    unittest.main()