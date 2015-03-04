from openerp.osv import fields, osv
from openerp.tools.translate import _
import re

class crm_lead2opportunity_partner(osv.osv_memory):
    _inherit = 'crm.lead2opportunity.partner'

    def action_apply(self, cr, uid, ids, context=None):
        """
        Convert lead to opportunity or merge lead and opportunity and open
        the freshly created opportunity view.
        """
        if context is None:
            context = {}

        lead_obj = self.pool['crm.lead']

        w = self.browse(cr, uid, ids, context=context)[0]
        opp_ids = [o.id for o in w.opportunity_ids]
        if w.name == 'merge':
            lead_id = lead_obj.merge_opportunity(cr, uid, opp_ids, context=context)
            lead_ids = [lead_id]
            lead = lead_obj.read(cr, uid, lead_id, ['type', 'user_id'], context=context)
            if lead['type'] == "lead":
                context = dict(context, active_ids=lead_ids)
                self._convert_opportunity(cr, uid, ids, {'lead_ids': lead_ids, 'user_ids': [w.user_id.id], 'section_id': w.section_id.id}, context=context)
            elif not context.get('no_force_assignation') or not lead['user_id']:
                lead_obj.write(cr, uid, lead_id, {'user_id': w.user_id.id, 'section_id': w.section_id.id}, context=context)
        else:
            lead_ids = context.get('active_ids', [])
            self._convert_opportunity(cr, uid, ids, {'lead_ids': lead_ids, 'user_ids': [w.user_id.id], 'section_id': w.section_id.id}, context=context)
        
        lead_dicts = lead_obj.read(cr, uid, lead_ids, ['name'])
        for lead_dict in lead_dicts:
            lead_dict['name'] = 'POT' + lead_dict['name'][3:]
            lead_obj.write(cr, uid, lead_dict['id'],{'name' : lead_dict['name']})
        return self.pool.get('crm.lead').redirect_opportunity_view(cr, uid, lead_ids[0], context=context)
    
    
class crm_lead2opportunity_mass_convert(osv.osv_memory):
    _inherit = 'crm.lead2opportunity.partner.mass'
    
    def action_apply(self, cr, uid, ids, context=None):
        """
        Convert lead to opportunity or merge lead and opportunity and open
        the freshly created opportunity view.
        """
        if context is None:
            context = {}

        lead_obj = self.pool['crm.lead']

        w = self.browse(cr, uid, ids, context=context)[0]
        opp_ids = [o.id for o in w.opportunity_ids]
        if w.name == 'merge':
            lead_id = lead_obj.merge_opportunity(cr, uid, opp_ids, context=context)
            lead_ids = [lead_id]
            lead = lead_obj.read(cr, uid, lead_id, ['type', 'user_id'], context=context)
            if lead['type'] == "lead":
                context = dict(context, active_ids=lead_ids)
                self._convert_opportunity(cr, uid, ids, {'lead_ids': lead_ids, 'user_ids': [w.user_id.id], 'section_id': w.section_id.id}, context=context)
            elif not context.get('no_force_assignation') or not lead['user_id']:
                lead_obj.write(cr, uid, lead_id, {'user_id': w.user_id.id, 'section_id': w.section_id.id}, context=context)
        else:
            lead_ids = context.get('active_ids', [])
            self._convert_opportunity(cr, uid, ids, {'lead_ids': lead_ids, 'user_ids': [w.user_id.id], 'section_id': w.section_id.id}, context=context)
        
        lead_dicts = lead_obj.read(cr, uid, lead_ids, ['name'])
        for lead_dict in lead_dicts:
            lead_dict['name'] = 'POT' + lead_dict['name'][3:]
            lead_obj.write(cr, uid, lead_dict['id'],{'name' : lead_dict['name']})
        return self.pool.get('crm.lead').redirect_opportunity_view(cr, uid, lead_ids[0], context=context)
    
    def mass_convert(self, cr, uid, ids, context=None):
        data = self.browse(cr, uid, ids, context=context)[0]
        ctx = dict(context)
        if data.name == 'convert' and data.deduplicate:
            merged_lead_ids = []
            remaining_lead_ids = []
            lead_selected = context.get('active_ids', [])
            for lead_id in lead_selected:
                if lead_id not in merged_lead_ids:
                    lead = self.pool['crm.lead'].browse(cr, uid, lead_id, context=context)
                    duplicated_lead_ids = self._get_duplicated_leads(cr, uid, lead.partner_id.id, lead.partner_id and lead.partner_id.email or lead.email_from)
                    if len(duplicated_lead_ids) > 1:
                        lead_id = self.pool.get('crm.lead').merge_opportunity(cr, uid, duplicated_lead_ids, False, False, context=context)
                        merged_lead_ids.extend(duplicated_lead_ids)
                        remaining_lead_ids.append(lead_id)
            active_ids = set(context.get('active_ids', []))
            active_ids = active_ids.difference(merged_lead_ids)
            active_ids = active_ids.union(remaining_lead_ids)
            ctx['active_ids'] = list(active_ids)
        ctx['no_force_assignation'] = context.get('no_force_assignation', not data.force_assignation)
        return self.action_apply(cr, uid, ids, context=ctx)
