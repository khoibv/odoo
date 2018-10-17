# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Mbo(models.Model):
    _name = 'nev.mbo.mbo'

    name = fields.Char(required=True)

    # add Object mbo
    objective_ids = fields.One2many(comodel_name='nev.mbo.objective', inverse_name='objective_id',
                                    string=_("Objective List"))

    # MBO's holder
    user_id = fields.Many2one(comodel_name='res.users', ondelete='set null', string=_("User"), index=True)

    mbo_plan_id = fields.Many2one('nev.mbo.mbo_plan', ondelete='cascade', string=_("MBO Plan"), required=True)

    # Nhân viên đã xác nhận MBO của bản thân (True/False)
    employee_approved = fields.Boolean(string=_("Approved"), required=True, default=False)

    # Manager đã xác nhận MBO của nhân viên (True/False)
    manager_approved = fields.Boolean(string=_("Manager Approved"), required=True, default=False)
