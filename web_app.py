from flask import Flask, render_template_string, request, redirect
# SavingsAccount'u tip kontrolü (isinstance) için ekledik
from banking_modules import BankSystem, SavingsAccount 

app = Flask(__name__)
bank = BankSystem()

# --- SINEMBANK PREMIUM PINK THEME (GÜNCELLENMİŞ) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SinemBank Web Portal</title>
    <style>
        body { background-color: #1a1a1a; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 40px; }
        h1 { color: #FF69B4; text-align: center; text-shadow: 2px 2px 4px #000; font-size: 32px; }
        .container { max-width: 1000px; margin: auto; border: 2px solid #FF1493; padding: 30px; border-radius: 20px; box-shadow: 0 0 25px #FF1493; }
        .form-section { background: #262626; padding: 25px; border-radius: 12px; border-left: 6px solid #FF1493; margin-bottom: 35px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; background-color: #222; }
        th, td { border: 1px solid #FF69B4; padding: 14px; text-align: left; }
        th { background-color: #FF1493; color: white; text-transform: uppercase; letter-spacing: 1px; }
        tr:hover { background-color: #2d2d2d; }
        input { width: 92%; padding: 12px; margin: 12px 0; border-radius: 6px; border: 1px solid #FF69B4; background: #333; color: white; font-size: 14px; }
        button { background-color: #FF1493; color: white; padding: 14px; border: none; border-radius: 6px; cursor: pointer; width: 100%; font-weight: bold; font-size: 16px; transition: 0.3s; }
        button:hover { background-color: #C71585; transform: scale(1.01); }
        .interest-val { color: #00FF7F; font-weight: bold; } /* Faiz için yeşil vurgu */
        .footer { text-align: center; font-size: 11px; margin-top: 30px; color: #FFB6C1; letter-spacing: 1px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💖 SinemBank Central Web Portal</h1>
        
        <div class="form-section">
            <h3>Customer Subscription Portal</h3>
            <form method="POST" action="/add_customer">
                <input type="text" name="customer_name" placeholder="Enter Full Name (e.g., Sinem Onar)" required>
                <input type="number" step="0.01" name="initial_balance" placeholder="Initial Deposit Amount (TRY)" required>
                <button type="submit">Activate New Account</button>
            </form>
        </div>

        <h3>Real-time Financial Reporting & Interest Analytics</h3>
        <table>
            <tr>
                <th>Account ID</th>
                <th>Owner Name</th>
                <th>Balance (TRY)</th>
                <th>Account Type</th>
                <th>Est. Annual Interest</th> <th>Status</th>
            </tr>
            {% for acc in processed_accounts %}
            <tr>
                <td>{{ acc.id }}</td>
                <td>{{ acc.owner }}</td>
                <td>{{ acc.balance }}</td>
                <td>{{ acc.type }}</td>
                <td class="interest-val">+ {{ acc.interest }} TRY</td>
                <td style="color: #FFB6C1; font-weight: bold;">Operational</td>
            </tr>
            {% endfor %}
        </table>
        <div class="footer">
            Stage 3 Requirement Fulfilled: Interest Computation & Web Reporting System | Secured by SinemBank © 2026
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Stage 3: Polymorphism ve Faiz Tahmini Mantığı
    processed_accounts = []
    for acc in bank.accounts:
        interest = 0
        if isinstance(acc, SavingsAccount):
            # banking_modules içindeki bileşik faiz algoritmasını çağırıyoruz
            interest = acc.calculate_projected_interest(years=1)
        
        processed_accounts.append({
            'id': acc._account_id,
            'owner': acc._owner.name,
            'balance': acc.balance,
            'type': acc.__class__.__name__,
            'interest': round(interest, 2)
        })
    
    return render_template_string(HTML_TEMPLATE, processed_accounts=processed_accounts)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form.get('customer_name')
    try:
        balance = float(request.form.get('initial_balance'))
        bank.add_account(name, balance)
    except Exception as e:
        print(f"Error: {e}")
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)