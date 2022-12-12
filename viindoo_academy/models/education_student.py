from odoo import models, fields, api

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = "Education Student"
    
    name = fields.Char(
        string='Name',
        required=True,
        )
    
    class_id = fields.Many2one(
        comodel_name='education.class',
        string='Current Class',
        )
    
    class_ids = fields.Many2many(
        comodel_name ='education.class', 
        relation='class_education_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes',
        )
    
    ethnicity_id = fields.Many2one(
        comodel_name="ethnicity",
        string="Ethnicity",
        )
    
    country_id = fields.Many2one(
        comodel_name="res.country",
        string="Country",
        )
    
    code_id = fields.Char(
        string="Ethnicity code",
        related="ethnicity_id.code",
        store=True,
        )
    
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="User",
        )
    
    @api.onchange('ethnicity_id')
    def _compute_country_id(self):
        self.country_id = self.ethnicity_id.country_ids[:1]
    
    
    
    
    
    
    
    