{
    'name'  : "Parkir",
    'version'   : "15.0.1.0.0",
    'summary'   : "Module Untuk Parkir",
    'description'   : """
    - Manage Roda 2
    - Manage Roda 4

""",
    'website'   : "www.parkir.com",
    'category'  : "New Tools",
    'author'    : "Galih Nur Arafat",
    'maintainer': "ArafatDev",
    'license'   : "AGPL-3",
    'depends'   : [
        'base',
        'mail',
        'report_xlsx',
    ],
    'data'      : [
        'view/parkir.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/report.xml',
        'reports/parkir_card.xml',
        'wizards/create_parkir.xml',
    ],
    'images'    : "static/description/icon.png",
    'application'   : True,
}