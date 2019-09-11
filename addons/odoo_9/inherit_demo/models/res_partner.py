from odoo import models, fields, api


class ResPartner(models.Model):
    # _name = 'res.partner'
    _inherit = 'res.partner'

    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')],
        string='Gender')
    member_code = fields.Char(string='Member Code')
    fax = fields.Char(string='Fax')
    # lang = fields.Selection(string='Ngon ngu')
