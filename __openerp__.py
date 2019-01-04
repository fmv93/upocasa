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

{
    "name": "UPOCASA",
    "version": "1.0",
    "depends": ["base"],
    "author": "Equipo 7",
    "category": "Inmobiliaria",
    "description": """
    Gestion de una inmobiliaria
    """,
    "init_xml": [],
    'data': ['cliente_view.xml', 'visita_view.xml', 'inmueble_view.xml', 'contrato_view.xml', 'agente_view.xml', 'tasador_view.xml', 'arquitecto_view.xml', 'propietario_view.xml', 'caracteristica_view.xml', 'workflow/inmueble_workflow.xml'],
    'demo_xml': ['upocasa_demo.xml'],
    'installable': True,
    'active': False
}