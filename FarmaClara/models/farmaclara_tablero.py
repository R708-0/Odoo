import json

from odoo import _, models, fields

class FarmaClaraTablero(models.Model):
    _inherit = "spreadsheet.dashboard"

    dashboard_group_id = fields.Many2one('spreadsheet.dashboard.group', required=False)
    
    def get_readonly_dashboard(self):
        self.ensure_one()

        if self.id == self.env.ref("spreadsheet_dashboard_account.dashboard_invoicing").id:
            return None
        
        snapshot = json.loads(self.spreadsheet_data)
        user_locale = self.env['res.lang']._get_user_spreadsheet_locale()
        snapshot.setdefault('settings', {})['locale'] = user_locale
        default_currency = self.env['res.currency'].get_company_currency_for_spreadsheet()
        return {
            'snapshot': snapshot,
            'revisions': [],
            'default_currency': default_currency,
        }