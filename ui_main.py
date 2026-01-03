import customtkinter as ctk
from tkinter import messagebox
from banking_modules import BankSystem, InsufficientFundsError

# --- APP THEME CONFIGURATION ---
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

class BankManagementUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("SinemBank - Advanced Management System")
        self.geometry("700x750")
        self.bank_engine = BankSystem() 

        # --- HEADER (PEMBE) ---
        self.header = ctk.CTkLabel(self, text="SinemBank Control Center", 
                                   text_color="#FF69B4", # Canlı Pembe
                                   font=("Helvetica", 32, "bold"))
        self.header.pack(pady=30)

        # --- SEARCH SECTION (STAGE 2) ---
        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        # HATA BURADAYDI: "px" yerine "padx" yapıldı
        self.search_frame.pack(pady=10, fill="x", padx=40) 

        self.search_input = ctk.CTkEntry(self.search_frame, 
                                         placeholder_text="Filter accounts by owner name...", 
                                         width=350,
                                         border_color="#FF69B4")
        self.search_input.pack(side="left", padx=10)

        self.search_btn = ctk.CTkButton(self.search_frame, text="Search", 
                                        fg_color="#FF1493", 
                                        hover_color="#C71585",
                                        command=self.run_search)
        self.search_btn.pack(side="left")

        # --- TRANSACTION SECTION (STAGE 2 & 3) ---
        self.trans_frame = ctk.CTkFrame(self, border_width=2, border_color="#FFB6C1")
        self.trans_frame.pack(pady=20, padx=40, fill="x")

        self.trans_label = ctk.CTkLabel(self.trans_frame, text="Secure Transaction Protocol", 
                                        font=("Helvetica", 14, "italic"), text_color="#FFB6C1")
        self.trans_label.pack(pady=5)

        self.amount_input = ctk.CTkEntry(self.trans_frame, 
                                         placeholder_text="Enter Amount (Fraud Detection Limit: 20k)", 
                                         width=400, border_color="#FF69B4")
        self.amount_input.pack(pady=15)

        self.deposit_btn = ctk.CTkButton(self.trans_frame, text="Execute Secure Transaction", 
                                         fg_color="#FF1493", 
                                         hover_color="#C71585",
                                         command=self.process_transaction)
        self.deposit_btn.pack(pady=10)

        # --- ANALYTICS SECTION (STAGE 3) ---
        self.analytics_btn = ctk.CTkButton(self, text="View SinemBank Analytics (Top 3)", 
                                           fg_color="#FF69B4", 
                                           hover_color="#FF1493",
                                           height=40,
                                           command=self.display_analytics)
        self.analytics_btn.pack(pady=20)

        # --- DISPLAY BOX ---
        self.display_box = ctk.CTkTextbox(self, width=600, height=200, 
                                          border_width=2, border_color="#FF69B4",
                                          font=("Courier New", 13))
        self.display_box.pack(pady=10)

        # --- FOOTER ---
        self.footer_status = ctk.CTkLabel(self, text="SinemBank © 2026 - Secured by Sinem Systems", 
                                          text_color="#FFB6C1", 
                                          font=("Helvetica", 11))
        self.footer_status.pack(side="bottom", pady=20)

    # --- LOGIC METHODS ---
    def run_search(self):
        query = self.search_input.get()
        matches = self.bank_engine.search_accounts(query)
        self.display_box.delete("1.0", "end")
        if matches:
            for acc in matches:
                self.display_box.insert("end", f"ID: {acc._account_id} | Owner: {acc._owner.name} | Balance: {acc.balance} TRY\n")
        else:
            self.display_box.insert("end", "Status: No matching account found.")

    def process_transaction(self):
        try:
            val = float(self.amount_input.get())
            fraud_status = self.bank_engine.detect_fraud(val)
            if fraud_status == "ALERT":
                messagebox.showwarning("Security Protocol Alert", f"Suspicious activity detected! Amount {val} exceeds safety limits.")
            else:
                messagebox.showinfo("Success", f"Transaction of {val} TRY processed securely.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    def display_analytics(self):
        top_list = self.bank_engine.get_top_3_accounts()
        self.display_box.delete("1.0", "end")
        self.display_box.insert("end", "--- SINEMBANK ANALYTICS: TOP 3 ACCOUNTS ---\n\n")
        for i, acc in enumerate(top_list, 1):
            self.display_box.insert("end", f"{i}. {acc._owner.name} -> {acc.balance} TRY\n")

if __name__ == "__main__":
    app = BankManagementUI()
    app.mainloop()