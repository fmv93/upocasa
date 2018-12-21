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

class contrato(osv.Model):

    _name = 'contrato'
    _description = 'Contrato de la relacion entre un cliente y un inmueble'
 
    _columns = {
        'name': fields.char('Id', size=9, required=True),
        'date': fields.date('Fecha', size=100, required=True),
        'buy': fields.boolean('Compra', required=False),
        'lease': fields.boolean('Alquiler', required=False),
        
        'cliente_ids':fields.one2many('cliente', 'contrato_ids', 'Clientes', required=True),
        'agente_dni_contrato':fields.many2one('agente', 'Agente', required=True),
        'inmueble_id':fields.many2one('inmueble', 'Inmueble'),
    }
