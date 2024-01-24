from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        if 'date_done' in vals:
            if self.purchase_id.is_done:
                self.purchase_id.button_done()
        return super(StockPicking, self).write(vals)
