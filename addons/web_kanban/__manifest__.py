# -*- coding: utf-8 -*-
# Part of Byte. See LICENSE file for full copyright and licensing details.

{
    'name': 'Base Kanban',
    'category': 'Hidden',
    'description': """
Byte Erp Web kanban view.
========================

""",
    'version': '2.0',
    'depends': ['web'],
    'data' : [
        'views/web_kanban_templates.xml',
    ],
    'qweb' : [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
