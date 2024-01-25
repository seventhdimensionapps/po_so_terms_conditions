# -*- coding: utf-8 -*-
{
    'name': "VENDOR TERMS & CONDITIONS",

    'summary': 'Display/Update/Print Vendor's Terms and Conditions',
    'description': """
        This module adds pricing functionality and Terms & Conditions (T&C) 
        - Update T&C on the Vendor Page
        - Display T&C on Purchase Orders
        - T&C is now available on the "Printed" Purchase Orders
    """,

    "author": "Seventh Dimension Company",
    'website': "https://www.7d.com.kw",
    'category': "Purchases",
    "version": "1.0",
    'license': 'OPL-1',


    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase','sale','l10n_gcc_invoice'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'report/purchase_custom_report.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 75.00,
    'currency': 'USD',
    'images': ['static/description/cover.png'],
}
