# Esenyurt Bank - Advanced Banking Management System 🏦

This project is a modular, secure, and user-friendly banking management application developed as a **Software Engineering** project at **Istanbul Esenyurt University**.

## 🌟 Project Highlights
The system is designed with a focus on **Object-Oriented Programming (OOP)** principles, data integrity, and a professional user experience.

### 🖥️ Modern User Interface (UI)
- Developed using the `CustomTkinter` library for a high-performance, dark-mode compatible interface.
- Features a streamlined management panel for personnel interactions.

### 🛠️ Engineering & Architecture
- **Immutability:** Uses `@dataclass(frozen=True)` for financial objects (`Money`) to ensure data cannot be altered unintentionally after creation.
- **Custom Error Handling:** Implements specialized exceptions like `InsufficientFundsError` to manage banking logic errors gracefully.
- **Persistence:** All account data is stored and managed via a local `bank_data.json` database.

### 📊 Reporting & Verification (Instructor Requirements)
- **Automated Reporting:** Includes a module to generate a system status report in `.txt` format for auditing purposes.
- **Unit Testing:** Integrated `unittest` suite ensures that the core banking logic is verified and bug-free.

---

## 📂 Directory Structure
```text
BANKING-PROJECT/
├── ui_main.py            # Main GUI Entry Point
├── banking_modules.py    # Backend Logic & Class Models
├── test_banking.py       # Unit Testing Suite
├── bank_data.json        # Data Storage
└── readme.md             # Project Documentation