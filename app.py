from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_loan(loan_amount, interest_rate, years):
    monthly_rate = (interest_rate / 100) / 12
    num_payments = years * 12
    if monthly_rate == 0:
        monthly_payment = loan_amount / num_payments
    else:
        monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    return round(monthly_payment, 2)

@app.route('/loan', methods=['GET'])
def loan():
    try:
        loan_amount = float(request.args.get('amount', 0))
        interest_rate = float(request.args.get('rate', 0))
        years = int(request.args.get('years', 0))
        monthly_payment = calculate_loan(loan_amount, interest_rate, years)
        return jsonify({"monthly_payments": monthly_payment})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
