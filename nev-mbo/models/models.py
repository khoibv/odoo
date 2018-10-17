# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Mbo(models.Model):
    _name = 'nev.mbo.mbo'

    name = fields.Char(required=True)

    # User đăng ký MBO
    user_mbo = fields.Text(required=True)

    # add Object mbo
    objective_ids = fields.One2many(comodel_name='nev.mbo.objective', inverse_name='objective_id',
                                    string="MBO List Object")

    # MBO's holder
    user_id = fields.Many2one(comodel_name='res.users', ondelete='set null', string=_("User"), index=True)

    mbo_plan_id = fields.Many2one('nev.mbo.mbo_plan', ondelete='cascade', string=_("MBO Plan"), required=True)
