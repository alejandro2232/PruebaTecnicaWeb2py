"""
File that defines the model of the 'students' table in the database.

This file uses the gluon.dal module to establish the connection
to the database in Postgres already created previously and defines
the structure of the 'students' table which is already created in
the database, this table structure was created with the help of alembic
"""
# -*- coding: utf-8 -*-


from gluon.dal import DAL,Field
# Conectar a la base de datos
db = DAL('postgres://director:1234@localhost:5432/postgres')

db.define_table('estudiantes',
    Field('id','integer'),
    Field('nombre','string'),
    Field('apellido','string'),
    Field('estado','string'),
    migrate=False  # Esto evita que web2py intente gestionar la migración de la tabla
)


