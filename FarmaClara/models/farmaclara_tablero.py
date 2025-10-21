import json

from odoo import _, models, fields

class FarmaClaraTablero(models.Model):
    _inherit = "spreadsheet.dashboard"

    dashboard_group_id = fields.Many2one('spreadsheet.dashboard.group', required=False)
    
    