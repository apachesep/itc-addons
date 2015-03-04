from openerp.osv import osv, fields

class account_analytic_account(osv.osv):
    
    _inherit = "account.analytic.account"
    
    _columns = {
                'lpo':fields.char('LPO#'),
                'con_offi':fields.char('Contract official#'),
                'subject':fields.char('Subject'),
                'type_vt':fields.many2one('contract.type','Type'),
                'track_unit':fields.many2one('tracking.unit','Tracking Unit'),
                'total_unit':fields.char('Total Units'),
                'use_unit':fields.char('Used Units'),
                'priority':fields.many2one('contract.priority','Priority'),
                'renewal_notice':fields.char('Renewal Notice'),
                'terminate':fields.boolean('Terminated'),
                'scope':fields.char('Scope'),
                'engineer':fields.char('Engineer'),
                'sla':fields.char('SLA'),
                'detail_scope':fields.char('Detailed Scope'),
                'performance': fields.boolean('Performance bond'),
                'cont_value':fields.char('Contract Value'),
                'pb_value':fields.char('PB Value'),
                'payment_sche':fields.char('Payment Schedule'),
                'pb_issue':fields.char('PB Issuer'),
                'user_id' : fields.many2one('res.users','Assigned to'),
                'section_id' : fields.many2one('crm.case.section','Team'),
                'contract_no' : fields.char('Contract No'),
                'endind_date' : fields.date('Ending Date'),
                }

class tracking_unit(osv.osv):
    
    _name = "tracking.unit"
    
    _columns = {
                'name' : fields.char('Tracking Unit'),
                }    

class contract_type(osv.osv):

    _name = "contract.type"
    
    _columns = {
                'name' : fields.char('Type'),
                }

class contract_priority(osv.osv):
    
    _name = "contract.priority"
    
    _columns = {
                'name' : fields.char('Priority')
                }

