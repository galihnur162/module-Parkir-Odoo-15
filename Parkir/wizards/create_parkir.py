from odoo import fields, models

class CreateParkir(models.TransientModel):
    _name = 'create.parkir'
    _description = 'Create Parkir'

    parkir_id = fields.Many2one('parkir.kendaraan', "Parkir")
    parkir_date = fields.Date("Parkir Date")