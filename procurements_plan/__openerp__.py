# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
{
    "name": "Procurements Plan",
    "version": "1.0",
    "author": "OdooMRP team",
    "category": "Procurements",
    "website": "http://www.odoomrp.com",
    "description": """
    This module performs the following:
    1.- Create the action ASSIGN PROJECT/ANALYTIC ACCOUNT in the object
        Procurement Order. With this option you can assign one project to the
        selected procurement orders.
    """,
    "depends": ['procurement',
                'project',
                'stock',
                'purchase',
                'sale',
                'sale_stock'
                ],
    "data": ['data/workflow.xml',
             'data/sequence.xml',
             'security/procurements_with_plan.xml',
             'security/ir.model.access.csv',
             'wizard/run_scheduler_with_plan_view.xml',
             'views/procurement_view.xml',
             'views/purchase_order_view.xml',
             'views/procurement_plan_view.xml',
             ],
    "installable": True
}