SinemBank - Advanced Banking & Payment System 🏦💖
SinemBank is a high-security banking management simulation developed using Object-Oriented Programming (OOP) principles in Python. This project was created as the first assignment for the Advanced Object-Oriented Programming course at Istanbul Esenyurt University, Faculty of Engineering and Architecture.

🌟 Project Highlights
The system is designed with a focus on modular architecture, data integrity, and a professional user experience.

🎀 Modern Pink Interface (UI)
Developed using the CustomTkinter library for a high-performance, dark-mode compatible interface.

Features a unique Vibrant Pink (#FF69B4) and Deep Pink (#FF1493) theme, representing the SinemBank corporate identity.

🛠️ Architecture & Engineering (Stage 1 & 2)
Abstraction: Implements an AbstractAccount base class to standardize transaction processing.

Immutability: Financial data is managed via the Money value object using @dataclass(frozen=True) to prevent unintended modifications.

Operator Overloading: Custom + and - operators are implemented within the Money class for seamless financial calculations.

Web Integration: Utilizes the requests library to fetch real-time foreign currency exchange rates.

📊 Advanced Functionalities (Stage 3)
Polymorphism: Includes specialized subclasses like SavingsAccount (with interest logic) and CheckingAccount (with overdraft limits).

Fraud Detection: An automated security routine that flags suspicious transactions exceeding 20,000 TRY.

Data Analytics: Features a real-time analytics engine to output the "Top 3" accounts by balance volume.

Unit Testing: The core banking logic is verified by a comprehensive unittest suite to ensure a bug-free system.

## 📂 Directory Structure
SINEMBANK-PROJECT/
├── ui_main.py            # Main GUI Entry Point (Pink Theme)
├── banking_modules.py    # Backend Logic & OOP Class Models
├── test_banking.py       # Unit Testing Suite
├── bank_data.json        # Persistent JSON Data Storage
└── README.md             # Project Documentation
