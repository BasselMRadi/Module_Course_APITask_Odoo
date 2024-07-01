# -*- coding: utf-8 -*-
{
    'name': "Courses Management",
    'version': '15.0.0.0.0',
    'summary': 'Module Customizations for an API to register a new partner in our system',
    'sequence': 3,
    'description': """ Module Customizations for an API to register a new partner in our system """,
    'author': "Basel Mahmoud Radi",
    'website': "http://www.linkedin.com/in/bassel-mahmoud-rady-abed-el-baey-201-493-965",
    'License':'LGPL-3.0.3',
    'category': 'productivity',
    'depends': ["base", "website_slides"],
    'data': [
        # 'security/ir.model.access.csv',
        # "base","mail",
        # 'data/hr_attendance_data.xml',
        "views/menu.xml",
        "views/new_partner.xml",
        "views/slide_channel_override.xml",
        # "views/lesson_id.xml",
        # "views/course_id.xml",
        # "views/attendance_ids.xml",
        # "views/instrument_ids.xml",
        # "views/room_ids.xml",
             ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}