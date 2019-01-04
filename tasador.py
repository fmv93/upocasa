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

class tasador(osv.Model):
    
    _name = 'tasador'
    _description = 'Persona encargada de tasar.'
    
    def _check_form(self, cr, uid, ids):   
        patron_dni = re.compile('\d{8}[A-Z]{1}')
        patron_phone = re.compile('\d{9}')
        for clase in self.browse(cr, uid, ids):
            if (patron_dni.search(clase.dni) and patron_phone.search(clase.phone)):
                return True
            else:
                return False
 
 
    _columns = {
        'dni': fields.char('DNI', size=9, required=True),
        'name': fields.char('Nombre', size=60, required=True),
        'lastname': fields.char('Apellidos', size=60, required=True),
        'phone': fields.char('Telefono', size=60, required=True),
        'inmueble_ids':fields.one2many('inmueble', 'tasador_dni', 'Inmueble', required=True),
        'arquitectos_cifs': fields.many2many('arquitecto','tasador_arquitecto_rel','tasador_dni','arquitecto_cif','Es asesorado por'),
    }
    

    _constraints = [(_check_form, '¡ Errores en el formulario !' , [ 'DNI','telefono' ])] 
    _sql_constraints=[('dni_uniq','unique (dni)','DNI de tasador registrado.')]  
