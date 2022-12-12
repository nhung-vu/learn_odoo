from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'
    
    name = fields.Char(
        string = 'Class Name',
        help = 'The name of class',
        required = True,      
        )
    
    state = fields.Selection(
        [
            ('draft','Draft'),
            ('confirmed','Confirmed'),
            ('done','Done'),
            ('canceled','Canceled'),
            ],
        string = 'Status',
        required = True,
        default = 'draft',
        help = "Status of the class"
        )
    
    description = fields.Char(
        string = 'Description',
        help = 'Description for class'
        )
    
    active = fields.Boolean(default=True)
    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_id',
        string="Student",
        help="The students that belong to the class",
        )
    
    historical_student_ids = fields.Many2many(
        comodel_name='education.student',
        relation='class_education_rel',
        column1='class_id',
        column2='student_id',
        string='Historical student',
        )
    
    company_id = fields.Many2one(
        comodel_name='res.company',
        string="Company",
        default=lambda self: self.env.company,
        )
    
    students_count = fields.Integer(
        string="Students count",
        help="Number of students in this class",
        compute="_compute_students_count",
        store=True,
        )
    
    historical_students_count = fields.Integer(
        string="Historical students count",
        help="Number of historical students in this class",
        compute="_compute_historical_students_count",
        store=True,
        )
    
    start_date = fields.Date(string="Start date")
    
    end_date = fields.Date(string="End date")
    
    responsible = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        )
    
    @api.depends('student_ids')
    def _compute_students_count(self):
        for r in self:
            r.students_count = len(r.student_ids)
            
    def _compute_historical_students_count(self):
        for r in self:
            r.historical_students_count = len(r.historical_student_ids)
        
    period_payment = fields.Float(
        string="Period payment",
        compute="_compute_period_payment",
        readonly=False,
        )
    
    @api.onchange('students_count')
    def _compute_period_payment(self):
        if self.students_count > 0:
            self.period_payment = "3"
    
    _sql_constraints = [
        ('class_uniq',
         'unique(name)',
         "The name of class must be unique per company")
    ]
    
    @api.constrains('start_date','end_date')
    def _check_date(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("The course of class must be earlier than or equal to end date.")
    
    
    
    
    
    
    
    
    
    