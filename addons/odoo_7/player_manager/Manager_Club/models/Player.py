from odoo import models, fields, api

class CauLacBo(models.Model):
    _name = 'player'

    name = fields.Char(string = "Ten", required = 1)
    age = fields.Integer(string = " Tuoi", required = 1)
    address = fields.Char(string="Dia chi", default = 'Ha Noi')
    club_id = fields.Many2one('club', string = "Club Ids")
    phone = fields.Char(string="So dien thoai")
    depot_id = fields.Many2one(comodel_name='depot', string="Noi huan luyen")
    salary = fields.Integer(string="Luong", compute='_get_salary', readonly=1 )
    state_player = fields.Selection(string = 'Trang thai cua cau thu',selection=[('free', 'Free'), ('n_free', 'None Free')]
                                   ,default = 'free', compute='_get_status')
    p_income_tax = fields.Float(string ='Thue thu nhap ca nhan',compute = '_get_tax', default = 0)

    @api.depends('salary')
    @api.multi
    def _get_tax(self):
        for player in self:
            if player.salary > 10000000 :
                player.p_income_tax = player.salary / 10
            else:
                player.p_income_tax = 0

    @api.onchange('name')  # bat su kien khi thay doi gia tri 1 or nhieu field nao do, chi thay doi tren giao dien
    # moi khi thay doi bat ky o dau deu chay onchange
    def onchange_name(self):
        if self.name:
            self.name = self.name.title()

    @api.multi
    @api.depends('depot_id') # chi sdung trong ham compute, chi khi ng dung thao tac thay doi thi moi chay depends
    def _get_salary(self):
        for a in self:
            if len(a.depot_id) > 1:
                a.salary = 15000000
            else:
                a.salary = 10000000

    @api.multi
    @api.depends('club_id')
    def _get_status(self):
        for i in self:
            if i.club_id:
                i.state_player = 'n_free'
            else:
                i.state_player = 'free'