import os
import requests
from flask import Flask

app = Flask(__name__)

# As tuas credenciais diretas do Telegram
TOKEN = "9121196229:AAHukP46GmYZO1vvJ8cdDYR38G2RQeCm4Ss"
CHAT_ID = "5183459179"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        print("Resposta do Telegram:", response.text)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

@app.route('/')
def home():
    # Sempre que o site for aberto, dispara a mensagem para o Telegram
    send_telegram_message("🚀 *Bot @undergoalslucio_bot ligado e operacional!*")
    return "Bot de Apostas a funcionar e mensagem enviada com sucesso!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
