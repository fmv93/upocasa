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
import re

class arquitecto(osv.Model):
    
    _name = 'arquitecto'
    _description = 'Persona dedicada al diseno de los inmuebles.'
    
    def _check_form(self, cr, uid, ids):   
        patron_cif = re.compile('\d{8}[A-Z]{1}')
        patron_phone = re.compile('\d{9}')
        for clase in self.browse(cr, uid, ids):
            if (patron_cif.search(clase.cif) and patron_phone.search(clase.phone)):
                return True
            else:
                return False
 
    _columns = {
        'cif': fields.char('CIF', size=9, required=True),
        'name': fields.char('Nombre', size=60, required=True),
        'address': fields.char('Direccion', size=60, required=True),
        'phone': fields.char('Telefono', size=9, required=True),
        'tasadores_dnis': fields.many2many('tasador','arquitecto_tasador_rel','arquitecto_cif','tasador_dni','Asesoramiento A2T')
    }
    
    _constraints = [(_check_form, '¡ Errores en el formulario !' , [ 'CIF','telefono' ])] 
    
    _sql_constraints=[('cif_uniq','unique (cif)','CIF de arquitecto registrado.')]  