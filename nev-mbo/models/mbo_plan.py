# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

PLAN_STATUSES = [
    ('none', 'None'),
    ('updating', 'Updating'),
    ('wait for review', 'Wait For Review'),
    ('approved', 'Approved'),
    ('doing', 'Doing'),
    ('evaluating', 'Evaluating'),
    ('finished', 'Finished')
]


class MboPlan(models.Model):
    _name = 'nev.mbo.mbo_plan'

    name = fields.Char(required=True)
    no = fields.Integer()
    status = fields.Selection(selection=PLAN_STATUSES,
                              string=_("Status"),
                              required=True, default='updating')

    mbo_ids = fields.One2many(comodel_name='nev.mbo.mbo', inverse_name='mbo_plan_id', string="MBO list")
