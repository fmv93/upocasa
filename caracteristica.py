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

class caracteristica(osv.Model):
    
    
    _name = 'caracteristica'
    _description = 'caracteristicas de un inmueble'
 
    _columns = {
            'name': fields.char('Nombre', size=60, required=True),
            'description': fields.char('Descripcion', size=120, required=False),
            'value': fields.integer('tasacion', size=20, required=True),
            
            'inmueble_id':fields.many2one('inmueble','Inmueble', required=True),
        }

    def clear_record_data(self,cr,uid,ids,context=None):
        self.write(cr,uid, ids,{'name': ''}, context)
        self.write(cr,uid, ids,{'description': ''}, context)
        self.write(cr,uid, ids,{'value': 0}, context)
      