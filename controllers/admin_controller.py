from flask import request, render_template, redirect, url_for

from models.produto_model import adicionar_produto as inserir_produto, listar_produtos


def perfil():
    return render_template('admin.html')


def adicionar_produto():
    if request.method == 'POST':
        id = int(request.form['id'])
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']

        inserir_produto(id, nome, descricao, preco)

        return redirect(url_for('menu'))

    return render_template('coffee_menu.html')


def clients():
    return render_template('clients.html')


def teste():
    return render_template('teste.html', listaProdutos=listar_produtos())
