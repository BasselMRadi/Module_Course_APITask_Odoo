from odoo import models, api, fields
from odoo.exceptions import ValidationError
from datetime import date
import string
import random


class Partner(models.Model):
    _inherit = "res.partner"
    _description = "Partner"

    phone = fields.Char(required=True)
    user_type = fields.Selection([
        ('lecturer', 'Lecturer'),
        ('student', 'Student')
    ], required=True, string="User Type", tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", tracking=True)
    token = fields.Char(string="User Token", readonly=True, tracking=True)
    age = fields.Integer(string="Age", compute="_compute_age", store=True, tracking=True)
    course_ids = fields.Many2many('slide.channel', string='Courses')
    years_of_experience = fields.Integer(string="Years of Experience", default=0, tracking=True)

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone:
                if len(record.phone) != 12 or not record.phone.startswith('966'):
                    raise ValidationError('Phone number must be 12 digits long and start with 966')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                date_of_birth = fields.Date.from_string(record .date_of_birth)
                age = today.year - date_of_birth.year - (
                            (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
                record.age = age
            else:
                record.age = 0

    @api.model
    def create(self, vals):
        vals['token'] = self._generate_unique_token()
        return super(Partner, self).create(vals)

    def _generate_unique_token(self):
        token_length = 12
        characters = string.ascii_letters + string.digits
        token = ''.join(random.choice(characters) for _ in range(token_length))
        while self.env['res.partner'].search([('token', '=', token)]):
            token = ''.join(random.choice(characters) for _ in range(token_length))
        return token