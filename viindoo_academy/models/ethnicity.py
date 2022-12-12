from odoo import models, fields, api

class Ethnicity(models.Model):
    _name = 'ethnicity'
    _description = 'Ethnicity'
    
    name = fields.Char(
        string="Name"
        )
    
    code = fields.Char(
        string="Code"
        )
    
    description = fields.Char(
        string="Description"
        )
    
    country_ids = fields.Many2many(
        comodel_name="res.country",
        relation="ethnicity_rel",
        column1="ethnicity_id",
        column2="country_id",
        )
    
    
    
    
    
    
    
    