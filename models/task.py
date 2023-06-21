from odoo import api, fields, models


class InheritedAccountAccount(models.Model):
    _name = 'task.task'
    _description = 'A test model for tasks'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
