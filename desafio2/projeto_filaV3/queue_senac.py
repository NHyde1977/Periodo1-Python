from flask import Flask, jsonify
import random
import time
from threading import Thread

# ─── Estrutura da Fila ───
class Nodo:
    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.proximo = proximo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def put(self, valor):
        novo = Nodo(valor)
        if self.ultimo:
            self.ultimo.proximo = novo
        self.ultimo = novo
        if not self.primeiro:
            self.primeiro = novo

    def get(self):
        if not self.primeiro:
            return None
        valor = self.primeiro.dado
        self.primeiro = self.primeiro.proximo
        if not self.primeiro:
            self.ultimo = None
        return valor

    def esta_vazia(self):
        return self.primeiro is None

# ─── App Flask ───
app = Flask(__name__)
fila = Fila()

@app.route('/start_processing', methods=['GET'])
def start_queue_senac():
    number = random.randint(18, 80)
    print(f"Pessoa com idade {number} adicionada na fila", flush=True)
    fila.put(number)
    return jsonify({"message": f"Pessoa com idade {number} adicionada na fila"}), 200

@app.route('/pos_processing', methods=['GET'])
def process_queue():
    atendimentos = []
    def atender():
        while not fila.esta_vazia():
            valor = fila.get()
            tipo = "caixa dedicado a idosos" if valor >= 60 else "caixa regular"
            print(f" Atendimento idade {valor} ({tipo})", flush=True)
            atendimentos.append({"valor": valor, "tipo": tipo})
            time.sleep(3)
        if not atendimentos:
            print("[FILA VAZIA] Nenhuma pessoa aguardando.", flush=True)
    Thread(target=atender).start()
    return jsonify(atendimentos or {"message": "Fila vazia"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
