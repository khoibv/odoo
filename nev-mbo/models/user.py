# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class User(models.Model):
    # Kế thừa từ user có sẵn trong hệ thống
    # Tham khảo class PartnerCategory (res_partner.py)
    _inherit = 'res.user'
    _description = 'User'

    # Add a new column to the res.user model, by default users do not have manager
    is_manager = fields.Boolean(string=_("Is manager"), default=False)
    manager_id = fields.Many2one(comodel_name='res.user', string='Manager', index=True, ondelete='set null')

    # Nếu là manager thì sẽ có danh sách các user thuộc quyền quản lý của manager
    employee_ids = fields.One2many(comodel_name='res.user', inverse_name='parent_id', string=_("Employees"))

    # Mỗi user có nhiều MBO
    mbo_ids = fields.One2many(comodel_name='nev.mbo.mbo',
                              inverse_name='user_id',
                              string=_("MBO List"),
                              readonly=True)

    @api.constrains('manager_id')
    def _check_parent_id(self):
        # Đảm bảo không bị lặp vòng
        # (VD lặp vòng : A là manager của B, B là manager của C, nhưng C lại là manager của A!!!)
        if not self._check_recursion():
            raise ValidationError(_('You can not create recursive tags.'))