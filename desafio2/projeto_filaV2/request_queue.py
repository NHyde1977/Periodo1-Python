from flask import Flask, render_template
import random
from queue_senac import fila_senac

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/start_processing', methods=['GET'])
def start_queue():
    number = random.randint(18, 80)
    fila_senac.put(number)
    print(f'[INSERIDO] Pessoa com idade {number} adicionada à fila.')
    return f'Pessoa com idade {number} adicionada à fila.', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
