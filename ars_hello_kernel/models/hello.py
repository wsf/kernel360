# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ars_hello_kernel(models.Model):
        _name = 'ars_hello_kernel.hello'
        _description = 'ars_hello_kernel.hello'

        name = fields.Char()
        value = fields.Integer()
        value2 = fields.Float(compute="_value_pc", store=True)
        description = fields.Text()

        @api.depends('value')
        def _value_pc(self):
            for record in self:
                record.value2 = float(record.value) / 100
