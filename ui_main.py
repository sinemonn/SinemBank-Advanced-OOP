import customtkinter as ctk
from banking_modules import BankSystem # Backend dosyasından sistemi çekiyoruz
from tkinter import messagebox

class BankManagementUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Esenyurt Bank - Advanced System")
        self.geometry("600x700")
        ctk.set_appearance_mode("dark")
        
        self.bank_engine = BankSystem()

        # UI Elements (Buttons, Inputs, etc.)
        self.header = ctk.CTkLabel(self, text="Banking Control Center", font=("Helvetica", 24, "bold"))
        self.header.pack(pady=20)

        # Search
        self.search_input = ctk.CTkEntry(self, placeholder_text="Filter by Name...")
        self.search_input.pack(pady=10)
        self.search_btn = ctk.CTkButton(self, text="Search", command=self.run_search)
        self.search_btn.pack()

        # Analytics
        self.analytics_btn = ctk.CTkButton(self, text="View Top 3 (Analytics)", 
                                           fg_color="#e67e22", command=self.display_analytics)
        self.analytics_btn.pack(pady=20)

        self.display_box = ctk.CTkTextbox(self, height=200, width=500)
        self.display_box.pack(pady=10)

    def run_search(self):
        query = self.search_input.get()
        matches = self.bank_engine.search_accounts(query)
        self.display_box.delete("1.0", "end")
        for acc in matches:
            self.display_box.insert("end", f"Owner: {acc.owner} | Balance: {acc.balance} TRY\n")

    def display_analytics(self):
        top_list = self.bank_engine.get_top_3_accounts()
        self.display_box.delete("1.0", "end")
        self.display_box.insert("end", "--- TOP ACCOUNTS --- \n")
        for i, acc in enumerate(top_list, 1):
            self.display_box.insert("end", f"{i}. {acc.owner} -> {acc.balance} TRY\n")

if __name__ == "__main__":
    app = BankManagementUI()
    app.mainloop()