from banking_modules import Account, get_exchange_rates

if __name__ == "__main__":
    print("--- 🏦 BANKA SİSTEMİ TESTİ BAŞLIYOR ---")

    # 1. Hesap Oluşturma (Sadece Account sınıfımız var)
    my_account = Account(owner="Sinem Onar", currency="TRY")

    # 2. Para Yatırma İşlemleri
    my_account.deposit(1000, "Maas Yatis")
    my_account.deposit(500, "Ek Gelir")

    # 3. Para Çekme İşlemi
    my_account.withdraw(200, "Market Alisverisi")

    # 4. Hata Testi (Yetersiz Bakiye)
    my_account.withdraw(5000, "Araba Alimi")

    # 5. Hesap Geçmişini Göster
    my_account.show_history()

    # 6. Algoritma 1: İşlem Arama
    print("\n--- 🔍 Arama Testi ---")
    my_account.search_transactions("Market")

    # 7. Algoritma 2: Bakiye Doğrulama (Döngü ile)
    my_account.calculate_balance_from_history()

    # 8. Algoritma 3: Web'den Veri Çekme
    print("\n--- 🌍 Döviz Kuru Testi ---")
    get_exchange_rates()
