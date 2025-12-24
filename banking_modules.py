from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime
import json
import os

# ==========================================
# 1. CUSTOM EXCEPTIONS
# ==========================================
class InsufficientFundsError(Exception):
    """Exception raised for errors in the withdrawal process due to low balance."""
    pass

# ==========================================
# 2. DATA MODELS (IMMUTABILITY)
# ==========================================
@dataclass(frozen=True)
class Money:
    """Value object for immutable currency operations."""
    amount: float
    currency: str = "TRY"
    
    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Currency mismatch during addition.")

@dataclass
class Transaction:
    """Model for tracking account transaction history."""
    description: str
    amount: float
    date: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M'))

# ==========================================
# 3. ACCOUNT HIERARCHY
# ==========================================
class Account:
    """Base class for banking accounts applying encapsulation principles."""
    def __init__(self, owner: str, currency: str = "TRY"):
        self.owner = owner
        self.currency = currency
        self._balance = 0.0 
        self._transaction_history: List[Transaction] = []

    def deposit(self, amount: float, description: str = "Deposit"):
        if amount <= 0: return
        self._balance += amount
        self._transaction_history.append(Transaction(description, amount))

    def withdraw(self, amount: float, description: str = "Withdrawal"):
        if amount > 10000: 
            print(f"REPORT: High-value transaction alert for account: {self.owner}")

        if amount > self._balance:
            raise InsufficientFundsError(f"Current balance {self._balance} is insufficient.")
        
        self._balance -= amount
        self._transaction_history.append(Transaction(description, -amount))

    def __str__(self):
        return f"Account Owner: {self.owner} | Balance: {self._balance:.2f} {self.currency}"

class SavingsAccount(Account):
    """Subclass implementing specialized interest computation algorithms."""
    def __init__(self, owner: str, interest_rate: float = 0.15):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Calculates interest and returns it as a Money object."""
        interest_value = self._balance * self.interest_rate
        return Money(interest_value)

    def apply_interest(self):
        """Applies interest to the balance."""
        interest_obj = self.calculate_interest()
        self.deposit(interest_obj.amount, "Accrued Interest Income")

class CheckingAccount(Account):
    """Subclass with transaction limits."""
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        if amount > 5000: 
            print("SECURITY: Transaction rejected. Amount exceeds standard limit.")
            return
        super().withdraw(amount, description)

# ==========================================
# 4. CUSTOMER CLASS (MISSING PIECE!)
# ==========================================
class Customer:
    """Class representing a bank customer and their linked accounts."""
    def __init__(self, name: str, tax_id: str):
        self.name = name
        self.tax_id = tax_id
        self.accounts: List[Account] = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.tax_id})"

# ==========================================
# 5. SYSTEM MANAGEMENT (Persistence & Analytics)
# ==========================================
class BankSystem:
    """Core system for data persistence and reporting analytics."""
    def __init__(self, data_file="bank_data.json"):
        self.data_file = data_file
        self.accounts: List[Account] = []

    def save_data(self):
        serialized_data = []
        for acc in self.accounts:
            serialized_data.append({
                "owner": acc.owner,
                "balance": acc._balance,
                "history": [t.__dict__ for t in acc._transaction_history]
            })
        with open(self.data_file, "w") as f:
            json.dump(serialized_data, f, indent=4)

    def get_top_performing_accounts(self, count=3):
        return sorted(self.accounts, key=lambda x: x._balance, reverse=True)[:count]