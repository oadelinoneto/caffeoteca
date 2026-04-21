from flask import Flask
from routes import site_router, admin_router


app = Flask(__name__)
app.secret_key = 'coffeoteca-secret-key'

site_router.adicionar_rotas_site(app)
admin_router.adicionar_rotas_admin(app)