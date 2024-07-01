from odoo import http
from odoo.http import request


class PartnerController(http.Controller):

    @http.route('/api/register_partner', type='json', auth='public', methods=['POST'], csrf=False)
    def register_partner(self, **kwargs):
        print("..................sads")
        name = kwargs.get('name')
        phone = kwargs.get('phone')
        user_type = kwargs.get('user_type')
        date_of_birth = kwargs.get('date_of_birth', False)  # Optional

        if not name or not phone or not user_type:
            return 'Name, phone, and user type are required.'

        if len(phone) != 12 or not phone.startswith('966'):
            return 'Phone number must be 12 digits long and start with 966.'

        partner_vals = [{
            'name': name,
            'phone': phone,
            'user_type': user_type,
            'date_of_birth': date_of_birth or ""
        }]
        partner = request.env['res.partner'].sudo().create(partner_vals)

        return f'Partner created successfully. Token: {partner.token}'
