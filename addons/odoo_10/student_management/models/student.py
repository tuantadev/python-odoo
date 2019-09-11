from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code', readonly=1)
    dob = fields.Date(string='Birthday')
    phone = fields.Char(string='Phone')
    class_class_ids = fields.Many2many('class.class', string='Class')
    subject_ids = fields.Many2many('subjects', string='Subject')
    point_ids = fields.One2many('points', 'student_id', string='Points')
    state = fields.Selection(selection=[
        ('enroll', 'Enroll'), ('progress', 'Progress'),
        ('graduate', 'Graduate')], compute='_get_state',
        store=True, string='State')

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('student_seq')
        record = super(Student, self).create(vals)
        return record

    @api.depends('class_class_ids', 'subject_ids')
    @api.multi
    def _get_state(self):
        for student in self:
            if len(student.class_class_ids) > 0 and len(student.subject_ids) > 0:
                student.state = 'progress'
            else:
                student.state = 'enroll'
