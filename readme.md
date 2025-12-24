# 🏦 Banking and Payment System - Stage 3 Application

This project is an advanced banking simulation system developed as part of the **Software Engineering** curriculum at **Istanbul Esenyurt University**. It implements robust architectural patterns and data analytics, fulfilling all requirements for **Stage 3: Advanced Application**.

## 🚀 Key Engineering Features
The system is built with modularity and scalability in mind, utilizing advanced software design principles:

* **Advanced OOP Hierarchy:** Implements inheritance and polymorphism through the `Account` base class and its specialized subclasses: `SavingsAccount` and `CheckingAccount`.
* **Custom Exception Handling:** Utilizes a domain-specific `InsufficientFundsError` to manage transaction failures gracefully without interrupting the system flow.
* **Data Persistence (JSON):** Features a robust persistence layer where all account states and transaction histories are serialized into `bank_data.json`, ensuring data integrity across sessions.
* **Fraud Detection Engine:** Includes an automated monitoring routine that flags high-value transactions (above 10,000 TRY) as suspicious activities.

## 📊 Algorithmic Implementations
* **Financial Analytics:** An algorithm within the `BankSystem` class analyzes all active accounts to report the "Top 3 Performing Accounts" based on current balances.
* **Interest Computation:** `SavingsAccount` includes a specialized method for calculating and applying interest rates to the account balance automatically.

## 🧪 Unit Testing
The reliability of the system is verified using the `unittest` framework. The test suite covers balance validation, interest accuracy, and withdrawal limit constraints, ensuring the code meets engineering quality standards.

## 📂 Project Structure
* `banking_modules.py`: Core logic, classes, and custom exception definitions.
* `main.py`: Primary simulation script executing the Stage 3 lifecycle.
* `test_banking.py`: Automated unit tests for system verification.
* `DESIGN_DOC.md`: Detailed documentation of architectural design and OOP principles.

## 🛠️ Execution
1.  **Run Simulation:** `python main.py`
2.  **Run Unit Tests:** `python test_banking.py`

---
**Developer:** Sinem Onar
**Institution:** Istanbul Esenyurt University - Dept. of Software Engineering