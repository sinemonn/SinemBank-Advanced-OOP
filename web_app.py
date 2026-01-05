from flask import Flask, render_template_string, request, redirect
from banking_modules import BankSystem

app = Flask(__name__)
bank = BankSystem() # Mevcut backend motorunu bağladık

# --- PEMBE WEB TASARIMI (CSS & HTML) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SinemBank Web Portal</title>
    <style>
        body { background-color: #1a1a1a; color: white; font-family: 'Segoe UI', sans-serif; padding: 40px; }
        h1 { color: #FF69B4; text-align: center; }
        .container { max-width: 850px; margin: auto; border: 2px solid #FF1493; padding: 25px; border-radius: 20px; box-shadow: 0 0 15px #FF1493; }
        table { width: 100%; border-collapse: collapse; margin-top: 25px; }
        th, td { border: 1px solid #FF69B4; padding: 15px; text-align: left; }
        th { background-color: #FF1493; color: white; }
        tr:nth-child(even) { background-color: #262626; }
        .form-section { background: #262626; padding: 20px; border-radius: 10px; border-left: 5px solid #FF1493; }
        input { width: 95%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #FF69B4; background: #333; color: white; }
        button { background-color: #FF1493; color: white; padding: 12px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-weight: bold; }
        button:hover { background-color: #C71585; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💖 SinemBank Central Web Portal</h1>
        
        <div class="form-section">
            <h3>New Customer Subscription</h3>
            <form method="POST" action="/add_customer">
                <input type="text" name="customer_name" placeholder="Full Name (e.g., Sinem Onar)" required>
                <input type="number" name="initial_balance" placeholder="Initial Deposit Amount (TRY)" required>
                <button type="submit">Complete Subscription</button>
            </form>
        </div>

        <hr style="border: 1px solid #FF69B4; margin: 30px 0;">

        <h3>Banka Genel Durum Raporu (Reporting)</h3>
        <table>
            <tr>
                <th>Account ID</th>
                <th>Owner Name</th>
                <th>Current Balance</th>
                <th>Status</th>
            </tr>
            {% for acc in accounts %}
            <tr>
                <td>{{ acc._account_id }}</td>
                <td>{{ acc._owner.name }}</td>
                <td>{{ acc.balance }} TRY</td>
                <td style="color: #FFB6C1;">Active</td>
            </tr>
            {% endfor %}
        </table>
        <p style="text-align: center; font-size: 11px; margin-top: 30px; color: #FFB6C1;">
            Stage 3 Requirement: Web-based Reporting System Enabled | Secured by SinemBank
        </p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Mevcut hesapları tarayıcıda listele (Reporting)
    return render_template_string(HTML_TEMPLATE, accounts=bank.accounts)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    # Web portalı üzerinden yeni müşteri kaydı (Data Entry)
    name = request.form.get('customer_name')
    balance = float(request.form.get('initial_balance'))
    bank.create_account(name, balance) # Backend metodunu tetikle
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)