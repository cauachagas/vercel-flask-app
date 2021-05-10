from flask import Flask, jsonify, json
from os.path import join

# Criando um dado de teste
livros = [
  {
    "id": 0,
    "titulo": "1984",
    "autor": "George Orwell",
    "ano_publicao": "1949"
  },
  {
    "id": 1,
    "titulo": "Laranja Mecânica",
    "autor": "Anthony Burgess",
    "ano_publicao": "1962"
  },
  {
    "id": 2,
    "titulo": "Admirável Mundo Novo",
    "autor": "Aldous Huxley",
    "ano_publicao": "1932"  
  }
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Página da rota Home</h1>'

@app.route('/sobre', methods=['GET'])
def about():
    return '<h1>Pagina da rota Sobre</h1>'

@app.route('/portfolio', methods=['GET'])
def portfolio():
    return '<h1>Página da rota Portfolio</h1>'

@app.route('/contato', methods=['GET'])
def contact():
    return '<h1>Página da rota Contato</h1>'

# Puxando dados de data.json e serializando
@app.route("/api/cervejas", methods=['GET'])
def api():
    with open('data/data.json', 'r') as file:
        data = json.load(file)
        return jsonify(data)

# Serializando nosso dado de teste
@app.route('/api/livros', methods=['GET'])
def api_all():
    return jsonify(livros)

if __name__ == '__main__':
    app.run()