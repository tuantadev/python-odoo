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

        'data/data.xml',
        'views/order_view.xml',
        'views/product_view.xml',
        'views/customer_view.xml',

        'wizard/res_partner_comment.xml',
        'wizard/add_price.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
