from odoo import models, fields

class EducationClass2(models.Model):
    _inherit = 'education.class'

    country_id = fields.Many2one(
        comodel_name = 'res.country',
        string = 'Country',
        )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    