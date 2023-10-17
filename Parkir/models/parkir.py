from odoo import models, fields, api, _
import datetime

class ParkirKendaraan(models.Model):
    _name = "parkir.kendaraan"
    _description = "Manage Parkir"
    _rec_name= 'parkir_nomor'

    @api.depends('parkiran_roda')
    def set_roda_group(self):
        for rec in self:
            if rec.parkiran_roda:
                if rec.parkiran_roda < 4:
                    rec.roda_group = "sepeda_motor"
                else:
                    rec.roda_group = "mobil"

    @api.depends('parkiran_roda')
    def set_parkir_nominal(self):
        for rec in self:
            if rec.parkiran_roda < 4 :
                rec.parkir_nominal = "2000"
            else:
                rec.parkir_nominal = '5000'

    parkir_nomor = fields.Char(string="Plat Nomor", required=True, default="0")
    parkiran_roda = fields.Integer(string="Kendaraan Roda", track_visibility='always')
    parkir_date_in = fields.Datetime(string="Tanggal Masuk")
    parkir_date_out = fields.Datetime(string="Tanggal Keluar")
    name_seq = fields.Char(string="Parkir Record", readonly=True, required=True,
                           index=True, copy=False, default=lambda self: _('New'))
    image = fields.Binary(string="Nomor By CCTV", help="This holds the image used as avatar for \ this contact, limited to 1024x1024px")
    parkir_lock = fields.Selection([
        ('none', "None"),
        ('b1', "Besment 01"),
        ('b2', "Besment 02"),
        ('b3', "Besment 03"),
        ('b4', "Besment 04"),
        ('b5', "Besment 05")
    ], default="none", string="Lokasi Parkir")
    
    state = fields.Selection([
        ('draft','Draft'),
        ('in_parkiran','Di Dalam Parkiran'),
        ('out_parkiran','Meninggalkan Parkiran'),
    ], string="Status", default="draft")

    def update_form_to_in_progress(self):
        for record in self:
            record.write({'state':'in_parkiran'})

    def update_form_to_in_finish(self):
        for record in self:
            record.write({'state':'out_parkiran'})

    
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New'))==_('New'):
            vals['name_seq']=self.env['ir.sequence'].next_by_code('parkir.kendaraan.sequence') or _('New')
        result = super(ParkirKendaraan,self).create(vals)
        return result


    roda_group = fields.Selection([
        ('sepeda_motor','Sepeda Motor'),
        ('mobil','Mobil'),
        # ('truk','Truk Atau Kendaraan Besar'),
    ], default='sepeda_motor', string='Kendaraan Group', compute='set_roda_group')

    parkir_nominal = fields.Selection([
        ('none', "None"),
        ('2000', "Rp. 2000"),
        ('5000', "Rp. 5000"),
    ], default="none", string="Nominal Parkir", compute='set_parkir_nominal')

    @api.onchange('parkir_nomor')
    def _onchange_parkir_nomor(self):
        new_parkir_nomor=self.parkir_nomor
        self.parkir_nomor=new_parkir_nomor.upper()
    
    
