from odoo import fields, models

class Inventario(models.Model):
    inherit = "product.template"

    available_in_pos = fields.Boolean(default=True)