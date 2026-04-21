from flask import render_template, request, redirect, url_for, session

from models.produto_model import listar_produtos, obter_produto_por_id


def index():
    return render_template('index.html')


def login():
    if request.method == 'POST':
        username = request.form['username']
        if username:
            session['usuario'] = {
                'nome': username,
                'email': 'nao informado',
                'username': username,
            }
            return redirect(url_for('menu', username=username))

        return render_template('login.html')

    return render_template('login.html')


def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        username = request.form.get('username', '').strip()
        senha = request.form.get('password', '').strip()
        confirmacao = request.form.get('confirm_password', '').strip()

        if not username or not senha or senha != confirmacao:
            return render_template('cadastro.html')

        session['usuario'] = {
            'nome': nome or username,
            'email': email or 'nao informado',
            'username': username,
        }
        return redirect(url_for('login'))

    return render_template('cadastro.html')


def menu():
    usuario = session.get('usuario', {})
    username = request.args.get('username') or usuario.get('username', 'Guest')
    return render_template('menu.html', username=username, listaProdutos=listar_produtos())


def perfil_usuario():
    usuario = session.get('usuario', {})

    perfil = {
        'nome': usuario.get('nome', 'Visitante'),
        'username': usuario.get('username', 'guest'),
        'email': usuario.get('email', 'nao informado'),
        'membro_desde': 'Abril de 2026',
        'status': 'Conta ativa',
        'plano': 'Padrao'
    }

    return render_template('perfil_usuario.html', perfil=perfil)


def carrinho():
    produto_id = request.args.get('id', type=int)
    carrinho_ids = session.get('carrinho_ids', [])

    if produto_id:
        carrinho_ids.append(produto_id)
        session['carrinho_ids'] = carrinho_ids

    carrinho_itens = []
    for item_id in carrinho_ids:
        produto_encontrado = obter_produto_por_id(item_id)
        if produto_encontrado:
            carrinho_itens.append(produto_encontrado)

    return render_template('carrinho.html', carrinho=carrinho_itens)
