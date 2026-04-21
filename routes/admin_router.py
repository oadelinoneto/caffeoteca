from flask import Flask

from controllers import admin_controller


def adicionar_rotas_admin(app: Flask):
    app.add_url_rule('/perfil', view_func=admin_controller.perfil, methods=['GET'])
    app.add_url_rule('/adicionar_produto', view_func=admin_controller.adicionar_produto, methods=['GET', 'POST'])
    app.add_url_rule('/clientes', view_func=admin_controller.clients, methods=['GET'])
    app.add_url_rule('/teste', view_func=admin_controller.teste, methods=['GET'])
