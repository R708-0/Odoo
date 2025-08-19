from odoo import fields, models

class Compras(models.Model):
    _inherit = "purchase.order"

    def button_confirm2(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            order.order_line._validate_analytic_distribution()
            order._add_supplier_to_product()
            # Deal with double validation process
            if order._approval_allowed():
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
            if order.partner_id not in order.message_partner_ids:
                order.message_subscribe([order.partner_id.id])

            self._get_action_view_picking(self.picking_ids)

            picking.button_validate()

        return True