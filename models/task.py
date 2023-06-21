from odoo import api, fields, models


class InheritedAccountAccount(models.Model):
    _name = 'odoo_ui_template.task'
    _description = 'A test model for tasks'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
