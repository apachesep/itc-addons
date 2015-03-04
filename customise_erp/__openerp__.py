# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2014-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
{
    "name" : "Customise Erp",
    "version" : "1.0",
    "depends" : [
                 'sale',
                 'account_accountant',
                 'crm','purchase',
                 'hr_contract',
                 'contacts','hr',
                 'delivery','document',
                 'hr_payroll',
                 'account_analytic_analysis',
                 ],
    "author" : "Browseinfo",

    "description": """
    This module is use to add extra field in sale order , invoice , purchase ,hr and crm.
    """,

    "website" : "www.browseinfo.in",

    "data" : [
              'sale_view.xml',
              'crm/crm_lead_view.xml',
              'crm/crm_sequence.xml',
              'contacts/res_partner_view.xml',
              'contacts/partner_workflow.xml',
              'product/product_template_view.xml',
#               'product/product_workflow.xml',
              'hr_employee/hr_emp_extview.xml',
              'purchase/purchase_extend_view.xml',
              'hr_contract/hr_extend_view.xml',
              'hr_contract/contract_workflow.xml',
              'account_analytic_analysis/account_analytic_analysis_view.xml'
              ],
    "auto_install": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
