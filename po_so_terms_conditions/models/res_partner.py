from odoo import models, fields, api, _


class Contact(models.Model):
    _inherit = 'res.partner'

    supplier_seq = fields.Char("Vendor Sequence", default='', copy=False)
    is_vendor = fields.Boolean(string="Is Vendor", compute="_compute_is_vendor",
                               inverse='_write_supplier_rank_and_sequence', store=True)
    terms_conditions = fields.Html("Terms and Conditions")
    @api.depends('supplier_rank')
    def _compute_is_vendor(self):
        for partner in self:
            partner.is_vendor = partner.supplier_rank > 0

    def _write_supplier_rank_and_sequence(self):
        for partner in self:
            if partner.is_vendor:
                partner.supplier_rank = 1 if partner.supplier_rank <= 0 else partner.supplier_rank
            else:
                partner.supplier_rank = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if ('supplier_rank' in vals and vals['supplier_rank'] > 0) or ('is_vendor' in vals and vals['is_vendor']):
                vals["supplier_seq"] = self.env['ir.sequence'].next_by_code('vendor.sequence') or _('New Vendor')
        return super(Contact, self).create(vals_list)

    def write(self, vals):
        supplier_seq = vals['supplier_seq'] if 'supplier_seq' in vals else self.supplier_seq
        if 'is_vendor' in vals and vals['is_vendor'] and supplier_seq == '':
            vals["supplier_seq"] = self.env['ir.sequence'].next_by_code('vendor.sequence') or _('New Vendor')
        return super(Contact, self).write(vals)

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default['is_vendor'] = self.is_vendor
        return super().copy(default)
