"""
File containing the subject model.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def materia(identificador, nombre, area):
    """
    Initialize a new instance of the subject class.

    Args:
        id (int): The subject's identifier.
        nombre (str): The subject's subject.
        area (str): The subject area.
    """
    # Creates and returns a dictionary representing a subject with the attributes provided.
    return {
        'id' : identificador,
        'nombre' : nombre,
        'area' : area
    }
