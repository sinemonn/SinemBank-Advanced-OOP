# 📄 Design Documentation: Banking & Payment System (Stage 3)

This document details the architectural structure and software engineering principles implemented for the **Stage 3: Advanced Application** requirements of the Banking & Payment System.

## 1. Object-Oriented Programming (OOP) Principles
The system architecture is built upon the four pillars of OOP to ensure modularity, scalability, and maintainability:

* **Encapsulation:** Account balances (`_balance`) and transaction histories (`_transaction_history`) are defined as protected attributes. Direct access to these data points is restricted, ensuring that balance modifications occur only through controlled `deposit` and `withdraw` methods to maintain data integrity.
* **Inheritance:** A hierarchical structure is established where `SavingsAccount` and `CheckingAccount` subclasses inherit from the `Account` base class. This prevents code duplication while allowing specialized features for different account types.
* **Polymorphism:** The `withdraw` method is overridden within the `CheckingAccount` class to implement specific daily withdrawal limits. This allows the same method signature to exhibit different behaviors depending on the object type.
* **Abstraction:** Complex financial data is simplified into intuitive models through the `Money` and `Transaction` classes, hiding internal complexities from the high-level system logic.

## 2. Algorithmic Features and Logical Layer
Three core algorithmic functions have been implemented to add analytical value to the system:

* **Interest Computation:** An automated algorithm within the `SavingsAccount` class calculates and applies periodic interest to the current balance, documenting the gain in the transaction history.
* **Fraud Detection:** A security routine monitors withdrawals; any transaction exceeding 10,000 TRY is flagged as a "High-value transaction," triggering a system-level security alert.
* **Data Analytics (Reporting):** The `BankSystem` utilizes a sorting algorithm to analyze all managed accounts and generate a "Top-performing Accounts" report based on balance volume.

## 3. Data Management and Persistence
* **JSON Persistence:** The system implements a data persistence layer via the `BankSystem` class, which serializes account data into `bank_data.json`. This ensures that user data and histories are preserved even after the program is terminated.
* **Custom Exception Handling:** Beyond standard error types, a domain-specific `InsufficientFundsError` has been defined. This provides professional error feedback to the user and prevents system crashes during invalid transaction attempts.