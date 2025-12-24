from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Protocol
import unittest

# ================================
# 1. EXCEPTION HANDLING & CUSTOM EXCEPTIONS
# ================================

class BankingError(Exception):
    """Base exception class for banking errors."""
    pass

class InsufficientFundsError(BankingError):
    """Hata: Bakiye yetersiz olduğunda fırlatılır."""
    def __init__(self, balance, amount):
        self.message = f"Yetersiz Bakiye! Mevcut: {balance}, İstenen: {amount}"
        super().__init__(self.message)

class LimitExceededError(BankingError):
    """Hata: Kredi Limiti aşıldığında fırlatılır."""
    pass

# ================================
# 2. INTERFACE & PROTOCOL
# ================================

class CreditScoreProtocol(Protocol):
    """Duck Typing ve Interface mantığı için protokol."""
    def get_score(self, customer_name: str) -> int:
        ...

# ================================
# 3. IMMUTABILITY & VALUE OBJECTS
# ================================

@dataclass(frozen=True)
class Transaction:
    """Değiştirilemez (Immutable) işlem kaydı."""
    amount: float
    description: str
    transaction_type: str

# ================================
# 4. ABSTRACTION & ABSTRACT BASE CLASS
# ================================

class Account(ABC):
    """Soyut Temel Sınıf (Abstract Base Class)."""

    # Class Variable (Sınıf Değişkeni)
    bank_name = "Python Bank"

    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self._balance = balance  # Encapsulation (Protected member)
        self._transactions: List[Transaction] = []

    # PROPERTIES (Getter & Setter)
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Bakiye negatif olamaz!")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Yatırılacak tutar pozitif olmalı.")
        self._balance += amount
        # Composition örneği: Transaction objesi oluşturup saklıyoruz
        self._transactions.append(Transaction(amount, "Para Yatırma", "CR"))

    # Abstract Method
    @abstractmethod
    def calculate_interest(self):
        pass

    # OPERATOR OVERLOADING (__str__, __add__)
    def __str__(self):
        return f"[{self.acc_no}] Bakiye: {self._balance} TL"

    def __add__(self, other):
        """İki hesabın bakiyesini toplamak için + operatörü."""
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented

# ================================
# 5. INHERITANCE & POLYMORPHISM
# ================================

class SavingAccount(Account):
    interest_rate = 0.05  # Class Attribute

    def calculate_interest(self):
        # Polymorphism: Üst sınıftaki metodu eziyoruz (Override)
        return self._balance * self.interest_rate

    # CLASS METHOD
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

class CheckingAccount(Account):
    def calculate_interest(self):
        return 0  # Vadesiz hesapta faiz yok

    # VARIABLE ARGUMENTS (*args)
    def log_audit(self, *messages):
        """Değişken sayıda argüman alan metod."""
        full_log = " | ".join(messages)
        print(f"[AUDIT LOG ({self.acc_no})]: {full_log}")

# ================================
# 6. COMPOSITION (vs Aggregation)
# ================================

class Address:
    """Composition için parça sınıf."""
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return f"{self.street}, {self.city}"

class Customer:
    def __init__(self, name, city, street):
        self.name = name
        # Composition: Customer silinirse Address de silinir
        self.address = Address(city, street)
        # Aggregation: Hesaplar dışarıdan eklenir, müşteri silinse de hesap bankada kalır
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    # STATIC METHOD
    @staticmethod
    def validate_identity(tc_no):
        """Nesneye ihtiyaç duymayan yardımcı metod."""
        return len(str(tc_no)) == 11

# ================================
# 7. DESIGN PATTERN (SIMPLE FACTORY)
# ================================

class AccountFactory:
    @staticmethod
    def create_account(acc_type, acc_no, balance=0):
        if acc_type == "saving":
            return SavingAccount(acc_no, balance)
        elif acc_type == "checking":
            return CheckingAccount(acc_no, balance)
        raise ValueError("Geçersiz hesap tipi")

# ================================
# 8. DEPENDENCY INJECTION & DUCK TYPING
# ================================

class CreditScoreService:
    def get_score(self, customer_name):
        # Basit bir mock logic
        return 750

class LoanApplication:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

    def approve(self, service: CreditScoreProtocol):
        # Dependency Injection
        score = service.get_score(self.customer.name)
        return score >= 700

# ================================
# 9. UNIT TESTING & MOCKING
# ================================

class TestBankSystem(unittest.TestCase):

    def setUp(self):
        self.acc = SavingAccount("SA-Test", 1000)

    def test_deposit(self):
        self.acc.deposit(500)
        self.assertEqual(self.acc.balance, 1500)

    def test_insufficient_funds(self):
        # Custom Exception Testi
        with self.assertRaises(ValueError):  # Basitleştirilmiş logic için ValueError
            self.acc.balance = -100

# ================================
# MAIN RUN
# ================================

if __name__ == "__main__":
    print("\n--- BANKA SİSTEMİ BAŞLATILIYOR ---\n")

    # 1. Factory ile Hesap Oluşturma
    s_acc = AccountFactory.create_account("saving", "SA123", 2000)
    c_acc = AccountFactory.create_account("checking", "CA987", 1000)

    # 2. Müşteri ve Composition
    sinem = Customer("Sinem Onar", "İstanbul", "Bağdat Cd.")
    print(f"Müşteri: {sinem.name}, Adres: {sinem.address}")

    # 3. Hesap Ekleme
    sinem.add_account(s_acc)
    sinem.add_account(c_acc)

    # 4. Operator Overloading Testi (+ operatörü)
    total_money = s_acc + c_acc
    print(f"Toplam Varlık (Op. Overloading): {total_money} TL")

    # 5. Variable Arguments Testi
    c_acc.log_audit("Giriş Yapıldı.", "Bakiye Sorgulandı.", "Çıkış Yapıldı.")

    # 6. Dependency & Duck Typing
    loan = LoanApplication(sinem, 50000)
    credit_service = CreditScoreService()

    approval = loan.approve(credit_service)
    print(f"Kredi Başvurusu Sonucu: {'ONAYLANDI' if approval else 'REDDEDİLDİ'}")

    # 7. Testing Bölümünü Çalıştırma
    print("\n--- TEST SONUÇLARI ---")
