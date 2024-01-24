from odoo import models, fields, api, _
import logging
from num2words import num2words

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    notes = fields.Html('Terms and Conditions', compute="_compute_terms_and_conditions", store=True, readonly=False)

    @api.depends('partner_id')
    def _compute_terms_and_conditions(self):
        for order in self:
            order.notes = order.partner_id.terms_conditions if order.partner_id else ''

  
    def print_quotation(self):
        action = self.env.ref('purchase_custom.action_new_purchase_order_report').read()[0]
        return action

    @api.model
    def _get_report_values(self, docids, data=None):
        purchase_orders = self.env['purchase.order'].browse(docids)

        report_data = {
            'doc_ids': docids,
            'doc_model': 'purchase.order',
            'docs': purchase_orders,
            'user_id': purchase_orders.user_id,
            'partner_ref': purchase_orders.partner_ref,
            'state': purchase_orders.state,
            'date_approve': purchase_orders.date_approve,
            'date_order': purchase_orders.date_order,
            'page_number': self.env.context.get('page_number', 1),  # Default to page 1

            'qty_to_text': self.qty_to_text,
        }

        return report_data

    @api.model
    def qty_to_text(self, quantity):
        text = num2words(quantity, to='currency', lang='en')
        return text

    def print_po(self):
        self.write({'state': "sent"})
        return self.env.ref('po_so_terms_conditions.action_new_purchase_order_report').report_action(self)


