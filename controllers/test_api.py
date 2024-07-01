from odoo import http


class TestApi(http.Controller):

    @http.route("/v2/res_partner", methods=["GET"], type="json", authu="none", csrf=False)
    def test_endpoint(self):
        print("inside test endpoint method")

        # def get_courses(self, **kwargs):
        #     user = request.env.user
        #     print(user)
        #     courses = request.env['slide.channel'].search([('user_ids', 'in', user.id)])
        #
        #     course_data = []
        #     for course in courses:
        #         course_data.append({
        #             'id': course.id,
        #             'name': course.name,
        #             'description': course.description,
        #         })
        #
        #     return {'status': 'success', 'data': course_data}
        #
        #

        # def courses_grouped_by_responsible(self, **kwargs):
        #     token = kwargs.get('token')
        #
        #     if not token:
        #         return {'status': 'error', 'message': 'Authorization token is required.'}
        #
        #     partner = request.env['res.partner'].sudo().search([('token', '=', token)], limit=1)
        #     print(partner)
        #     if not partner:
        #         return {'status': 'error', 'message': 'Invalid token.'}
        #
        #     show_fields = ["name", "user_id", "description"]
        #     courses = request.env['slide.channel'].sudo().search_read([('user_id.partner_id', '=', partner.id)],
        #                                                               fields=show_fields)
        #     print(courses)
        #     print(partner.id)
        #     # return {'status': 'success', 'data': courses}
        #     # return {'status': 'success', 'data': courses}
        #     if not courses:
        #         return {'error': 'Invalid token or no courses found'}
        #
        #     grouped_courses = {}
        #     print(courses)
        #
        #     for course in courses:
        #         responsible = course.user_id
        #         responsible_name = responsible.name
        #         responsible_age = responsible.age
        #         responsible_years_of_experience = responsible.years_of_experience
        #         responsible_key = (responsible_name, responsible_age, responsible.years_of_experience)
        #         if responsible_key not in grouped_courses:
        #             grouped_courses[responsible_key] = {
        #                 'responsible_info': {
        #                     'name': responsible.name,
        #                     'age': responsible.age,
        #                     'years_of_experience': responsible.years_of_experience,
        #                 },
        #                 'courses': []
        #             }
        #         print(courses)
        #         grouped_courses[responsible_key]['courses'].append({
        #             'course_info': {
        #                 'id': course.id,
        #                 'name': course.name,
        #                 'description': course.description,
        #                 'num_of_views': course.total_views,
        #                 'last_update': course.slide_last_update,
        #                 'image_url': course.image_1920
        #             },
        #             'course_content': [
        #                 {
        #                     'title': content.name,
        #                     'type': content.slide_type,
        #                     'url': content.datas,
        #                     'duration': content.completion_time,
        #                     'image_url': content.image_1920
        #                 }
        #                 for content in course.slide_content_ids
        #             ]
        #         })
        #
        #     response_data = [data for data in grouped_courses.values()]
        #     return {'status': 'success', 'data': response_data}

        # class CofurseController(http.Controller):
        #         @http.route('/responsible/course_controller_api', type='json', auth='public', methods=['GET'], csrf=False)
        #         def get_token(self, **kwargs):
        #             try:
        #                 token = kwargs.get('token')
        #                 if not token:
        #                     raise UserError('Token is required')
        #                 return {'token': token}
        #             except UserError as e:
        #                 return {'error': str(e)}
        #
        #         @http.route('/responsible/get_courses', type='json', auth='public', methods=['POST'], csrf=False)
        #         def get_courses(self, **kwargs):
        #             try:
        #                 token = kwargs.get('token')
        #                 if not token:
        #                     raise UserError('Token is required')
        #
        #                 courses = request.env['slide.channel'].sudo().search([('token', '=', token)])
        #                 if not courses:
        #                     raise MissingError('Invalid token or no courses found')
        #
        #                 courses_list = [{'id': course.id, 'name': course.name} for course in courses]
        #                 return {'courses': courses_list}
        #             except (UserError, AccessError, ValidationError, MissingError) as e:
        #                 return {'error': str(e)}

        # class CourseController(http.Controller):
        #     @http.route('/responsible/course_controller_api', type='json', auth='public', methods=['GET'], csrf=False)
        #     def get_token(self, **kwargs):
        #         try:
        #             token = kwargs.get('token')
        #             if not token:
        #                 raise UserError('Token is required')
        #             return {'token': token}
        #         except UserError as e:
        #             return {'error': str(e)}
        #
        #     @http.route('/responsible/get_courses', type='json', auth='public', methods=['POST'], csrf=False)
        #     def get_courses(self, **kwargs):
        #         try:
        #             token = kwargs.get('token')
        #             if not token:
        #                 raise UserError('Token is required')
        #
        #             if token == 'invalid_token':
        #                 raise MyCustomError('This is a custom error for invalid tokens')
        #
        #             courses = request.env['slide.channel'].sudo().search([('token', '=', token)])
        #             if not courses:
        #                 raise UserError('Invalid token or no courses found')
        #
        #             courses_list = [{'id': course.id, 'name': course.name} for course in courses]
        #             return {'courses': courses_list}
        #         except (UserError, MyCustomError) as e:
        #             return {'error': str(e)}
        #

        # def get_responsible(self, **kwargs):
        #     try:
        #         token = kwargs.get('token')
        #         responsible = request.env['slide.channel'].sudo().search([('token', '=', token)])
        #
        #         print(token)
        #         if not responsible:
        #             return request.make_json_response({'error': "There are not token"}, status=400)
        #         return request.make_json_response([{
        #             "name": responsible.name,
        #             "age": responsible.age,
        #             "responsible_years_of_experience": responsible.years_of_experience,
        #             "courses": [],
        #         }for responsible_id in responsible],status=200)
        #     except: Excepation as error :
        #         return request.make_json_response({'error': "error"}, status=400)

        # courses = request.env['slide.channel'].sudo().search([('token', '=', token)])
        # if not courses:
        #     return {'error': 'Invalid token or no courses found'}
        # grouped_courses = {}
        # for course in courses:
        #     responsible = course.user_id
        #     responsible_name = responsible.name
        #     responsible_age = responsible.age
        #     responsible_years_of_experience = responsible.years_of_experience
        #     responsible_key = (responsible_name, responsible_age, responsible.years_of_experience)
        #     if responsible_key not in grouped_courses:
        #         grouped_courses[responsible_key] = {
        #             'responsible_info': {
        #                 'name': responsible.name,
        #                 'age': responsible.age,
        #                 'years_of_experience': responsible.years_of_experience,
        #             },
        #             'courses': []
        #         }
        #
        #     grouped_courses[responsible_key]['courses'].append({
        #         'course_info': {
        #             'id': course.id,
        #             'name': course.name,
        #             'description': course.description,
        #             'num_of_views': course.total_views,
        #             'last_update': course.slide_last_update,
        #             'image_url': course.image_1920
        #         },
        #         'course_content': [
        #             {
        #                 'title': content.name,
        #                 'type': content.slide_type,
        #                 'url': content.datas,
        #                 'duration': content.completion_time,
        #                 'image_url': content.image_1920
        #             }
        #             for content in course.slide_content_ids
        #         ]
        #     })
        #
        # response_data = [data for data in grouped_courses.values()]
        # return {'status': 'success', 'data': response_data}

        #     def get_token(self, **kwargs):
        #
        #         token = kwargs.get('token')
        #
        #         if not token:
        #            # return {'token': token}
        #         # else:
        #             return {'error': 'Failed to get token'}
        #         # print('courses_grouped_by_responsible', token)
        #         # if not token:
        #         #     return {'status': 'error', 'message': 'Authorization token is required.'}
        #         # print('courses_grouped_by_responsible', token)
        #         partner = request.env['slide.channel'].sudo().search([('name', '=', "Mitchell Admin")], limit=1)
        #         # courses = request.env['course.course'].sudo().search([('token', '=', token)])
        #
        #         # partner = request.env['res.partner'].sudo().search([('token', '=', token)])
        #         print('courses_grouped_by_responsible', token)
        #
        #         # if not partner:
        #         #     return {'status': 'error', 'message': 'Invalid token.'}
        #         print(partner)
        #         courses = request.env['slide.channel'].sudo().search([])
        #         print(token)

        #
        #     def courses_grouped_by_responsible(self, **kwargs):
        #         token = kwargs.get('token')
        #
        #         print('courses_grouped_by_responsible', token)
        #
        #         if not token:
        #             return {'status': 'error', 'message': 'Authorization token is required.'}
        #
        #         print('courses_grouped_by_responsible', token)
        #
        #         partner = request.env['res.partner'].sudo().search([('token', '=', token)])
        #         print('courses_grouped_by_responsible', token)
        #
        #         # user = partner.user_id
        #         # if not user:
        #         #     return {'status': 'error', 'message': 'No user associated with this partner.'}
        #
        #         if not partner:
        #             return {'status': 'error', 'message': 'Invalid token.'}
        #
        #         print('-----------courses_grouped_by_responsible', token)
        #
        #         courses = request.env['slide.channel'].sudo().search([])
        #         grouped_courses = {}
        #
        #         for course in courses:
        #             responsible = course.user_id
        #             responsible_name = responsible.name
        #             responsible_age = responsible.age
        #             responsible_key = (responsible_name, responsible_age)
        #             if responsible_key not in grouped_courses:
        #                 grouped_courses[responsible_key] = {
        #                     'name': responsible_name,
        #                     'age': responsible_age,
        #                     'course_content': []
        #                 }
        #
        #             grouped_courses[responsible_key]['course_content'].append({
        #                 'id': course.id,
        #                 'name': course.name,
        #                 'description': course.description,
        #                 'num_of_views': course.total_views,
        #                 'last_update': course.slide_last_update,
        #                 'image_url': course.image_1920
        #
        #             })
        #
        #         response_data = []
        #         for responsible_key, data in grouped_courses.items():
        #             responsible_name, responsible_age = responsible_key
        #             response_data.append({
        #                 'name': responsible_name,
        #                 'age': responsible_age,
        #                 'course_content': data['course_content']
        #             })
        #
        #         return {'status': 'success', 'data': response_data}
        #
        # def get_courses(self, **kwargs):
        #     # Get the logged-in user
        #     user = request.env.user
        #     print(user)
        #     # Fetch courses accessible to the user
        #     courses = request.env['slide.channel'].search([('user_ids', 'in', user.id)])
        #
        #     course_data = []
        #     for course in courses:
        #         course_data.append({
        #             'id': course.id,
        #             'name': course.name,
        #             'description': course.description,
        #         })
        #
        #     return {'status': 'success', 'data': course_data}
