from openerp.osv import osv, fields

class product_template(osv.osv):
    
    _inherit = "product.template"
    
    _columns = {
               'part_number' : fields.char('Part Number'),
               'product_no' : fields.char('Product No'),
               'sales_start_date' : fields.date('Sales Start Date'),
               'sales_end_date' : fields.date('Sales End Date'),
               'support_start_date' : fields.date('Support Start Date'),
               'support_expiry_date' : fields.date('Support Expiry Date'),
               'website' : fields.char('Website'),
               'mfr_part_no' : fields.char('Mfr Part No'),
               'vendor_part_no' : fields.char('Vendor Part No'),
               'serial_no' : fields.char('Serial No'),
               'product_sheet' : fields.char('Product Sheet'),
               'gl_account_id' : fields.many2one('gl.account','GL Account'),
               'manufacturer' : fields.char('Manufacturer'),
               'vartical' : fields.boolean('VERTICAL'),
               'annual_sales_target' : fields.char('Annual Sales Target'),
               'vertical_priority' : fields.char('Vertical Priority'),
               'state' : fields.selection([('draft','Draft'),
                                           ('review1','Review 1'),
                                           ('reviewer2','Reviewer 2'),
                                           ('approver1','Approver 1'),
                                           ('approver2','Approver 2')], 'State',select=True, store=True),
                'industry' : fields.char('Industry'),
                'commission_rate' : fields.float('Commission Rate(%)'),
                'handler' : fields.char('Handler'),
               }
    
    _defaults = {
                 'state' : 'draft',
                 }
    
    def product_review1(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'review1'})
        return True
    
    def product_reviewer2(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'reviewer2'})
        return True
    
    def product_approver1(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'approver1'})
        return True
    
    def product_approver2(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'approver2'})
        return True
    
class gl_account(osv.osv):
    
    _name = "gl.account"

    _columns = {
                'name' : fields.char('Gl Account'),
                }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
