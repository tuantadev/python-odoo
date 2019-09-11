# -*- coding: utf-8 -*-
from odoo import models, fields, api


# from odoo.exceptions import ValidationError


class Player(models.Model):
    _name = 'player'
    _description = 'Player'
    # _rec_name = 'name'

    # odoo tu dong nhan dien field 'name'. Khuyen cao khong nen viet ten field khac 'name'
    name = fields.Char(string='Tên cầu thủ', required = 1)
    address = fields.Text(string='Địa chỉ', required = 1)
    phone = fields.Char(string='Phone')

    state = fields.Selection(selection=[('tudo', 'Tự do'), ('dtbc', 'Đang Thuộc Biên Chế')],
                              string='Trạng thái' , default='tudo', compute='_get_state', store=True)
    gender = fields.Selection(selection=[('male', 'Nam'), ('female', 'Nữ')],
                              string='Giới tính')

    club_id = fields.Many2one('club', 'CLB')

    @api.depends('club_id')
    @api.multi
    def _get_state(self):
        for player in self:
            if player.club_id:
                player.state = 'dtbc'
            else:
                player.state = 'tudo'

    @api.onchange('name')
    def onchange_name(self):
        if self.name:
            self.name = self.name.title()
