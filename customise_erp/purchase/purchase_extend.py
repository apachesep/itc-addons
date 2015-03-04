from openerp.osv import osv, fields

class purchase_order(osv.osv):

    _inherit = "purchase.order"

    _columns = {

               'subject' : fields.char('Subject'),
               'requisition' : fields.char('Requisition No.'),
               'tracking' : fields.char('Tracking No.'),
               'carrier' : fields.char('Carrier'),
               'salescomm':fields.char('Sales Commission'),
               'excise':fields.char('Excise Duty'),
               'assign_to':fields.many2one('res.partner','Assigned To'),
               'so':fields.char('SO#'),
               'team' : fields.many2one('crm.case.section','Team'),
               'paid' : fields.boolean('Paid'),
               }