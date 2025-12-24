from banking_modules import BankSystem, Account, SavingsAccount, Customer

def run_simulation():
    # 1. Initialize the Bank System
    system = BankSystem()
    print("--- 🏦 Banking System Simulation Started ---")

    # 2. Define Customers
    sinem = Customer("Sinem Onar", "12345678901")
    coskun = Customer("Coskun Sahin", "98765432109")

    # 3. Create and Link Accounts
    acc1 = Account("TR-CHECKING-01")
    acc2 = SavingsAccount("TR-SAVINGS-02", interest_rate=0.15)
    
    sinem.add_account(acc1)
    sinem.add_account(acc2)

    # 4. Perform Transactions
    print("\n--- 💸 Processing Transactions ---")
    acc1.deposit(1000, "Initial Deposit")
    acc2.deposit(5000, "Savings Startup")
    
    # NEW: Demonstrating Interest Computation Algorithm (Stage 3 Requirement)
    acc2.apply_interest() # Algorithmic check for interest

    # 5. Triggering Fraud Detection Algorithm
    print("\n--- 🛡️ Security Check: Fraud Detection ---")
    try:
        # High-value transaction to trigger alert
        acc1.withdraw(12000, "Suspicious Luxury Purchase") 
    except Exception as e:
        print(f"SECURITY ALERT: {e}")

    # 6. Data Analytics & Reporting
    print("\n--- 📊 DATA ANALYTICS: Top Performing Accounts ---")
    system.accounts.extend([acc1, acc2])
    top_accounts = system.get_top_performing_accounts(3) # Financial analytics
    
    for rank, acc in enumerate(top_accounts, 1):
        print(f"{rank}. {acc}")

    # 7. Save State to JSON (Persistence)
    system.save_data() # Saving to bank_data.json
    print("\n✅ Simulation Complete. All data persistent in JSON.")

if __name__ == "__main__":
    run_simulation()


