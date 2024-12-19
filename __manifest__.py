# -*- coding: utf-8 -*-
{
    'name': "escuela",

    'summary': "Módulo de gestión de escuela",

    'description': """
Este módulo gestiona estudiantes, asignaturas y grupos dentro de una escuela.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/view_estudiante.xml',
        'views/view_asignatura.xml', 
        'views/view_grupo.xml',
        'views/menu_escuela.xml',
        'security/ir.model.access.csv',
        'reports/escuela_reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

