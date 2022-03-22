# -*- coding: utf-8 -*-
{
    'name': "my_module",

    'summary': """
        lalala""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,


    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management'],

    # only loaded in demonstration mode
    'data': [
        'security/ir.model.access.csv',
        'views/booking_views.xml',
        'views/service_team_view.xml',
        'views/work_order_views.xml',
        'views/menu.xml',   
    ],
}