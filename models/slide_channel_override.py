from odoo import models, api, fields


class SlideChannel(models.Model):

    _inherit = 'slide.channel'

    # partner_ids = fields.Many2many('res.partner', string='Responsible Partners')
    token = fields.Many2many('res.partner', string='Partners', readonly=False)
