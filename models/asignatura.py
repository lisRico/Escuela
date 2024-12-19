from odoo import models, fields

class Asignatura(models.Model):
    _name = 'escuela.asignatura'
    _description = 'Asignaturas de la escuela'

    codigo_asignatura = fields.Char(string="Código", required=True)
    nombre_asignatura = fields.Char(string="Nombre de la asignatura", required=True)
    descripcion = fields.Text(string="Descripción")
    numero_horas = fields.Integer(string="Número de horas", required=True)
    grupo_ids = fields.Many2many('escuela.grupo', string="Grupos")