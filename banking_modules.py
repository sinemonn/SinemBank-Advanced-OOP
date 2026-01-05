import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List

# =====================================================
# STAGE 3 – CUSTOM EXCEPTION
# =====================================================

class InsufficientFundsError(Exception):
    pass


# =====================================================
# STAGE 1 – VALUE OBJECT (IMMUTABLE)
# =====================================================

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "TRY"

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.amount < other.amount:
            raise InsufficientFundsError("Insufficient balance")
        return Money(self.amount - other.amount, self.currency)


# =====================================================
# STAGE 1 – MODEL CLASSES
# =====================================================

class Transaction:
    def __init__(self, amount: Money, t_type: str):
        self.amount = amount
        self.t_type = t_type
        self.timestamp = datetime.now()

class Customer:
    def __init__(self, name: str, customer_id: int):
        self.name = name
        self.customer_id = customer_id


# =====================================================
# STAGE 1 – ABSTRACTION
# =====================================================

class AbstractAccount(ABC):
    def __init__(self, account_id: int, owner: Customer, balance: Money):
        self._account_id = account_id
        self._owner = owner
        self._balance = balance
        self._history: List[Transaction] = []

    @property
    def balance(self):
        return self._balance.amount

    @abstractmethod
    def deposit(self, amount: Money): pass

    @abstractmethod
    def withdraw(self, amount: Money): pass

    # ---------- STAGE 2 ----------
    def running_balance(self):
        balance = Money(0)
        for t in self._history:
            if t.t_type in ("Deposit", "Interest"):
                balance += t.amount
            else:
                balance -= t.amount
        return balance.amount


# =====================================================
# STAGE 3 – INHERITANCE & POLYMORPHISM
# =====================================================

class SavingsAccount(AbstractAccount):
    INTEREST_RATE = 0.05

    def deposit(self, amount: Money):
        self._balance += amount
        self._history.append(Transaction(amount, "Deposit"))

    def withdraw(self, amount: Money):
        self._balance -= amount
        self._history.append(Transaction(amount, "Withdrawal"))

    # ---------- STAGE 3 ----------
    def apply_interest(self):
        interest = Money(self._balance.amount * self.INTEREST_RATE)
        self._balance += interest
        self._history.append(Transaction(interest, "Interest"))


class CheckingAccount(AbstractAccount):
    def __init__(self, account_id, owner, balance, overdraft_limit=Money(1000)):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: Money):
        self._balance += amount
        self._history.append(Transaction(amount, "Deposit"))

    def withdraw(self, amount: Money):
        if self._balance.amount + self.overdraft_limit.amount < amount.amount:
            raise InsufficientFundsError("Overdraft limit exceeded")
        self._balance = Money(self._balance.amount - amount.amount)
        self._history.append(Transaction(amount, "Withdrawal"))


# =====================================================
# STAGE 1–2–3 – BANK SYSTEM
# =====================================================

class BankSystem:
    def __init__(self, data_file="bank_data.json"):
        self.data_file = data_file
        self.accounts: List[AbstractAccount] = []
        self.load_data()

    # ---------- STAGE 3 ----------
    def add_account(self, name, initial_balance):
        cid = 1000 + len(self.accounts)
        customer = Customer(name, cid)
        acc = SavingsAccount(cid, customer, Money(initial_balance))
        self.accounts.append(acc)
        self.save_data()
        return acc

    # ---------- STAGE 2 ----------
    def search_transactions(self, account, t_type=None, min_amount=None):
        results = []
        for t in account._history:
            if t_type and t.t_type != t_type:
                continue
            if min_amount and t.amount.amount < min_amount:
                continue
            results.append(t)
        return results

    def generate_monthly_report(self, month, year):
        report = []
        for acc in self.accounts:
            for t in acc._history:
                if t.timestamp.month == month and t.timestamp.year == year:
                    report.append({
                        "account": acc._account_id,
                        "type": t.t_type,
                        "amount": t.amount.amount
                    })
        return report

    # ---------- STAGE 3 ----------
    def detect_fraud(self, account, amount: Money):
        recent = account._history[-3:]
        if amount.amount > 20000:
            return "ALERT: Large transaction"
        if len(recent) == 3 and all(t.t_type == "Withdrawal" for t in recent):
            return "ALERT: Frequent withdrawals"
        return "Safe"

    def top_3_accounts(self):
        return sorted(self.accounts, key=lambda a: a.balance, reverse=True)[:3]

    # ---------- PERSISTENCE ----------
    def save_data(self):
        data = []
        for acc in self.accounts:
            data.append({
                "id": acc._account_id,
                "owner": acc._owner.name,
                "balance": acc.balance
            })
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for d in data:
                    c = Customer(d["owner"], d["id"])
                    self.accounts.append(
                        SavingsAccount(d["id"], c, Money(d["balance"]))
                    )
        except:
            self.accounts = []
