from openerp.osv import osv, fields
from datetime import datetime, timedelta
import time
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

import openerp.addons.decimal_precision as dp
from openerp import api

class sale_order(osv.osv):
    
    _inherit = "sale.order"
    
    _columns = {
                'subject' : fields.char('Subject'),
                'valid_till' : fields.date('Valid Till'),

                'purchase_order' : fields.char('Purchase Order'),
                'carrier' : fields.char('Carrier'),
                'pending' : fields.char('Pending'),
                'sales_commission' : fields.char('Sales Commission'),
                'excise_duty' : fields.char('Excise Duty'),
                'emable_recurring' : fields.boolean('Enable Recurring'),
                'frequency' : fields.char('Frequency'),
                'start_period' : fields.date('Start Period'),
                'end_period' : fields.date('End Period'),
                'payment_duration' : fields.char('Payment Duration'),
                'invoice_status' : fields.char('Invoice Status'),
                'potential_name' : fields.many2one('crm.lead','Opportunity Name'),
                'customer_no' : fields.char('Customer No'),
		'contact_name':fields.many2one('res.partner','Contact Name'),
                }
    
class account_name(osv.osv):
    
    _name = "account.name"
    
    _columns = {
                'name' : fields.char('Account Name'),
                }
    
class account_invoice(osv.osv):
    
    _inherit = "account.invoice"
    
    _columns = {
                'subject' : fields.char('Subject'),
                'excise_duty' : fields.char('Excise Duty'),
                'sales_commission' : fields.char('Sales Commission'),
                'old_inv' : fields.char('Old Inv.#'),
                'settled' : fields.boolean('Settled'),
                'request_date' : fields.date('Request Date'),
                'effective_date' : fields.date('Effective Date'),
                'maturity_date' : fields.date('Maturity Date'),
                'finance_amount' : fields.float('Finance Amount'),
                'interest_day' : fields.char('Interest_day'),
                'total_interest' : fields.float('Total Interest'),
                'cheque_detail' : fields.char('Cheque Detail'),
                'financed' : fields.boolean('Financed'),
                'gf_settled' : fields.boolean('GF Settled'),
                'customer_no' : fields.char('Customer No'),
                }
    
