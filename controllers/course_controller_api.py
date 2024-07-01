from odoo import http
# from urllib.parse import parse_qs
from odoo.http import request


# import json
# from odoo.exceptions import UserError, AccessError, ValidationError, MissingError


class CourseController(http.Controller):
    @http.route('/responsible/course_controller_api', type='json', auth='public', methods=['GET'], csrf=False)
    def courses_grouped_by_responsible(self, **kwargs):
        token = kwargs.get('token')

        print('courses_grouped_by_responsible', token)

        if not token:
            return {'status': 'error', 'message': 'Authorization token is required.'}

        # print('courses_grouped_by_responsible', token)

        partner = request.env['res.partner'].sudo().search([('token', '=', token)])

        # print('courses_grouped_by_responsible', token)

        if not partner:
            return {'status': 'error', 'message': 'Invalid token.'}

        # print('-----------courses_grouped_by_responsible', token)

        courses = request.env['slide.channel'].sudo().search(
            [('user_id.partner_id', '=', partner.id)])  # ,fields=show_fields)
        grouped_courses = []
        for course in courses:
            course_data = {
                'course_info': {
                    'id': course.id,
                    'name': course.name,
                    'description': course.description,
                    'num_of_views': course.total_views,
                    'last_update': course.slide_last_update.strftime('%d/%m/%Y'),
                    'image_url': course.image_1920

                },
                'course_content': []
            }

            slide_contents = request.env['slide.slide'].sudo().search([('channel_id', '=', course.id)])
            for slide in slide_contents:
                course_data['course_content'].append({
                    'title': slide.name,
                    'type': slide.slide_type,
                    'url': slide.url,
                    'duration': slide.completion_time,
                    'image_url': slide.image_1920
                })
            grouped_courses.append(course_data)
        response_data = {
            'responsible_info': {
                'name': partner.name,
                'age': partner.age,
                'years_of_experience': partner.years_of_experience
            },
            'courses': grouped_courses
        }

        return {'status': 'success', 'data': response_data}
