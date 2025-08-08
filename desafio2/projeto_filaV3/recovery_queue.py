from flask import Flask
import requests

app = Flask(__name__)

@app.route('/pos_processing')
def start_attending():
    response = requests.get('http://localhost:5002/pos_processing')
    if response.status_code == 200:
        return f"<pre>{response.json()}</pre>"
    return "Erro ao processar fila", response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5001)
