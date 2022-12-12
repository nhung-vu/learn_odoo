from odoo import models, fields

class ViinVipAcademy(models.Model):
    _name = 'viin.vip.academy'
    _description = 'Viin Vip Academy'
    _inherit ='education.class' 
    
    historical_student_ids = fields.Many2many(
        comodel_name='education.student',
        relation='class_education_rel2',
        column1='class_id',
        column2='student_id',
        string='Historical student'
        )
    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_vip_id',
        string="Student",
        help="The students that belong to the class"
        )
    
    credit = fields.Char(string='Credit')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    