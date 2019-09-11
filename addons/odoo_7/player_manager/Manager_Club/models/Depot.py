from odoo import api, models, fields

class Depot(models.Model):
    _name = 'depot'
    _description = 'Lo dao tao'

    name = fields.Char(string='Ten lo dao tao', required='1')
    address = fields.Char(string='Dia chi', required='1')
    player_ids = fields.One2many(comodel_name='player', inverse_name='depot_id', string='Cac cau thu')

    @api.onchange('name')
    def onchange_name(self):
        if self.name:
            self.name = self.name.titile()
