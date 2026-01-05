from banking_modules import (
    BankSystem,
    SavingsAccount,
    CheckingAccount,
    Customer,
    Money,
    InsufficientFundsError
)

def run_simulation():
    system = BankSystem()
    print("--- 🏦 Banking System Simulation Started ---")

    # Customers
    sinem = Customer("Sinem Onar", 1)
    coskun = Customer("Coskun Sahin", 2)

    # Accounts
    acc1 = CheckingAccount(101, sinem, Money(2000))
    acc2 = SavingsAccount(102, sinem, Money(5000))

    system.accounts.extend([acc1, acc2])

    # Transactions
    print("\n--- 💸 Processing Transactions ---")
    acc1.deposit(Money(1000))
    acc2.deposit(Money(3000))

    # Interest (Stage 3)
    acc2.apply_interest()

    # Fraud Detection
    print("\n--- 🛡️ Fraud Detection ---")
    alert = system.detect_fraud(acc1, Money(25000))
    print("Fraud check result:", alert)

    # Analytics
    print("\n--- 📊 Top Accounts ---")
    for i, acc in enumerate(system.top_3_accounts(), 1):
        print(f"{i}. Account ID: {acc._account_id}, Balance: {acc.balance}")

    # Persistence
    system.save_data()
    print("\n✅ Simulation completed successfully.")

if __name__ == "__main__":
    run_simulation()
