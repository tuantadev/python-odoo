{
    'name' : 'Order Manager',
    'version' : '1.0',
    'summary': 'Demo Model Relation',
    'sequence': 1,
    'description': """

    """,
    'category': '',
    'website': '',
    'depends' : ['base'],
    'data': [
        'security/order_manager_security.xml',
        'security/ir.model.access.csv',

        'views/order_view.xml',
        'views/product_view.xml',
        'views/customer_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
