# -*- coding: utf-8 -*-
##############################################################################
#
# © 2022 Marcelo Costa <marceloengecom@gmail.com>, engeCloud
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
#
##############################################################################
{
    'name': 'Price Readonly',        
    'summary': 'Valor Somente Leitura',
    'description': """Valor 'somente leitura' para usuário específico.""",
    'author': 'Marcelo Costa',
    'website': 'https://engecloud.com/',
    'version': '12.0.1.0',       
    'license': 'AGPL-3',
    'category': 'Base',  
    'depends': ['sale_management', 'account'],
    'data': [
        'data/ir_module_category_data.xml',
        'security/security.xml',
        'views/sale_views.xml',
        'views/account_move_views.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
