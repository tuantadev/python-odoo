from odoo import models, fields, api


class Subjects(models.Model):
    _name = 'subjects'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    intake_ids = fields.Many2many('intake', string='Intakes')
