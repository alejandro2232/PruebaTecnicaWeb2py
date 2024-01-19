"""
File that defines the model of the table 'salons' in the database.

This file uses the gluon.dal module to establish the connection to the database in Postgres already created previously
and defines the structure of the table 'salons' that is already created in the database, this table structure was created with the help of alembic
"""

# -*- coding: utf-8 -*-
db.define_table('salones',
    Field('id','integer'),
    Field('nombre','string'),
    Field('edificio','string'),
    migrate=False  # Esto evita que web2py intente gestionar la migración de la tabla
)
