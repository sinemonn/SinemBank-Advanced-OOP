import json
import requests
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# --- STAGE 3: CUSTOM EXCEPTION ---
class InsufficientFundsError(Exception):
    """Stage 3: Custom error handling requirement."""
    pass

# --- STAGE 1 & 2: VALUE OBJECTS ---
@dataclass(frozen=True)
class Money:
    """Stage 1: Immutability & Stage 2: Operator Overloading."""
    amount: float
    currency: str = "TRY"

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.amount < other.amount:
            raise InsufficientFundsError("Bakiye yetersiz.")
        return Money(self.amount - other.amount, self.currency)

# --- STAGE 1: MODEL CLASSES ---
class Transaction:
    """Stage 1: Transaction model class requirement."""
    def __init__(self, amount, t_type):
        self.amount = amount
        self.t_type = t_type
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Customer:
    """Stage 1: Customer model class requirement."""
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

# --- STAGE 1: ABSTRACTION ---
class AbstractAccount(ABC):
    def __init__(self, account_id, owner: Customer, balance=0.0):
        self._account_id = account_id # Encapsulation
        self._owner = owner
        self._balance = balance
        self._history = [] # Transaction logs

    @property
    def balance(self): return self._balance

    @abstractmethod
    def deposit(self, amount: float): pass

    @abstractmethod
    def withdraw(self, amount: float): pass

# --- STAGE 3: INHERITANCE & POLYMORPHISM ---
class SavingsAccount(AbstractAccount):
    def deposit(self, amount):
        self._balance += amount
        self._history.append(Transaction(amount, "Deposit"))

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self._history.append(Transaction(amount, "Withdrawal"))
            return True
        raise InsufficientFundsError("Yetersiz bakiye.")

    def calculate_interest(self): # Stage 3 Algorithmic
        return self._balance * 0.05

class CheckingAccount(AbstractAccount):
    def __init__(self, account_id, owner, balance=0.0, limit=1000.0):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = limit

    def deposit(self, amount):
        self._balance += amount
        self._history.append(Transaction(amount, "Deposit"))

    def withdraw(self, amount):
        if (self._balance + self.overdraft_limit) >= amount:
            self._balance -= amount
            self._history.append(Transaction(amount, "Withdrawal"))
            return True
        raise InsufficientFundsError("Limit aşıldı.")

# --- STAGE 1: BANK CLASS (SYSTEM) ---
class BankSystem:
    def __init__(self, data_file='bank_data.json'):
        self.data_file = data_file
        self.accounts = []
        self.load_persistence()

    def get_exchange_rates(self):
        """Stage 2: Collect currency rates from web."""
        try:
            # Simüle edilmiş API çağrısı
            return 30.45 
        except: return 30.0

    def load_persistence(self):
        """Stage 3: Data persistence simulation."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    c = Customer(item['owner'], item['id'])
                    self.accounts.append(SavingsAccount(item['id'], c, item['balance']))
        except: self.accounts = []

    def detect_fraud(self, amount): # Stage 3 Algorithmic
        return "ALERT" if amount > 20000 else "Safe"

    def get_top_3_accounts(self): # Stage 3 Algorithmic
        return sorted(self.accounts, key=lambda x: x.balance, reverse=True)[:3]

    def search_accounts(self, query): # Stage 2 Algorithmic
        return [a for a in self.accounts if query.lower() in a._owner.name.lower()]