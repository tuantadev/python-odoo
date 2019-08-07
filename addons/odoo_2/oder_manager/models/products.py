from odoo import models,fields,api


class Products(models.Model):
    _name = 'products'
    _description = 'Product '
    # _rec_name = product_name

    name = fields.Char(string ='name')
    description = fields.Char(string ='description')
    date = fields.Datetime(string ='date' ,default=lambda self: fields.Datetime.now())
    price = fields.Float(string ='price')

