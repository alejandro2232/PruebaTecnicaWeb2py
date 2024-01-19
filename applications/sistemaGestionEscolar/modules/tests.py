"""
file where the testing of the student, classroom and
subject models and the repository has been performed,
thus ensuring that the creation and updating of the
database information works correctly.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from modelos.modelo_estudiante import estudiante
from modelos.modelo_salones import salones
from modelos.modelo_materia import materia
from repository import EstudiantesRepository



# from factoriaEstudiantes import EstudiantesFactory


class TestEstudiantesRepository(unittest.TestCase):
    """
    Test class for EstudiantesRepository.
    """
    def setUp(self):
        """
        Set up method to create an instance of the database for testing.
        """
        # create in-memory database instance for tests
        self.db_mock = MagicMock()

    def test_modelo_estudiante(self):
        """
        Test for the student model, successful.
        """
        est = estudiante(identificador=1, nombre="John", apellido="Doe", estado="Activo")
        self.assertEqual(est['id'], 1)
        self.assertEqual(est['nombre'], "John")
        self.assertEqual(est['apellido'], "Doe")
        self.assertEqual(est['estado'], "Activo")

    def test_modelo_salones(self):
        """
        Test for the classroom model, successful.
        """
        # Create an instance of the model
        salon = salones(identificador=1, nombre="A2", edificio="Edificio Giordano Bruno")

        # Verify that the attributes have been assigned correctly
        self.assertEqual(salon['id'], 1)
        self.assertEqual(salon['nombre'], "A2")
        self.assertEqual(salon['edificio'], "Edificio Giordano Bruno")

    def test_modelo_materias(self):
        """
        Test for the subject model.
        """
        # Create an instance of the model
        mat = materia(identificador=1, nombre="Español", area="Lenguas")

        # Verify that the attributes have been assigned correctly
        self.assertEqual(mat['id'], 1)
        self.assertEqual(mat['nombre'], "Español")
        self.assertEqual(mat['area'], "Lenguas")

    def test_create_estudiante(self):
        """
        Test to register a student using the repository class, successful.
        """
        # Create a mock object for the insert method of self.db.students
        with patch("repository.EstudiantesRepository.create_estudiante") as mock_insert:
            # configure the return of the insert method
            mock_insert.return_value = (1)

            # We call the function we want to test
            repository = EstudiantesRepository(self.db_mock)
            result = repository.create_estudiante("Daniel", "Barreto")

            # We verify that the insert method was called with the correct arguments
            mock_insert.assert_called_with("Daniel", "Barreto")

            # Check return value
            self.assertEqual(result, 1)

    def test_get_estudiantes(self):
        """
        Test to generate a list of students using the repository class, successful.
        """
        with patch(
            "repository.EstudiantesRepository.get_estudiantes"
                  ) as mocked_select:
            mocked_select.return_value = [
                {
                    "id": 1,
                    "nombre": "Daniel",
                    "apellido": "Barreto",
                    "estado": "asistio",
                },
                {"id": 2, "nombre": "Sara", "apellido": "Gomez", "estado": None},
            ]

            repository = EstudiantesRepository(self.db_mock)
            estudiantes = repository.get_estudiantes()

            mocked_select.assert_called_with()

            self.assertEqual(
                estudiantes,
                [
                    {
                        "id": 1,
                        "nombre": "Daniel",
                        "apellido": "Barreto",
                        "estado": "asistio",
                    },
                    {"id": 2, "nombre": "Sara", "apellido": "Gomez", "estado": None},
                ],
            )

    def test_get_estudiante(self):
        """
        Test for getting a specific student using the repository class, successful.
        """
        with patch(
            "repository.EstudiantesRepository.get_estudiante"
        ) as mocked_select:
            mocked_select.return_value = {
                "id": 1,
                "nombre": "Daniel",
                "apellido": "Barreto",
                "estado": "asistio",
            }

            repository = EstudiantesRepository(self.db_mock)
            est = repository.get_estudiante(1)

            mocked_select.assert_called_with(1)
            self.assertEqual(
                est,
                {
                    "id": 1,
                    "nombre": "Daniel",
                    "apellido": "Barreto",
                    "estado": "asistio",
                },
            )

    def test_update_estudiante_exitoso(self):
        """
        Test to update a student's attendance status, successful.
        """
        estudiante_existente = MagicMock()
        estudiante_existente.id = 1
        estudiante_existente.update_record.return_value = True

        # Configure the get_student mock to return the existing student
        with patch(
            "repository.EstudiantesRepository.get_estudiante"
        ) as mocked_get_estudiante:
            mocked_get_estudiante.return_value = estudiante_existente

            # create the repository instance and call the update_student method
            repository = EstudiantesRepository(self.db_mock)
            resultado = repository.update_estudiante(1, "asistio")

            # Verify that update_record was called with the provided ParamState
            estudiante_existente.update_record.assert_called_with(estado="asistio")

            # Verify that the method returned True
            self.assertTrue(resultado)

    def test_update_estudiante_no_existente(self):
        """
        Test to update the attendance status of a non-existing student, successful.
        """
        # Configuring a student that does not exist in the simulated database
        with patch(
            "repository.EstudiantesRepository.get_estudiante"
        ) as mocked_get:
            mocked_get.return_value = False
            repository = EstudiantesRepository(self.db_mock)
            resultado = repository.update_estudiante(1, "ausente")

            mocked_get.assert_called_with(1)
            self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()
