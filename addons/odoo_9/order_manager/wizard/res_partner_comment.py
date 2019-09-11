from odoo import models, fields, api


class ResPartnerComment(models.TransientModel):
    _name = 'res.partner.comment'

    comment = fields.Text(string='Text')

    @api.multi
    def add_comment(self):
        if self.comment:
            partner_id = self.env.context.get('active_id', False)
            partner = self.env['res.partner'].browse(partner_id)
            partner.comment = self.comment
