{
    'name': 'Interview Process',
    'version': '1.0',
    'sequences': '-200',
    'summary': 'Manage Candidate Interviews',
    'description': 'manage interview process with candidate details',
    'category': 'Custom Modules',
    'author': 'Santhosh',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/candidate_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
