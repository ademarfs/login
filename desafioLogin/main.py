from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'root'
    
@app.route('/') # Rota inicial
def home(): # Função para renderizar o html inicial
    return render_template('login.html') # render_template para renderizar

@app.route('/login', methods=['POST']) # Rota para pagina de login
def login(): # Função para tratar o Login
    usuario = request.form.get('username') # Coleta o username digitado no front-end. Mesmo nome setado no Html
    password = request.form.get('password') # Coleta o password digitado no front-end. Mesmo nome setado no Html
    with open('data_users.json', 'r') as json_file: # Abre o arquivo json em modo READ 
        list = json.load(json_file) # Comando para ler o arquivo, armazenado na variavel "list"
        cont = 0 # Var para o contador de tentativas de acesso
        for i in list:
            cont += 1
            if usuario == i['username'] and password == i['password']: # Condição se os ddos do usuário estiverem de acordo com no Banco de Dados, fornece o acesso.
                return render_template('acesso.html', nameUser = i['username']) # Fornece o acesso para um outro html. Var nameUser p/ chamar no html.
            if cont >= len(list): # Se o contador for for maior ou igual ao tamanho da lista, usário inválido, pois a tentativa já é igual ou ultrapassa a quantidade de Dados no Banco.
                flash('Usuário inválido') # Mensagem para o usuário após tentativa errada. Inserido no html.
                return redirect('/') # Rediceriona para home.
                
if __name__ == '__main__':
    app.run(debug=True)