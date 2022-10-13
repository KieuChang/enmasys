from odoo import models, fields


class ProjectStudy(models.Model):
    _name = 'project.study'
    _description = 'Enmasys Project Study'
    list=([('to_do', "TODO"), ('in_progress', "IN-PROGRESS"), ('review', "REVIEW"), ('done', "DONE")])


    name = fields.Char(string='Name', required=True)
    dateline = fields.Date(string='DateLine', required=True)
    note = fields.Text(string='Note')
    description = fields.Text(string='Description')
    status = fields.Selection(selection=list, default='to_do', String='Status', required=True)
    assign_to = fields.Many2one('res.user', 'Assign_to')
