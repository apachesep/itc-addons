from openerp.osv import osv, fields

class hr_contract(osv.osv):

    _inherit = "hr.contract"

    _columns = {
                'lpo':fields.char('LPO#'),
                'con_offi':fields.char('Contract official#'),
                'subject':fields.char('Subject'),
                'type':fields.char('Type'),
                'track_unit':fields.char('Tracking Unit'),
                'total_unit':fields.char('Total Units'),
                'use_unit':fields.char('Used Units'),
                'priority':fields.char('Priority'),
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
                'state' : fields.selection([('draft','Draft'),('review1','Review 1'),('reviewer2','Reviewer 2'),('approver1','Approver 1'),('approver2','Approver 2')], 'State'),
                'user_id' : fields.many2one('res.users','Assigned to'),
                'section_id' : fields.many2one('crm.case.section','Team'),
                }
    
    _defaults = {
                 'state' : 'draft',
                 }