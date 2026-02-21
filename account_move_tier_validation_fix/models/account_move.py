from odoo import models

class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_under_validation_exceptions(self):
        res = super(AccountMove, self)._get_under_validation_exceptions()
        if 'checked' not in res:
            res.append('checked')
        return res
