"""
File containing the student's model
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def estudiante(identificador, nombre, apellido, estado):
    """
    Initialize a new instance of the Estudiante class.
    Args:
        id (int): The student's identifier.
        name (str): The student's name.
        apellido (str): The student's last name.
        estado (str): The student's attendance status.
    """
    # Creates and returns a dictionary representing a student with the attributes provided.
    return {
        'id': identificador,
        'nombre': nombre,
        'apellido': apellido,
        'estado': estado
    }
