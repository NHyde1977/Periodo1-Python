from flask import Flask
import time
from threading import Thread
from queue_senac import fila_senac

app = Flask(__name__)

@app.route('/pos_processing', methods=['GET'])
def process_queue():
    def atender():
        while not fila_senac.esta_vazia():
            idade = fila_senac.get()
            if idade is not None:
                tipo = "preferencial" if idade >= 60 else "regular"
                print(f'[ATENDIMENTO] Idade {idade} ({tipo})')
                time.sleep(3)
        print("[FILA VAZIA] Nenhuma pessoa aguardando atendimento.")

    Thread(target=atender).start()
    return 'Atendimento iniciado. Veja o console.', 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
