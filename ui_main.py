import customtkinter as ctk
from banking_modules import BankSystem
from tkinter import messagebox

class BankManagementUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Configuration
        self.title("SinemBank - Advanced Management System")
        self.geometry("600x780")
        ctk.set_appearance_mode("dark")
        
        # Initialize Backend Engine
        self.bank_engine = BankSystem()

        # --- HEADER ---
        self.header = ctk.CTkLabel(self, text="SinemBank Control Center", font=("Helvetica", 28, "bold"))
        self.header.pack(pady=30)

        # --- SEARCH SECTION ---
        self.search_frame = ctk.CTkFrame(self)
        self.search_frame.pack(pady=10, padx=20, fill="x")
        
        self.search_input = ctk.CTkEntry(self.search_frame, placeholder_text="Filter accounts by owner name...")
        self.search_input.pack(side="left", padx=10, pady=10, expand=True, fill="x")
        
        self.search_btn = ctk.CTkButton(self.search_frame, text="Search", command=self.run_search)
        self.search_btn.pack(side="right", padx=10)

        # --- TRANSACTION & FRAUD SECTION ---
        self.trans_frame = ctk.CTkFrame(self)
        self.trans_frame.pack(pady=15, padx=20, fill="x")
        
        self.label_amount = ctk.CTkLabel(self.trans_frame, text="Secure Transaction Protocol", font=("Arial", 14, "italic"))
        self.label_amount.pack(pady=5)

        self.amount_input = ctk.CTkEntry(self.trans_frame, placeholder_text="Enter Amount (Fraud Detection Limit: 20k)")
        self.amount_input.pack(pady=10, padx=20, fill="x")

        self.deposit_btn = ctk.CTkButton(self.trans_frame, 
                                         text="Execute Secure Transaction", 
                                         fg_color="#27ae60", 
                                         hover_color="#2ecc71",
                                         command=self.process_deposit)
        self.deposit_btn.pack(pady=10)

        # --- ANALYTICS SECTION ---
        self.analytics_btn = ctk.CTkButton(self, text="View SinemBank Analytics (Top 3)", 
                                           fg_color="#e67e22", 
                                           hover_color="#d35400",
                                           command=self.display_analytics)
        self.analytics_btn.pack(pady=20)

        # --- OUTPUT AREA ---
        self.display_box = ctk.CTkTextbox(self, height=220, width=520, font=("Consolas", 12))
        self.display_box.pack(pady=10)

        # --- FOOTER ---
        self.footer_status = ctk.CTkLabel(self, text="SinemBank © 2026 - Secured by Sinem Systems", text_color="#3498db")
        self.footer_status.pack(side="bottom", pady=15)

    def run_search(self):
        query = self.search_input.get()
        matches = self.bank_engine.search_accounts(query)
        self.display_box.delete("1.0", "end")
        if matches:
            for acc in matches:
                # DİKKAT: acc._owner bir Customer nesnesi olduğu için .name ekledik
                self.display_box.insert("end", f"ID: {acc._account_id} | Owner: {acc._owner.name} | Balance: {acc.balance} TRY\n")
        else:
            self.display_box.insert("end", "Status: No matching account found.")
    
    def process_deposit(self):
        try:
            val = float(self.amount_input.get())
            security_status = self.bank_engine.detect_fraud(val)
            if "ALERT" in security_status:
                messagebox.showwarning("SinemBank Security Alert", security_status)
            else:
                messagebox.showinfo("SinemBank Success", f"Transaction of {val} TRY processed.\n{security_status}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    def display_analytics(self):
        top_list = self.bank_engine.get_top_3_accounts()
        self.display_box.delete("1.0", "end")
        self.display_box.insert("end", "--- SINEMBANK ANALYTICS: TOP 3 ACCOUNTS ---\n\n")
        for i, acc in enumerate(top_list, 1):
            # DİKKAT: acc._owner.name ve acc.balance (property) kullanıldı
            self.display_box.insert("end", f"{i}. {acc._owner.name} -> {acc.balance} TRY\n") 

if __name__ == "__main__":
    app = BankManagementUI()
    app.mainloop()