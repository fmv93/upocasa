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

class cliente(osv.Model):

    _name = 'cliente'
    _description = 'Cliente de la inmobiliaria'
 
    def _check_form(self, cr, uid, ids):   
        patron_dni = re.compile('\d{8}[A-Z]{1}')
        patron_phone = re.compile('\d{9}')
        patron_email = re.compile('^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$')
        for clase in self.browse(cr, uid, ids):
            if (patron_dni.search(clase.dni)and patron_phone.search(clase.phone)and patron_email.search(clase.email)):
                return True
            else:
                return False

    _columns = {
        'dni': fields.char('DNI', size=9, required=True),
        'name': fields.char('Nombre', size=60, required=True),
        'lastname': fields.char('Apellidos', size=100, required=True),
        'phone': fields.char('Telefono', size=60, required=True),
        'email': fields.char('Email', size=60, required=True),
        'buyer': fields.boolean('Comprador', required=False),
        'leaseholder': fields.boolean('Arrendatario', required=False),
        'interests': fields.text('Intereses'),        
                
        'visita_ids':fields.one2many('visita', 'cliente_dni', 'Visitas concertadas'),
        'contrato_ids':fields.one2many('contrato','cliente_ids' ,'Contrato'),
    }
    
    _constraints = [(_check_form, '¡ Errores en el formulario !' , [ 'dni','telefono','email' ])] 

    
    _sql_constraints=[('dni_uniq','unique (dni)','DNI de cliente ya registrado.')]
    
