from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    nome = "Baptysta"
    return render_template('contato.html', usuario=None, nome=nome, title="Home")

@app.route("/contato")
def home():
    return render_template('contato.html')

@app.route('/usuario')
def usuario():
    usuario = {'nome': 'Alba', 'sobrenome': 'Lopes'}
    return render_template('index.html', title='Página Inicial', usuario=usuario)

@app.route('/dados', defaults={"nome":"usuário comum"}) 
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}'

@app.route('/semestre/<int:x>')
def semestre(x):
    return 'Estamos no semestre ' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return 'Você pagou: '+ str(valor)

@app.route('/soma', defaults={"n1": "0", "n2": "0"})
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    resultado = n1 + n2
    return render_template('somar.html', n1=n1, n2=n2, resultado=resultado)

@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        return "[cadeado fechado] Acesso bloqueado"
    else:
        return "[cadeado aberto] Acesso liberado"

if __name__ == "__main__":
    app.run(debug=True)

