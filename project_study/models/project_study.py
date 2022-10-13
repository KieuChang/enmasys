from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import datetime
import datetime


class User(models.Model):
    _inherit = 'res.users'
    user_id = fields.Many2one('project.study')


class ProjectStudy(models.Model):
    _name = 'project.study'
    _description = 'Enmasys Project Study'
    list = ([('to_do', "TODO"), ('in_progress', "IN-PROGRESS"), ('review', "REVIEW"), ('done', "DONE")])

    name = fields.Char(string='Name', required=True)
    dateline = fields.Date(string='DateLine', required=True)
    note = fields.Text(string='Note')
    description = fields.Text(string='Description')
    status = fields.Selection(selection=list, default='to_do', string='Status', required=True)
    assign_to_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
    project_managers_ids = fields.Many2many('res.users', string='Project Managers')
    task_attendees_ids = fields.One2many('res.users', 'user_id', string='Task Attendees')
    assignee_update_at = fields.Date(string='Assignee Update At', compute='_compute_assignee')
    tags = fields.Selection([('new_feature', "New feature")], string='Tags')
    customer_id = fields.Many2one("res.partner", string="Customer")

    @api.depends("assign_to_id")
    def _compute_assignee(self):
        for record in self:
            record.assignee_update_at = datetime.datetime.today()

    @api.onchange("assign_to_id")
    def _onchange_assign_to_id(self):
        self.tags = 'new_feature'

    @api.constrains('customer_id')
    def _check_customer_id(self):
        for record in self:
            subject = self.env['project.study'].search(
                [('customer_id.id', '=', record.customer_id.id), ('id', '!=', record.id)])
            if subject:
                raise ValidationError("This customer is existed at another task. Please choose another customer")
