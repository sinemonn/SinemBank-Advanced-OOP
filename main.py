from banking_modules import Account, get_exchange_rates

if __name__ == "__main__":
    print("--- 🏦 BANK SYSTEM TEST STARTING ---")

    # 1. Create Account
    my_account = Account(owner="Sinem Onar", currency="TRY")

    # 2. Deposit Operations
    my_account.deposit(1000, "Salary Deposit")
    my_account.deposit(500, "Extra Income")

    # 3. Withdrawal Operation
    my_account.withdraw(200, "Grocery Shopping")

    # 4. Error Test (Insufficient Funds)
    my_account.withdraw(5000, "Car Purchase")

    # 5. Show History
    my_account.show_history()

    # 6. Algorithm 1: Search
    print("\n--- 🔍 Search Test ---")
    my_account.search_transactions("Grocery")

    # 7. Algorithm 2: Balance Verification
    my_account.calculate_balance_from_history()

    # 8. Algorithm 3: Web Data
    print("\n--- 🌍 Exchange Rate Test ---")
    get_exchange_rates()


