{
    'name': 'Item Master',
    'version': '18.0',
    'category': 'item master',
    'author': 'Ativeg Technology',
    'summary': 'this is item master',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/item_master_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}