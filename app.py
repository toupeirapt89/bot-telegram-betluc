import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# Configurações do Telegram com os teus dados reais
TOKEN = os.environ.get("TELEGRAM_TOKEN", "9121196229:AAHukP46GmYZO1vvJ8cdDYR38G2RQeCm4Ss")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "5183459179")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        print("Telegram response:", response.text)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

@app.route('/')
def home():
    # Envia a mensagem de teste assim que alguém aceder ao site do Render
    send_telegram_message("🚀 *Bot @undergoalslucio_bot ligado e operacional!*")
    return "Bot de Apostas a funcionar e mensagem enviada para o Telegram!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
