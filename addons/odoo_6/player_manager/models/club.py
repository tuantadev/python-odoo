# -*- coding: utf-8 -*-
from odoo import models, fields, api
# from odoo.exceptions import ValidationError


class Club(models.Model):
    _name = 'club'
    _description = 'Club'
    # _rec_name = 'name'

    # odoo tu dong nhan dien field 'name'. Khuyen cao khong nen viet ten field khac 'name'
    name = fields.Char(string='Tên CLB', required = 1)
    club = fields.Integer('Năm thành lập')
    address = fields.Text(string='Địa chỉ', default='Ha Noi')
    state = fields.Selection(selection=[('dhd', 'Đang hoạt động'), ('gt', 'Giải thể')],
                              string='Trạng thái', default='dhd', store=True)

    hlv = fields.Char('Huấn luyện viên chính')
    player_ids = fields.One2many(comodel_name="player", inverse_name="club_id", string="Cầu thủ")
    nop = fields.Integer(string=('SL cầu thủ'), default=0, compute='_get_nop')

    @api.multi
    @api.depends('player_ids')
    def _get_nop(self):
        for clb in self:
            clb.nop = len(clb.player_ids)

    @api.multi
    def giai_the(self):
        for clb in self:
            clb.state = 'gt'
            clb.player_ids = False
