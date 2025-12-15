from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
import json
import urllib.request

# ==========================================
# 1. MONEY CLASS
# ==========================================

@dataclass(frozen=True)
class Money:
    """Immutable class to store currency and amount."""
    amount: float
    currency: str = "TRY"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Currency mismatch or invalid operation.")

    def __sub__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        raise ValueError("Currency mismatch or invalid operation.")

# ==========================================
# 2. TRANSACTION CLASS
# ==========================================

@dataclass(frozen=True)
class Transaction:
    """Records individual transactions (deposit/withdrawal)."""
    description: str
    amount: Money
    date: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f"[{self.date.strftime('%Y-%m-%d %H:%M')}] {self.description}: {self.amount}"

# ==========================================
# 3. ACCOUNT CLASS
# ==========================================

class Account:
    """Main class to manage bank accounts."""
    def __init__(self, owner: str, currency: str = "TRY"):
        self.owner = owner
        self.currency = currency
        self.__balance = Money(0.0, currency) 
        self.__transaction_history: List[Transaction] = []

    def deposit(self, amount: float, description: str = "Deposit"):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        
        money_obj = Money(amount, self.currency)
        self.__balance = self.__balance + money_obj
        
        transaction = Transaction(description=description, amount=money_obj)
        self.__transaction_history.append(transaction)
        print(f"✅ {amount} {self.currency} deposited. New Balance: {self.__balance}")

    def withdraw(self, amount: float, description: str = "Withdrawal"):
        if amount <= 0:
            print("Error: Amount must be positive.")
            return

        if self.__balance.amount < amount:
            print(f"❌ Error: Insufficient funds! Current: {self.__balance}")
            return

        money_obj = Money(amount, self.currency)
        self.__balance = self.__balance - money_obj

        # Negative amount for logic consistency
        transaction = Transaction(description=description, amount=Money(-amount, self.currency))
        self.__transaction_history.append(transaction)
        print(f"✅ {amount} {self.currency} withdrawn. New Balance: {self.__balance}")

    def show_history(self):
        print(f"\n--- Account Statement: {self.owner} ---")
        for t in self.__transaction_history:
            print(t)
        print(f"FINAL BALANCE: {self.__balance}\n")

    # --- REQUIRED ALGORITHMS ---

    def search_transactions(self, keyword: str):
        print(f"\n🔍 Search Results: '{keyword}'")
        results = [t for t in self.__transaction_history if keyword.lower() in t.description.lower()]
        if not results:
            print("No results found.")
        for t in results:
            print(t)

    def calculate_balance_from_history(self):
        """Calculates balance by iterating through history."""
        print("\n🔄 Algorithm: Recalculating balance from history...")
        total = 0.0
        for t in self.__transaction_history:
            total += t.amount.amount
        print(f"Verified Balance: {total:.2f} {self.currency}")
        return Money(total, self.currency)

# ==========================================
# 4. WEB DATA FETCHING
# ==========================================

def get_exchange_rates():
    """Fetches real-time data. Uses backup if offline."""
    print("\n🌍 Fetching Exchange Rates from Web...")
    
    url = "https://api.exchangerate-api.com/v4/latest/TRY"
    
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        
        rates = {
            "USD": 1 / data['rates']['USD'],
            "EUR": 1 / data['rates']['EUR'],
            "GBP": 1 / data['rates']['GBP']
        }
        print("✅ Connection Successful! Rates updated.")
        return rates

    except Exception as e:
        print(f"⚠️ Web error: {e}")
        print("⚠️ Using backup (offline) rates.")
        return {"USD": 34.50, "EUR": 36.20, "GBP": 42.10}
