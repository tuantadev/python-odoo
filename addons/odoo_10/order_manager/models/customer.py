# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Customer(models.Model):
    _name = 'customer'
    _description = 'Customer Object Model'

    # odoo tu dong nhan dien field 'name'. Khuyen cao khong nen viet ten field khac 'name'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code', default='/')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')],
                              string='Gender')
    order_ids = fields.One2many('orders', 'customer_id', string='Orders')
    order_count = fields.Integer(string='Order Count', default=0,
                                 compute='_get_order_count', store=True)
    is_customer = fields.Boolean(default=True, string='Is Customer', help='When tick true is customer')
    is_vendor = fields.Boolean(default=False, string='Is Vendor', help='When tick true is vendor')

    # raise ValidationError('Message Display')
    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('SEQ_CUSTOMER')
        vals['name'] = vals['name'].title()
        if not vals.get('address', ''):
            vals['address'] = 'Ha Noi'
        return super(Customer, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].replace('PYAE0519', '').strip()
        if not vals.get('address', False):
            raise ValidationError('Please Update The Address')
        if not vals.get('gender', False):
            vals['gender'] = 'male'
        return super(Customer, self).write(vals)

    @api.onchange('name', 'phone')
    def onchange_name_phone(self):
        print('name --- ', self.name)
        print('phone ----', self.phone)

    @api.depends('order_ids')
    def _get_order_count(self):
        for customer in self:
            customer.order_count = len(customer.order_ids)

    @api.multi
    def get_list_order(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'orders',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('customer_id', 'in', self.ids)],
        }
