"""
File containing the factory class of the subject
class using the singleton and Caché design pattern.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..modelos.modelo_salones import salones


class SalonesFactory:
    """
    Factory class for creating instances of Salones
    """
    # Dictionary for caching classrooms instances
    _cache = {}

    def __new__(cls):
        """
        This method ensures that only one instance of the class rooms
        is created, returning the existing instance if it has already been created.

        Args:
            cls: The class itself.

        Returns:
            SalonesFactory: The instance of MateriaFactory.
        """
        # Singleton pattern: Ensure only one instance of the factory class is created
        if not hasattr(cls, "_instance"):
            cls._instance = super(SalonesFactory, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def modelo_salones(identificador, nombre, edificio):
        """
        Creates a room instance or retrieves it from the cache if available.

        This method checks if a room instance with the `name` and `building`
        already exists in the cache. If yes, it returns the existing instance.
        Otherwise, a new room instance is created, cached and returned.

        Args:
            identifier (int): The classroom identifier.
            name (str): The name of the classroom.
            building (str): the classroom building

        Returns:
            Subject: An instance of the Salon class.
        """
        # Create a unique key for the cache based on nombre and edificio
        cache_key = (nombre, edificio)

        # Check if an instance with the same key exists in the cache
        if cache_key not in SalonesFactory._cache:
            print(f"Creando nueva instancia de salones para clave {cache_key}")
            # If not, create a new instance and add it to the cache
            SalonesFactory._cache[cache_key] = salones(
                identificador=identificador , nombre=nombre, edificio=edificio
            )

        else:
            print(f"Reutilizando instancia de salones para clave {cache_key}")
        # If an instance with the same key exists, reuse it
        return SalonesFactory._cache[cache_key]
