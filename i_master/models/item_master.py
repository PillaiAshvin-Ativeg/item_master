from odoo import models, fields

class ItemMaster(models.Model):
    _name = 'item.master'
    _description = 'Item Master'

    brand = fields.Char(string="Brand")
    segment = fields.Char(string="Segment")
    width = fields.Float(string="Width")
    length = fields.Float(string="Length")
    height = fields.Float(string="Height")
    noon = fields.Char(string="Noon")
    amazon = fields.Char(string="Amazon")
    internal_id = fields.Integer(string="Internal ID")
