"""
File that defines the model of the table 'subjects' in the database.

This file uses the gluon.dal module to establish the connection
to the database in Postgres already created previously and defines
the structure of the table 'subjects' that is already created in
the database, this table structure was created with the help of alembic
"""

# -*- coding: utf-8 -*-

db.define_table('materias',
    Field('id','integer'),
    Field('nombre','string'),
    Field('area','string'),
    migrate=False
)
