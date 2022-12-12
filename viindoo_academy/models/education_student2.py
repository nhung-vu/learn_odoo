from odoo import models, fields

class EducationStudent(models.Model):
    _inherit = 'education.student'
    
    class_vip_id = fields.Many2one(
        comodel_name='viin.vip.academy',
        string='Current Vip Class',
        groups="base.group_user,viindoo_academy.group_viindoo_academy_user",
        )

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    