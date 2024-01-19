"""
File containing the classroom model.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def salones(identificador, nombre, edificio):
    """
    Model representing a classroom.

    Args:
        id (int): The classroom identifier.
        name (str): The name of the classroom.
        edificio (str): the classroom building
    """
    # Creates and returns a dictionary representing a classroom with the attributes provided.
    return{
        'id' : identificador,
        'nombre' : nombre,
        'edificio' : edificio
    }
