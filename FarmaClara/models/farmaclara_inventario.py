from odoo import fields, models

class Inventario(models.Model):
    _inherit = "product.template"

    fecha_vencimiento = fields.Date("Fecha de Vencimiento")
    presentacion = fields.Text("Presentacion")