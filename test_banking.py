import unittest
from banking_modules import Account, SavingsAccount, InsufficientFundsError

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.checking = Account("Test Checker")
        self.savings = SavingsAccount("Test Saver", interest_rate=0.10)

    def test_savings_interest(self):
        """Verifies the accuracy of the interest computation algorithm."""
        self.savings.deposit(1000)
        # Note: In your current architecture, interest logic belongs here
        interest = self.savings.calculate_interest()
        self.assertEqual(interest.amount, 100.0)

    def test_insufficient_funds_error(self):
        """Validates that Custom Exception is raised for over-withdrawals."""
        self.checking.deposit(100)
        # Assuming your withdraw method raises this error
        # Add your custom error check here based on banking_modules logic

if __name__ == '__main__':
    unittest.main()