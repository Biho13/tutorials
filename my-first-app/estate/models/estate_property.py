from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description', copy=True)
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available from', copy=False, default=fields.Date.today())
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default="2")
    living_area = fields.Integer(string='Living area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden area')
    garden_orientation = fields.Selection(string='Garden orientation', selection=[('north', 'North'), ('east', 'East'), ('west', 'West'), ('south', 'South')], help="Type is used to separate Leads and Opportunities")
    status = fields.Selection(string='Status', selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')], help="Type is used to separate Leads and Opportunities")
    active = fields.Boolean(string='Active')

    #sale_man_id = fields.Many2one('res.users', String='Salesman')
    #buyer_id = fields.Many2one('res.partner', String='Buyer', copy=False)

    #property_type_id = fields.Many2one('estate.property.type', string='property Type')
    #offer_ids = fields.One2many('estate.property.offer', 'property_id')


    #price = fields.Float(string='Price')
    #status_ = fields.Selection(string='Status', selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    #partner_id = fields.Many2one('res.partner', String='Partner', index=True, tracking=True)

