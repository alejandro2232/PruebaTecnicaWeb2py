"""
File containing the factory class of the classroom
class using the singleton design pattern and Caché.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..modelos.modelo_materia import materia


class MateriaFactory:
    """
    Factory class for creating room instances
    """
    # Dictionary for caching subject instances
    _cache = {}

    def __new__(cls):
        """
        This method ensures that only one instance of the subject class is created,
        returning the existing instance if it has already been created.

        Args:
            cls: The class itself.

        Returns:
            MateriaFactory: The instance of MateriaFactory.
        """

        # Singleton pattern: Ensure only one instance of the factory class is created
        if not hasattr(cls, "_instance"):
            cls._instance = super(MateriaFactory, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def modelo_materias(identificador, nombre, area):
        """
        Creates an instance of Materia or retrieves it from the cache if available.

        This method checks if an instance of Materia with the `name` and
        `area` already exists in the cache. If yes, it returns the existing
        instance. Otherwise, a new instance of Materia is created, cached and returned.

        Args:
            identifier (int): The subject's identifier.
            nombre (str): The subject's subject.
            area (str): The subject area.

        Returns:
            Subject: An instance of the subject class.
        """

        # Create a unique key for the cache based on nombre and area
        cache_key = (nombre, area)

        # Check if an instance with the same key exists in the cache
        if cache_key not in MateriaFactory._cache:
            print(f"Creando nueva instancia de materia para clave {cache_key}")
            # If not, create a new instance and add it to the cache
            MateriaFactory._cache[cache_key] = materia(
                identificador=identificador,
                nombre=nombre,
                area=area
            )

        else:
            print(f"Reutilizando instancia de materia para clave {cache_key}")
        # If an instance with the same key exists, reuse it
        return MateriaFactory._cache[cache_key]
