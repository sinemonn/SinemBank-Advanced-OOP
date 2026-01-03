# SinemBank - Advanced OOP Management System

## 1. Project Overview
**SinemBank** is a high-performance bank management engine developed as a final project for the Object-Oriented Programming (OOP) course. The system focuses on modular architecture, secure financial transactions, and real-time data analytics.

## 2. Technical Features & OOP Implementation
The project is built on three major stages, strictly following the course evaluation criteria:

* **Abstraction (Stage 1):** Utilizes an `AbstractAccount` base class to enforce a consistent blueprint for all financial products.
* **Inheritance & Polymorphism (Stage 3):** Features specialized `SavingsAccount` and `CheckingAccount` classes with unique withdrawal and interest computation logic.
* **Operator Overloading (Stage 2):** Implements a `Money` value object with overloaded `__add__` and `__sub__` operators for intuitive arithmetic.
* **Advanced Algorithms:** Includes a **Fraud Detection Routine** (monitoring high-volume transfers) and **Data Analytics** (sorting top accounts by balance).

## 3. Technology Stack
* **Language:** Python 3.x
* **UI Framework:** CustomTkinter (Modern Dark Mode UI)
* **Data Persistence:** JSON-based storage (`bank_data.json`)

## 4. Getting Started
To run the application locally:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/sinemonn/SinemBank-Advanced-OOP.git](https://github.com/sinemonn/SinemBank-Advanced-OOP.git)
    ```
2.  Install dependencies:
    ```bash
    pip install customtkinter
    ```
3.  Launch the UI:
    ```bash
    python ui_main.py
    ```

## 5. Project Structure
* `ui_main.py`: Modern user interface and event handling.
* `banking_modules.py`: Backend logic, OOP hierarchies, and algorithms.
* `DESIGN_DOC.md`: Detailed system architecture documentation.
* `bank_data.json`: Persistent storage for account information.

---
**Developer:** Sinem Onar  
**University:** Istanbul Esenyurt University  
**Department:** Software Engineering

---

## 📂 Directory Structure
```text
BANKING-PROJECT/
├── ui_main.py            # Main GUI Entry Point
├── banking_modules.py    # Backend Logic & Class Models
├── test_banking.py       # Unit Testing Suite
├── bank_data.json        # Data Storage
└── readme.md             # Project Documentation