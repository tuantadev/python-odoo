# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Customer(models.Model):
    _inherit = 'customer'

    total_purchased_amount = fields.Float(compute='_get_total_purchased_amt',
                                          string='Total Purchased Amount', store=True)

    @api.multi
    @api.depends('order_ids')
    def _get_total_purchased_amt(self):
        total = 0
        for customer in self:
            for order in customer.order_ids:
                total += order.total_amount
            customer.total_purchased_amount = total

    @api.model
    def create(self, vals):
        if vals.get('address', ''):
            vals['address'] = vals['address'].title()
        return super(Customer, self).create(vals)
