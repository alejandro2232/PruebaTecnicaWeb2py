"""
File containing the factor class for creating instances of student.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..modelos.modelo_estudiante import estudiante


def estudiante_factory(identificador, nombre, apellido, estado):
    """
    Create an instance of Estudiante.

    Args:
        identificador (int): The student's identifier.
        nombre (str): The student's name.
        apellido (str): The student's last name.
        estado (str): The student's attendance status.

    Returns:
        Estudiante: An instance of the Estudiante class.
    """
    # Uses the arguments provided to create and return an instance of the Student class.
    return estudiante(identificador=identificador, nombre=nombre, apellido=apellido, estado=estado)
