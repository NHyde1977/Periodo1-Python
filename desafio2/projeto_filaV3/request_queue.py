from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/start_processing')
def start_queue():
    number = random.randint(18, 80)
    print(f"[CLIENTE] Enviando idade {number} para fila...")
    response = requests.post(
        'http://localhost:5002/start_processing',
        json={"number": number}
    )
    return f'Pessoa com idade {number} adicionada à fila (via API)', response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5000)
