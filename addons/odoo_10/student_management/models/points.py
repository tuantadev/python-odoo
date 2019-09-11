from odoo import models, fields, api

class Points(models.Model):
    _name = 'points'
    _rec_name = 'display_name'

    student_id = fields.Many2one('student', string='Student')
    subject_id = fields.Many2one('subjects', string='Subject')
    display_name = fields.Char(string='Display Name', compute='_get_point_name',
                               store=True)
    point = fields.Float(string='Point')

    @api.depends('student_id', 'subject_id')
    def _get_point_name(self):
        for point in self:
            point.display_name = point.student_id.name + point.subject_id.name
