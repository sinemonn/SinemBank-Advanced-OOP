import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# --- STAGE 1 & 2: Value Objects & Operator Overloading ---
@dataclass(frozen=True)
class Money:
    """Value object with immutability principles."""
    amount: float
    currency: str = "TRY"

    def __add__(self, other): # Stage 2: Operator Overloading
        return Money(self.amount + other.amount)
    
    def __sub__(self, other): # Stage 2: Operator Overloading
        return Money(self.amount - other.amount)

# --- STAGE 1: Abstraction ---
class AbstractAccount(ABC):
    """Abstract base class for all account types."""
    def __init__(self, account_id, owner, balance=0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.transaction_logs = []

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

# --- STAGE 3: Polymorphism (Savings vs Checking) ---
class SavingsAccount(AbstractAccount):
    """Subclass with interest computation logic."""
    def deposit(self, amount):
        self.balance += amount
        self.transaction_logs.append(f"Deposited: {amount} at {datetime.now()}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def calculate_interest(self): # Stage 3: Interest Computation
        return self.balance * 0.05

class CheckingAccount(AbstractAccount):
    """Subclass with credit limits."""
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        limit = 500
        if (self.balance + limit) >= amount:
            self.balance -= amount
            return True
        return False

# --- STAGE 3: Advanced Application Logic ---
class BankSystem:
    def __init__(self, data_file='bank_data.json'):
        self.data_file = data_file
        self.accounts = []
        self.load_persistence()

    def load_persistence(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for acc in data:
                    # Defaulting to SavingsAccount for simulation
                    self.accounts.append(SavingsAccount(acc['id'], acc['owner'], acc['balance']))
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = []

    def get_top_3_accounts(self): # Stage 3: Data Analytics Output
        return sorted(self.accounts, key=lambda x: x.balance, reverse=True)[:3]

    def detect_fraud(self, amount): # Stage 3: Fraud Detection Routine
        if amount > 20000:
            return "ALERT: Possible Fraudulent Activity!"
        return "Normal"

    def search_accounts(self, name_query): # Stage 2: Search & Filter Algorithm
        return [acc for acc in self.accounts if name_query.lower() in acc.owner.lower()]