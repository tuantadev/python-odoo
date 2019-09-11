{
    'name' : 'Student Management',
    'version' : '1.0',
    'summary': 'Student Mangement',
    'sequence': 1,
    'description': """

    """,
    'category': '',
    'website': '',
    'depends' : ['base'],
    'data': [
        'data/data.xml',

        'views/student_view.xml',
        'views/class_class_view.xml',
        'views/intake_view.xml',
        'views/subject_view.xml',
        'views/point_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
