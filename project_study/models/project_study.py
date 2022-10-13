from odoo import models, fields

class User(models.Model):
    _inherit = 'res.users'
    user_id= fields.Many2one('project.study')
class ProjectStudy(models.Model):
    _name = 'project.study'
    _description = 'Enmasys Project Study'
    list=([('to_do', "TODO"), ('in_progress', "IN-PROGRESS"), ('review', "REVIEW"), ('done', "DONE")])


    name = fields.Char(string='Name', required=True)
    dateline = fields.Date(string='DateLine', required=True)
    note = fields.Text(string='Note')
    description = fields.Text(string='Description')
    status = fields.Selection(selection=list, default='to_do', string='Status', required=True)
    assign_to = fields.Many2one('res.users', string= 'Assign_to')
    project_managers=fields.Many2many('res.users',string='Project Managers')
    task_attendees=fields.One2many('res.users','user_id',string='Task Attendees')
