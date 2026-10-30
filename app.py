import os
import time
import threading
import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

# Configurações do Telegram (podes alterar se necessário)
TOKEN = os.environ.get("TELEGRAM_TOKEN", "7707328905:AAH47vYvjY0T7ZfN4G0ZfN4G0ZfN4G0ZfN4")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "123456789")

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

def check_matches():
    while True:
        try:
            # Lógica de verificação de jogos e alertas de Under
            print("A verificar jogos...")
            # Exemplo de alerta: send_telegram_message("⚽ Alerta Under 1.5 HT detectado!")
        except Exception as e:
            print("Erro no ciclo de verificação:", e)
        
        # Intervalo de 60 segundos entre verificações
        time.sleep(60)

@app.route('/')
def home():
    return "Bot de Apostas a funcionar na nuvem!"

if __name__ == "__main__":
    # Inicia a thread de monitorização em segundo plano
    t = threading.Thread(target=check_matches)
    t.daemon = True
    t.start()
    
    # Inicia o servidor Flask para o Render manter o serviço ativo
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
