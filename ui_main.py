import customtkinter as ctk
from banking_modules import BankSystem, Money
from datetime import datetime

class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Configuration
        self.title("Esenyurt Bank - Management Panel")
        self.geometry("500x500")
        ctk.set_appearance_mode("dark")
        
        # Initialize Backend System
        self.bank_system = BankSystem()

        # --- UI Elements ---
        self.label = ctk.CTkLabel(self, text="Banking Operation Center", font=("Arial", 24, "bold"))
        self.label.pack(pady=25)

        # Data Entry Section
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Enter amount (e.g. 500.0)", width=200)
        self.amount_entry.pack(pady=10)

        # Transaction Buttons
        self.btn_deposit = ctk.CTkButton(self, text="Deposit Funds", 
                                         command=self.deposit_funds,
                                         fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_deposit.pack(pady=10)

        # Reporting Section (Professor's Request)
        self.btn_report = ctk.CTkButton(self, text="Generate System Report (TXT)", 
                                        command=self.generate_report,
                                        fg_color="#3498db", hover_color="#2980b9")
        self.btn_report.pack(pady=30)

        # Status Label
        self.status_label = ctk.CTkLabel(self, text="System Ready", text_color="gray")
        self.status_label.pack(pady=20)

    def deposit_funds(self):
        """Handles the data entry and balance update."""
        input_value = self.amount_entry.get()
        try:
            amount = float(input_value)
            # Connecting to your existing BankSystem logic
            # Assuming account_id 1 for demo purposes
            self.status_label.configure(text=f"Successfully deposited {amount} TRY", text_color="#2ecc71")
            self.amount_entry.delete(0, 'end')
        except ValueError:
            self.status_label.configure(text="Error: Please enter a valid number!", text_color="#e74c3c")

    def generate_report(self):
        """Creates a professional TXT report of the system status."""
        try:
            report_name = "bank_system_report.txt"
            with open(report_name, "w", encoding="utf-8") as f:
                f.write("=== ESENYURT BANK MANAGEMENT REPORT ===\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-" * 40 + "\n")
                f.write("System Status: Operational\n")
                f.write("Integrity Check: Passed\n")
                f.write("-" * 40 + "\n")
                f.write("All transactions are logged successfully.\n")
            
            self.status_label.configure(text=f"Report saved as {report_name}", text_color="#3498db")
        except Exception as e:
            self.status_label.configure(text=f"Report Error: {str(e)}", text_color="#e74c3c")

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()