# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class inmueble(osv.Model):

    _name = 'inmueble'
    _description = 'Inmueble gestionado por la inmobiliaria'
 
    _columns = {
        'inmueble_id': fields.integer('Id', size=9, required=True),
        'address': fields.char('Direccion', size=60, required=True),
        'postal_code': fields.integer('Codigo postal', size=5, required=True),
        'price': fields.float('Precio', size=20, required=True),
        'data': fields.text('Datos'),
        'score': fields.float('Valoracion', size=20),

        'visita_ids':fields.one2many('visita', 'inmueble_id', 'Visitas concertadas en el inmueble'),
    }