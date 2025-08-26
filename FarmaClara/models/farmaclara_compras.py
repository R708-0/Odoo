from odoo import fields, models

class Compras(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        # Llamamos al flujo original de confirmación
        res = super().button_confirm()

        for order in self:
            # 1. Confirmar el picking en estado borrador (recepción)
            pickings = order.picking_ids.filtered(lambda p: p.state not in ['done', 'cancel'])
            for picking in pickings:
                if picking.state == 'draft':
                    picking.action_confirm()
                # 2. Si no se registró cantidad realizada, copiar planificada
                for move in picking.move_ids:
                    if move.quantity == 0 and move.product_uom_qty > 0:
                        move.quantity = move.product_uom_qty
                # 3. Validar directamente la recepción
                picking.button_validate()
            
        # redirigir a la vista tree
        action = self.env.ref('FarmaClara.farmaclara_compras_action_view').read()[0]
        return action

        # 4. Crear y validar factura de proveedor (versión Odoo 17)
        # if not order.invoice_ids:
        #     invoice_vals = order._prepare_invoice()
        #     invoice = self.env['account.move'].create(invoice_vals)
        #     invoice.action_post()
