# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MboObjective(models.Model):
    _name = 'nev.mbo.objective'

    # Nội dung MBO (vd: lấy chứng chỉ tiếng Nhật N3)
    name = fields.Text(string=_("MBO Content"), required=True)

    # Thời gian thực hiện MBO
    duration_mbo = fields.Date(string=_("Duration"), required=True)

    # Kế hoạch thực hiện MBO (vd: mỗi ngày học 2h, tháng 10 đăng ký thi, tháng 9 học tủ tài liệu
    action_plan_mbo = fields.Text(string=_("Actions"), required=True)

    # Đánh giá kết quả thực hiện MBO (vd: thi đạt N3: 60%, đạt từ 110 điểm trở lên: 80%, từ 130 điểm trở lên: 100%)
    evaluation_criteria_mbo = fields.Text(string=_("Evaluation"))

    # Tự đánh giá của nhân viên về mục tiêu (%)
    employee_result_by_percent_mbo = fields.Selection(
        [('50', '50%'), ('70', '70%'), ('90', '90%'), ('100', '100%'), ('105', '105%'), ('110', '110%'),
         ('120', '120%'), ('150', '150%'),
         ('170', '170%')],
        string=_("Eval. by employee (percent)"),
        required=True, default='100')

    # Tự đánh giá của nhân viên về mục tiêu (text)
    employee_result_by_text_mbo = fields.Selection(
        [('s+', 'S+'), ('s', 'S'), ('a+', 'A+'), ('a', 'A'), ('b+', 'B+'), ('b', 'B'), ('c+', 'C+'), ('c', 'C'),
         ('d+', 'D+'), ('d', 'D')],
        string=_("Eval. by employee (text)"),
        required=True, default='a')

    # Đánh giá của manager về mục tiêu (%)
    manager_result_by_percent_mbo = fields.Selection(
        [('50', '50%'), ('70', '70%'), ('90', '90%'), ('100', '100%'), ('105', '105%'), ('110', '110%'),
         ('120', '120%'), ('150', '150%'),
         ('170', '170%')],
        string=_("Eval. by manager (percent)"),
        required=True, default='100')

    # Đánh giá của manager về mục tiêu (text)
    manager_result_by_text_mbo = fields.Selection(
        [('s+', 'S+'), ('s', 'S'), ('a+', 'A+'), ('a', 'A'), ('b+', 'B+'), ('b', 'B'), ('c+', 'C+'), ('c', 'C'),
         ('d+', 'D+'), ('d', 'D')],
        string=_("Eval. by manager (text)"),
        required=True, default='a')

    objective_id = fields.Many2one('nev.mbo.mbo', ondelete='cascade', string=_("MBO Objective"), required=True)
