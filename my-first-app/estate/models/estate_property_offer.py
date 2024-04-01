from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    #price = fields.Float(string='Price')
    #status_offer = fields.Selection(string='Status', selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)

    #partner_id = fields.Many2one('res.partner', String='Partner', index=True, tracking=True, required=True)
    #property_id = fields.Many2one('estate.property', required=True, String='Property')

