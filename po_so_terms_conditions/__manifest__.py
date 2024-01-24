# -*- coding: utf-8 -*-
{
    'name': "TERMS & CONDITIONS IN PO & SO",

    'version': '16.0',
    'summary': 'Manage pricing and terms & conditions for PO and SO',
    'description': """
        This module adds pricing functionality and Terms & Conditions (T&C) 
        - Display T&C on the Vendor Page
        - Reflect T&C on Purchase Orders and its Print
        - Show T&C for Customers on Sales Invoices
    """,

    'author': "beyz",
    'website': "https://www.7d.com.kw",
    'category': 'kuwait-agro',


    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase','sale','l10n_gcc_invoice'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_report_view.xml',
        'data/sequences.xml',
        'report/purchase_custom_report.xml',
        'views/purchase_order.xml',
        'views/purchase_menu.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 199.00,
    'currency': 'USD',
}