from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# ================================
# 1. VALUE OBJECTS (IMMUTABILITY)
# ================================

@dataclass(frozen=True)
class Money:
    """Para birimi ve tutarı tutan, değiştirilemez (Immutable) sınıf."""
    amount: float
    currency: str = "TRY"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"
    
    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Para birimleri eşleşmiyor veya geçersiz işlem.")

@dataclass(frozen=True)
class Transaction:
    """Değiştirilemez işlem kaydı."""
    amount: Money
    description: str
    transaction_type: str  # 'CR' (Credit/Yatırılan) veya 'DR' (Debit/Çekilen)

# ================================
# 2. ABSTRACTION (AbstractAccount)
# ================================

class AbstractAccount(ABC):
    """Hesap işlemleri için Soyut Temel Sınıf (Abstract Base Class)."""

    def __init__(self, acc_no: str):
        self.acc_no = acc_no
        self._balance = Money(0.0)
        self._transactions: List[Transaction] = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Yatırılacak tutar pozitif olmalı.")
        
        # Money objesi immutable olduğu için yeni bir obje oluşturuyoruz
        deposit_money = Money(amount)
        self._balance = self._balance + deposit_money
        
        # İşlemi geçmişe ekle
        self._transactions.append(Transaction(deposit_money, "Para Yatırma", "CR"))
        print(f"[{self.acc_no}] Hesabına {deposit_money} yatırıldı.")

    @abstractmethod
    def calculate_interest(self):
        pass

    def __str__(self):
        return f"Hesap No: {self.acc_no} | Bakiye: {self._balance}"

# ================================
# 3. CONCRETE CLASSES
# ================================

class Account(AbstractAccount):
    """Vadesiz Hesap Sınıfı."""
    def calculate_interest(self):
        return Money(0.0) # Vadesiz hesapta faiz yok

class SavingsAccount(AbstractAccount):
    """Vadeli Hesap Sınıfı."""
    interest_rate = 0.05

    def calculate_interest(self):
        interest_amount = self._balance.amount * self.interest_rate
        return Money(interest_amount)

# ================================
# 4. CUSTOMER & BANK SYSTEM
# ================================

class Customer:
    def __init__(self, name: str, tax_id: str):
        self.name = name
        self.tax_id = tax_id
        self.accounts: List[AbstractAccount] = []

    def add_account(self, account: AbstractAccount):
        self.accounts.append(account)

    def __str__(self):
        return f"Müşteri: {self.name} (ID: {self.tax_id})"

class Bank:
    """Bankacılık sistemini yöneten ana sınıf."""
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"SİSTEM: {customer.name} bankaya müşteri olarak eklendi.")

    def list_customers(self):
        print(f"\n--- {self.name} MÜŞTERİ RAPORU ---")
        for cust in self.customers:
            print(f"- {cust}")
            for acc in cust.accounts:
                print(f"    -> {acc}")
        print("----------------------------------\n")

# ================================
# MAIN EXECUTION
# ================================

if __name__ == "__main__":
    # 1. Banka Kurulumu
    my_bank = Bank("Python Bank")

    # 2. Müşteri Tanımlama
    sinem = Customer("Sinem Onar", "12345678901")

    # 3. Hesap Açılışları
    acc1 = Account("TR-VADESIZ-01")
    acc2 = SavingsAccount("TR-VADELI-02")

    # 4. İşlemler
    acc1.deposit(1000)
    acc2.deposit(5000)

    # 5. İlişkilendirme
    sinem.add_account(acc1)
    sinem.add_account(acc2)
    my_bank.add_customer(sinem)

    # 6. Raporlama
    my_bank.list_customers()
