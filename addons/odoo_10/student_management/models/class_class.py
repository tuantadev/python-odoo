from odoo import models, fields, api


class ClassClass(models.Model):
    _name = 'class.class'

    code = fields.Char(string='Code')
    name = fields.Char(string='Class')
    student_ids = fields.Many2many('student', string='Students')
