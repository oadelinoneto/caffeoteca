from flask import Flask

from controllers import site_controller


def adicionar_rotas_site(app: Flask):
    app.add_url_rule('/', view_func=site_controller.index, methods=['GET'])
    app.add_url_rule('/login', view_func=site_controller.login, methods=['GET', 'POST'])
    app.add_url_rule('/cadastro', view_func=site_controller.cadastro, methods=['GET', 'POST'])
    app.add_url_rule('/menu', view_func=site_controller.menu, methods=['GET', 'POST'])
    app.add_url_rule('/perfil_usuario', view_func=site_controller.perfil_usuario, methods=['GET'])
    app.add_url_rule('/carrinho', view_func=site_controller.carrinho, methods=['GET', 'POST'])
