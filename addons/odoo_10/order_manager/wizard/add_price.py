from odoo import models, fields, api


class ResPartnerComment(models.TransientModel):
    _name = 'add.price'

    price = fields.Float(string='Add Price')

    @api.multi
    def add_price(self):
        if self.price:
            partner_id = self.env.context.get('active_id', False)
            partner = self.env['products'].browse(partner_id)
            partner.price = self.price
