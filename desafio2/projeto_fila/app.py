from flask import Flask, render_template
import random
import time
from threading import Thread
from queue_senac import Fila

app = Flask(__name__)
fila_senac = Fila()

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/start_processing', methods=['GET'])
def start_queue():
    number = random.randint(18, 80)
    fila_senac.put(number)
    print(f'[INSERIDO] Pessoa com idade {number} adicionada à fila.')
    return f'Pessoa com idade {number} adicionada à fila.', 200

@app.route('/pos_processing', methods=['GET'])
def process_queue():
    def atender():
        while not fila_senac.esta_vazia():
            idade = fila_senac.get()
            if idade is not None:
                tipo = "preferencial" if idade >= 60 else "regular"
                print(f'[ATENDIMENTO] Idade {idade} ({tipo}) → {idade * 1000}')
                time.sleep(3)  # simula tempo de atendimento
        print("[FILA VAZIA] Nenhuma pessoa aguardando atendimento.")

    Thread(target=atender).start()
    return 'Atendimento iniciado (veja o console).', 200

if __name__ == '__main__':
    app.run(debug=True)
