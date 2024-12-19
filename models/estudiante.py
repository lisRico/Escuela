from odoo import models, fields

class Estudiante(models.Model):
    _name = 'escuela.estudiante'
    _description = 'Estudiante de la escuela'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    edad = fields.Integer(string="Edad", required=True)
    correo = fields.Char(string="Correo Electrónico", required=True) 
    telefono = fields.Char(string="Teléfono") 
    grupo_id = fields.Many2one('escuela.grupo', string="Grupo")