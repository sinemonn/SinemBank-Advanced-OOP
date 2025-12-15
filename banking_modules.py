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
    """Para birimi ve tutarı tutan, değiştirilemez (Immutable) sınıf."""
    amount: float
    currency: str = "TRY"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Para birimleri eşleşmiyor veya geçersiz işlem.")

    def __sub__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        raise ValueError("Para birimleri eşleşmiyor veya geçersiz işlem.")

# ==========================================
# 2. TRANSACTION CLASS
# ==========================================

@dataclass(frozen=True)
class Transaction:
    """Her bir işlemi (yatırma/çekme) kayıt altına alan sınıf."""
    description: str
    amount: Money
    date: datetime = field(default_factory=datetime.now)

    def __str__(self):
        return f"[{self.date.strftime('%Y-%m-%d %H:%M')}] {self.description}: {self.amount}"

# ==========================================
# 3. ACCOUNT CLASS
# ==========================================

class Account:
    """Banka hesabını yöneten ana sınıf."""
    def __init__(self, owner: str, currency: str = "TRY"):
        self.owner = owner
        self.currency = currency
        self.__balance = Money(0.0, currency) 
        self.__transaction_history: List[Transaction] = []

    def deposit(self, amount: float, description: str = "Para Yatırma"):
        if amount <= 0:
            print("Hata: Tutar pozitif olmalı.")
            return
        
        money_obj = Money(amount, self.currency)
        self.__balance = self.__balance + money_obj
        
        transaction = Transaction(description=description, amount=money_obj)
        self.__transaction_history.append(transaction)
        print(f"✅ {amount} {self.currency} yatırıldı. Yeni Bakiye: {self.__balance}")

    def withdraw(self, amount: float, description: str = "Para Çekme"):
        if amount <= 0:
            print("Hata: Tutar pozitif olmalı.")
            return

        if self.__balance.amount < amount:
            print(f"❌ Hata: Yetersiz bakiye! Mevcut: {self.__balance}")
            return

        money_obj = Money(amount, self.currency)
        self.__balance = self.__balance - money_obj

        # Algoritma için negatif tutarlı kayıt
        transaction = Transaction(description=description, amount=Money(-amount, self.currency))
        self.__transaction_history.append(transaction)
        print(f"✅ {amount} {self.currency} çekildi. Yeni Bakiye: {self.__balance}")

    def show_history(self):
        print(f"\n--- {self.owner} Hesap Özeti ---")
        for t in self.__transaction_history:
            print(t)
        print(f"SON BAKİYE: {self.__balance}\n")

    # --- İSTENEN ALGORİTMALAR ---

    def search_transactions(self, keyword: str):
        print(f"\n🔍 Arama Sonuçları: '{keyword}'")
        results = [t for t in self.__transaction_history if keyword.lower() in t.description.lower()]
        if not results:
            print("Sonuç bulunamadı.")
        for t in results:
            print(t)

    def calculate_balance_from_history(self):
        """Geçmiş işlemleri döngü ile (iteration) toplayarak bakiye hesaplar."""
        print("\n🔄 Algoritma: Bakiye yeniden hesaplanıyor...")
        total = 0.0
        for t in self.__transaction_history:
            total += t.amount.amount
        print(f"Doğrulanan Bakiye: {total:.2f} {self.currency}")
        return Money(total, self.currency)

# ==========================================
# 4. WEB'DEN VERİ ÇEKME
# ==========================================

def get_exchange_rates():
    """Gerçek zamanlı veri çeker. İnternet yoksa yedek veriyi kullanır."""
    print("\n🌍 Web'den Döviz Kurları Çekiliyor...")
    
    url = "https://api.exchangerate-api.com/v4/latest/TRY"
    
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        
        rates = {
            "USD": 1 / data['rates']['USD'],
            "EUR": 1 / data['rates']['EUR'],
            "GBP": 1 / data['rates']['GBP']
        }
        print("✅ Bağlantı Başarılı! Güncel kurlar alındı.")
        return rates

    except Exception as e:
        print(f"⚠️ Web hatası: {e}")
        print("⚠️ Yedek (Offline) kurlar kullanılıyor.")
        return {"USD": 34.50, "EUR": 36.20, "GBP": 42.10}
