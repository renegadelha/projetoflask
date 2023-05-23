from flask import Flask, render_template, request,session
import random
app = Flask(__name__)
app.secret_key = '1234fdsa'

usuarios = {'rene':['123', {123:['a', 44, 'bom'], 777:['b', 12, 'ruim']}]}



def validar_login(login, senha):
    for chave in usuarios:
        if(login == chave):
            if(usuarios[login][0] == senha):
                return True
    return False

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def fazer_login():
    #request recebe uma requisição via formulário e pega o campo especificado
    login = str(request.form.get('usuario'))
    senha = str(request.form.get('senha'))
    print(login + " - " + senha)

    if (len(login) == 0 or len(senha) == 0 ):
        return render_template('index.html')
    else:
        if validar_login(login, senha):
            session['username'] = login

            return render_template('menuUser.html', user=login)
        else:
            return render_template('index.html', mensagem='Usuário ou senha inválida')

@app.route("/pag_cadastro_produto")
def pag_cadastro_prod():
    return render_template('cadastrarproduto.html')

@app.route("/cadastrar_produto", methods=['POST'])
def cadastrar_prod():
    nome = str(request.form.get('nomeproduto'))
    preco = str(request.form.get('preco'))
    descricao = str(request.form.get('descricao'))

    dic_prod = usuarios[session['username']][1]

    while True:
        code_prod = random.randint(1,9999)
        if code_prod not in dic_prod:
            break
    dic_prod[code_prod] = [nome, preco, descricao]

    print(usuarios)


    return render_template('menuUser.html', user=session['username'])

@app.route("/listar_produtos")
def listar_produtos():
    return render_template('listarprodutos.html', user=session['username'], produtos=usuarios[session['username']][1])


@app.route("/voltar_menu")
def retornar_menu():
    return render_template('menuUser.html', user=session['username'])

if __name__ == "__main__":
    app.run(debug=True)