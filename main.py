from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = '8910036824:AAE6KRF_-6bIOonGTphWEoTj0XKvTqUFGxc'
CHAT_ID = '7837875628'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        signal = data.get("signal", "N/A")
        pair = data.get("pair", "N/A")
        price = data.get("price", "N/A")
        
        message = (
            f"🚨 **QUOTEX SIGNAL ALERT** 🚨\n\n"
            f"📌 Pair: {pair}\n"
            f"📈 Signal: {signal}\n"
            f"💰 Price: {price}\n"
            f"⏰ Expiry: 1 Min"
        )
        
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload)
        
        return "Signal Received", 200
    return "No Data", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
