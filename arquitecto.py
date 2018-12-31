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

'''
Created on 28 dic. 2018

@author: usuario
'''

from osv import osv
from osv import fields

class arquitecto(osv.Model):
    _name = 'arquitecto'
    _description = 'Persona dedicada al diseño de los inmuebles.'
 
    _columns = {
        'cif': fields.char('CIF', size=9, required=True),
        'name': fields.char('Nombre', size=60, required=True),
        'address': fields.char('Direccion', size=60, required=True),
        'phone': fields.char('Telefono', size=60, required=True),
    }