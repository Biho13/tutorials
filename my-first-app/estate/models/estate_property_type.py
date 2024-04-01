from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Tag"

    name_type = fields.Char(string='Title', required=True)


