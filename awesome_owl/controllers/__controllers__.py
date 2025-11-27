# Librerias para crear rutas http
from odoo import http
from odoo.http import request, route

# Crear una clase que hereda los controladores web
class OwlPlayground(http.Controller):

    # Registra el metodo awesome_owl como una ruta en el servidor de odoo
    @http.route(['/awesome_owl'], type="http", auth ="public")
    def show_playground(self):

        # Renderiza el template playground
        return request.render('awesome_owl.palyground')
