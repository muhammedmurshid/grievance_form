{
    'name': "Grievance Form",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail','logic_base'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/grievance_form.xml',
        'views/web_form.xml',
        'views/types.xml',
        'security/rules.xml',
        'data/activity.xml',
    ],
    'demo': [],
    'summary': "Grievance_form",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
