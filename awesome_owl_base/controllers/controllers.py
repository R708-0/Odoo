# Librerias para crear rutas http
from odoo import http
from odoo.http import request, route

# Crear una clase que herede los controladores web
class OwlPlaygroundBase(http.Controller):

    # Registrar la ruta 'awesome_owl_base' en el servidor de odoo
    @route(["/awesome_owl_base"], type="http", auth="public")
    def playground_base(self):

        # renderizar el template playground
        return request.render("awesome_owl_base.playground_base")