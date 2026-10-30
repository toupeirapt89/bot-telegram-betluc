import os
import requests
from flask import Flask

app = Flask(__name__)

# Token correto e atualizado do Telegram
TOKEN = "9121196229:AAHacVcHrwJoG4e8kDTigzzPv180iPQ17Zk"
CHAT_ID = "5183459179"

@app.route('/')
def home():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "🚀 Bot @undergoalslucio_bot ligado e operacional com sucesso!"
    }
    
    try:
        response = requests.post(url, json=payload)
        resposta_texto = response.text
        print("RESPOSTA DO TELEGRAM:", resposta_texto)
        return f"Tentativa de envio feita! Resposta do Telegram: {resposta_texto}"
    except Exception as e:
        print("ERRO:", str(e))
        return f"Erro ao enviar: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
