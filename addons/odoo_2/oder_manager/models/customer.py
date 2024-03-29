from odoo import models, fields, api


class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer Object Model'

    name = fields.Char(string='Name')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')],
                              string='Gender')
