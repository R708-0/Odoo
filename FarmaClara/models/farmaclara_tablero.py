import json

from odoo import _, models, fields

class FarmaClaraTablero(models.Model):
    _inherit = "spreadsheet.dashboard"

    dashboard_group_id = fields.Many2one('spreadsheet.dashboard.group', required=False)
    
class FarmaClaraPurchaseReport(models.Model):
    _inherit = "purchase.report"

    # price_total = fields.Monetary('Value', compute='_compute_value', groups='stock.group_stock_manager')

    # value = fields.Monetary('Value', compute='_compute_value', groups='stock.group_stock_manager')
    # currency_id = fields.Many2one('res.currency', compute='_compute_value', groups='stock.group_stock_manager')