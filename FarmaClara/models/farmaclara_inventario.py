from odoo import fields, models

class Inventario(models.Model):
    _inherit = "product.template"

    fecha_vencimiento = fields.Date("Fecha de Vencimiento")
    presentacion = fields.Text("Accion terapeutica")
    available_in_pos = fields.Boolean(default=True)