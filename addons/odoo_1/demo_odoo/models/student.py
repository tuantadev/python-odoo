from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Studen Object Model'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    exam = fields.Boolean(string='Boolean Type')
    dob = fields.Date(string='Birthday')
    input_date = fields.Datetime(string = 'Date')



