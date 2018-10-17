{
    'name': "MBO Management",

    'summary': """
        NEV management by objective system (NEV MBO)""",

    'description': """
        Manage by objective system
        - Allow users set objective themselves
        - Allow managers approve user's objective
    """,

    'author': "Nissho Electronics Vietnam",
    'website': "http://www.nissho-vn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/mbo_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views-mbo-plan.xml',
        'views/views-mbo.xml',
        'views/views-objective.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
