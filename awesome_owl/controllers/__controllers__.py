# Librerias para crear rutas http
from odoo import http
from odoo.http import request, route

# Crear una clase que herede los controladores web
class OwlPlayground(http.Controller):
    # Registra l metodo awesome_owl como una ruta en el servidor de odoo
    @http.route(['/awesome_owl'], type="http", auth ="public")