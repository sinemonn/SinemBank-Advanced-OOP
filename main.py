from banking_modules import Account, get_exchange_rates
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
