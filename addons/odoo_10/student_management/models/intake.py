from odoo import models, fields, api


class Intake(models.Model):
    _name = 'intake'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    subject_ids = fields.Many2many('subjects', string='Subjects')
