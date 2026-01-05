# SinemBank - Advanced Object-Oriented Management System 🏦✨

## 1. Project Overview
**SinemBank** is a comprehensive financial management engine developed for the Object-Oriented Programming (OOP) course. It integrates a **Modern Desktop Dashboard** for daily operations and a **Web Reporting Portal** for high-level analytics.

## 2. Visual Architecture & Design
The system architecture follows a strict class hierarchy to ensure scalability and security.

### 📊 Class Diagram (UML)
Below is the visual blueprint of the system, illustrating how different accounts and the core system interact:

![SinemBank UML Diagram](uml_diagram.png)

## 3. Core Technical Implementation
The project is structured across three developmental stages (S1, S2, S3), implementing key OOP pillars:

* **Abstraction (Stage 1):** Uses an `AbstractAccount` base class to enforce a consistent template for all account types.
* **Inheritance & Polymorphism (Stage 3):** Specialized `SavingsAccount` and `CheckingAccount` classes implement unique business logic for interest and withdrawals.
* **Encapsulation:** Sensitive data such as `_balance` and `_account_id` are protected, accessible only through secure properties.
* **Operator Overloading (Stage 2):** The `Money` class overloads `__add__` and `__sub__` for intuitive currency calculations.

## 4. Advanced Algorithmic Features
* **Fraud Detection Routine:** Real-time monitoring for high-volume transactions (e.g., > 20,000 TRY) with UI-based security alerts.
* **Data Analytics:** Custom sorting algorithms to identify and report the "Top 3 Accounts" by total balance.
* **Search & Filtering:** Case-insensitive search engine to filter accounts by customer names.

## 5. Technology Stack
* **Core Logic:** Python 3.14 (OOP Focused)
* **Desktop UI:** CustomTkinter (Modern Dark/Light Themes)
* **Web Portal:** Flask Web Server (RESTful approach for reporting)
* **Database:** JSON Data Persistence for local storage (`banka_verileri.json`)

## 6. 🚀 Getting Started
To launch the SinemBank ecosystem, use the following terminal commands:

1. **Launch Desktop Dashboard:**
   `python ui_main.py`
2. **Launch Web Reporting Portal:**
   `python web_app.py` (Access via http://127.0.0.1:5000)
3. **Execute Automated Testing:**
   `python test_bankacılık.py`

---

## 📂 Project Directory Structure (Detailed)
```text
BANKING-PROJECT/
├── ui_main.py                # Main Entry Point: Desktop Graphical User Interface
├── web_app.py                # Web Portal: Flask-based reporting server
├── bankacılık_modülleri.py    # Core Logic: All OOP Classes and Business Logic
├── ana.py                    # Script: Primary execution logic for back-end
├── modeller.py               # Data Models: Definitions for data structures
├── TASARIM_BELGESI.md        # Documentation: Deep dive into architectural design
├── uml_diagram.png           # Visual Design: The class relationship diagram
├── banka_verileri.json       # Database: Persistent storage for account records
├── banka_sistem_raporu.txt   # Reports: Auto-generated system audit logs
└── readme.md                 # Documentation: This overview file