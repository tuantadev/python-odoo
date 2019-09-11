from odoo import models, fields, api


class Products(models.Model):
    _name = 'products'
    _rec_name = 'product_name'

    def _get_vendor_ids_default(self):
        customers = self.env['customer'].search([('is_vendor', '=', True)])
        return [(6, 0, customers.ids)]

    def _get_description_default(self):
        return 'This is product'

    def _get_default_price(self):
        return 10000

    product_name = fields.Char(string='Name')
    description = fields.Char(string='Description', default=_get_description_default)
    date = fields.Datetime(string='Date',
                           default=lambda self: fields.Datetime.now())
    price = fields.Float(string='Price', default=_get_default_price)
    vendor_ids = fields.Many2many('customer', 'product_customer_rel',
                                  'product_id', 'customer_id', string='Vendors',
                                  default=_get_vendor_ids_default)

    @api.onchange('vendor_ids')
    def onchange_vendor_ids(self):
        print(self.vendor_ids)


