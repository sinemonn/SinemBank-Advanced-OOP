import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# --- STAGE 3: CUSTOM EXCEPTIONS ---
class InsufficientFundsError(Exception):
    """Custom exception for professional error handling."""
    pass

# --- STAGE 1 & 2: VALUE OBJECTS & OPERATOR OVERLOADING ---
@dataclass(frozen=True)
class Money:
    """Immutable money object with operator overloading."""
    amount: float
    currency: str = "TRY"

    def __add__(self, other): # Stage 2 Requirement
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other): # Stage 2 Requirement
        if self.amount < other.amount:
            raise InsufficientFundsError("Insufficient balance for this operation.")
        return Money(self.amount - other.amount, self.currency)

# --- STAGE 1: ABSTRACTION ---
class AbstractAccount(ABC):
    """Abstract base class for SinemBank accounts."""
    def __init__(self, account_id, owner, balance=0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    @abstractmethod
    def deposit(self, amount: float): pass

    @abstractmethod
    def withdraw(self, amount: float): pass

# --- STAGE 3: INHERITANCE & POLYMORPHISM ---
class SavingsAccount(AbstractAccount):
    """Polymorphic implementation for Savings."""
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount} at {datetime.now()}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        raise InsufficientFundsError("Savings balance too low.")

    def calculate_interest(self): # Specific algorithm
        return self.balance * 0.05

class CheckingAccount(AbstractAccount):
    """Polymorphic implementation for Checking with Overdraft."""
    def __init__(self, account_id, owner, balance=0.0, limit=1000.0):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance + self.overdraft_limit) >= amount:
            self.balance -= amount
            return True
        raise InsufficientFundsError("Overdraft limit exceeded.")

# --- STAGE 3: ADVANCED SYSTEM LOGIC ---
class BankSystem:
    def __init__(self, data_file='bank_data.json'):
        self.data_file = data_file
        self.accounts = []
        self.load_persistence()

    def load_persistence(self):
        """Loads and maps JSON data to SinemBank account objects."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for acc in data:
                    # Mapping to SavingsAccount for the simulation
                    self.accounts.append(SavingsAccount(acc['id'], acc['owner'], acc['balance']))
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = []

    def get_top_3_accounts(self):
        """Requirement: Data Analytics Sorting Algorithm."""
        return sorted(self.accounts, key=lambda x: x.balance, reverse=True)[:3]

    def detect_fraud(self, amount):
        """Requirement: Fraud Detection Security Routine."""
        if amount > 20000:
            return "ALERT: Possible Fraudulent Activity Detected!"
        return "Transaction Status: SECURE"

    def search_accounts(self, name_query):
        """Requirement: Transaction Search & Filtering."""
        return [acc for acc in self.accounts if name_query.lower() in acc.owner.lower()]