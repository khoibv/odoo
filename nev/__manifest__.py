# -*- coding: utf-8 -*-
{
    'name': "nev",

    'summary': """
        NEV Odoo module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nissho Electronics Vietnam",
    'website': "http://www.nissho-vn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
