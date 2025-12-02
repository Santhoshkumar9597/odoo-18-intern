from odoo import models, fields, api

class Candidate(models.Model):
    _name = 'interview.candidate'
    _description = 'Interview Candidate'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)
    email = fields.Char(string="Email", tracking=True,required=True)
    phone = fields.Char(string="Phone Number")
    degree = fields.Char(string="Degree",required=True)
    skills_ids = fields.Many2many('res.partner.category',string="Skills")
    expected_salary = fields.Float(string="Expected Salary")
    summary = fields.Text(string="Short Summary")
    experience_years = fields.Float(string="Work Experience Years")
    photo = fields.Binary(string="Photo")

    state = fields.Selection([
        ('initial', 'Initial'),('qualification', 'Qualify'),('exam', 'Examination'),
        ('selected', 'Selected'),('rejected', 'Rejected')], string='Status', default='initial', tracking=True)

    @api.depends('state')
    def action_initial(self):
        self.state = 'initial'

    def action_qualification(self):
        self.state = 'qualification'

    def action_examine(self):
        self.state = 'exam'

    def action_selected(self):
        self.state = 'selected'

    def action_rejected(self):
        self.state = 'rejected'

