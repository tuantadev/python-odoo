from odoo import models, fields, api

class CauLacBo(models.Model):
    _name = 'club'
    _description = 'DeMo CLub Test'

    name = fields.Char(string = "Ten", required = 1)
    founder_year = fields.Datetime(string = " Nam thanh lap", required = 1)
    address = fields.Char(string = "Dia chi", default = 'Ha Noi')
    player_ids = fields.One2many('player', 'club_id', string="Club Id")
    num_player = fields.Integer(string="So luong cau thu", compute = '_get_num_player', default = '0')
    coach = fields.Char(string = " Huan luyen vien ")
    club_status = fields.Selection(string = "Trang thai cua cau lac bo", selection=[('act', 'Hoat dong'), ('disso', 'Giai the')]
                                   ,default = 'act')

    @api.onchange('name')
    def onchange_name(self):
        if self.name:
            self.name = self.name.title()

    @api.multi
    @api.depends('player_ids')
    def _get_num_player(self):
        for clb in self :
            clb.num_player = len(clb.player_ids)

    @api.multi
    def validate_club(self):
        self.club_status = 'disso'
        self.player_ids = False