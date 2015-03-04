from openerp.osv import osv, fields
from openerp.osv.fields import _column
from bsddb.dbtables import _columns_key


class hr_employee(osv.osv):

    _inherit = "hr.employee"

    _columns = {
               'spouce':fields.char('Spouse Name'),
               'join_date':fields.date('Date of Joining'),
               'name_passport':fields.char('Complete name as shown on passport'),
               'date_issue':fields.date('Date of Issue'),
'bank_account_num':fields.char('Bank Account Number'),
               'date_expiry':fields.date('Date of Expiry'),
               'validity':fields.char('Validity'),
               'place_issued':fields.char('Place issued'),
               'current_visa':fields.char('Current visa'),
               'name_eme':fields.char('Name'),
               'relationship':fields.char('Relationship'),
               'address':fields.char('Address'),
               'city':fields.char('City , Country'),
               'home_phone':fields.char('Home Phone'),
               'mobile':fields.char('Mobile'),
               'name_eme1':fields.char('Name'),
               'relationship1':fields.char('Relationship'),
               'address1':fields.char('Address'),
               'city1':fields.char('City , Country'),
               'home_phone1':fields.char('Home Phone'),
               'mobile1':fields.char('Mobile'),
               'remark':fields.text(''),
               'name_phy':fields.char('Physician Name'),
               'address_phy':fields.char('Address'),
               'city_phy':fields.char('City , Country'),
               'home_phone_phy':fields.char('Home Phone'),
               'state' : fields.selection([('draft','Draft'),
                                           ('review1','Review 1'),
                                           ('reviewer2','Reviewer 2'),
                                           ('approver1','Approver 1'),
                                           ('approver2','Approver 2')], 'State',select=True, store=True),
                'id_type' : fields.many2one('id.type','ID Type'),
                'title_labour' : fields.many2one('title.labour','Title of Labour Contract')
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
               
class id_type(osv.osv):
    
    _name = "id.type"
    
    _columns = {
                'name' : fields.char('ID Type'),
                }

class title_labour(osv.osv):
    
    _name = "title.labour"
    
    _columns = {
                'name' : fields.char('Title of Labour Contract'),
                }

