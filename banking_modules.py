import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# --- STAGE 1 & 2: Value Objects & Operator Overloading ---
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "TRY"

    def __add__(self, other): # Operator Overloading
        return Money(self.amount + other.amount)

# --- STAGE 1: Abstraction ---
class AbstractAccount(ABC): # Base class with Abstraction
    def __init__(self, account_id, owner, balance=0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.transactions = []

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

# --- STAGE 3: Polymorphism (Savings vs Checking) ---
class SavingsAccount(AbstractAccount):
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({"type": "Deposit", "amount": amount, "date": str(datetime.now())})

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({"type": "Withdrawal", "amount": amount, "date": str(datetime.now())})
            return True
        return False

    def calculate_interest(self): # Algorithmic Requirement: Interest
        return self.balance * 0.05

class CheckingAccount(AbstractAccount):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        # Checking accounts might have a credit limit
        limit = 500
        if (self.balance + limit) >= amount:
            self.balance -= amount
            return True
        return False

# --- STAGE 2 & 3: Bank System & Data Analytics ---
class BankSystem:
    def __init__(self, data_file='bank_data.json'):
        self.data_file = data_file
        self.accounts = []
        self.load_data()

    def load_data(self): # Senin eski kodundaki JSON mantığını buraya aldık
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                # Veriyi uygun sınıflara (Savings/Checking) dönüştürerek yükle
                for acc in data:
                    self.accounts.append(SavingsAccount(acc['id'], acc['owner'], acc['balance']))
        except FileNotFoundError:
            self.accounts = []

    # --- ALGORITHMIC REQUIREMENTS ---
    
    def get_top_3_accounts(self): # Data Analytics: Top 3
        return sorted(self.accounts, key=lambda x: x.balance, reverse=True)[:3]

    def detect_fraud(self, amount): # Fraud Detection Routine
        if amount > 10000: 
            return "WARNING: Suspicious high-value transaction!"
        return "Transaction Secure"

    def search_transactions(self, owner_name): # Search & Filtering
        return [acc for acc in self.accounts if owner_name.lower() in acc.owner.lower()]