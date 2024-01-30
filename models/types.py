from odoo import models, fields, api, _


class GrievanceFormTypes(models.Model):
    _name = 'grievance.form.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Grievance Types'
    _rec_name = 'type'

    type = fields.Char(string='Type')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    assigned_to_users = fields.Many2many('res.users', string='Assigned To Users')
