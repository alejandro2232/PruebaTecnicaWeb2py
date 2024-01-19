"""
File containing the renderer class that will be
in charge of generating the visualization
of the student, subject and classroom models
using Web2py HTML objects, ensuring that each
element is correctly displayed in the interface.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon.html import TABLE,THEAD,TR,TH,TD,SELECT,OPTION
from .factory.factoria_materia import MateriaFactory
from .factory.factoria_estudiante import estudiante_factory
from .factory.factoria_salones import SalonesFactory
from .repository import EstudiantesRepository


class Renderer:
    """
    Class to represent the table where the data of
    the student, the subjects and the classroom will be shown.
    """
    def __init__(self, db):
        """
        Initialize data.

        Args:
        db: The database object being used.
        repository: an instance of StudentsRepository to access student data.
        """
        self.db = db
        self.repository = EstudiantesRepository(db)

    def renderer_estudiantes(self):
        """
        Displays a table with the student's information.

        Returns:
            TABLE: HTML table containing the student information.
        """
        # Gets the list of students from the repository
        estudiantes = self.repository.get_estudiantes()

        # Create the HTML table structure
        table = TABLE(
            THEAD(
                TR(
                    TH("ID", _style="width: 10%;"),
                    TH("Nombre", _style="width: 30%;"),
                    TH("Apellido", _style="width: 30%;"),
                    TH("Estado", _style="width: 30%;"),
                )
            ),
            _class="table table-bordered",
        )

        # Adds rows to the table for each student
        for i, est in enumerate(estudiantes):
            estudiante = estudiante_factory(
                est.id, est.nombre, est.apellido, est.estado
            )

            row = TR(
                TD(i + 1),
                TD(estudiante['nombre']),
                TD(estudiante['apellido']),
                TD(
                    SELECT(
                        OPTION("Seleccione un estado", _value=""),
                        OPTION(
                            "Ausente",
                            _value="ausente",
                            _selected=(estudiante['estado'] == "ausente"),
                        ),
                        OPTION(
                            "Asistió",
                            _value="asistio",
                            _selected=(estudiante['estado'] == "asistio"),
                        ),
                        _name="estado_asistencia",
                        _class="select-asistencia",
                        _onchange="obtenerValorSeleccionado(this , "
                        + str(estudiante['id'])
                        + ")",
                    )
                ),
            )
            table.append(row)
        return table

    def renderer_materias(self):
        """
        Displays a table with subject information.

        Returns:
            TABLE: HTML table containing the subject information.
        """
        # Gets the list of subjects from the database
        materias = self.db(self.db.materias.id > 0).select()

        # makes an instance of subject
        factory = MateriaFactory()

        # Create the HTML table structure
        table = TABLE(
            THEAD(
                TR(
                    TH("ID", _style="width: 10%;"),
                    TH("Nombre", _style="width: 45%;"),
                    TH("Area", _style="width: 45%;"),
                )
            ),
            _class="table table-bordered",
        )

        # Add rows to the table for each subject
        for i, mat in enumerate(materias):
            materia = factory.modelo_materias(mat.id, mat.nombre, mat.area)

            row = TR(
                TD(i+1),
                TD(materia['nombre']),
                TD(materia['area']),
            )
            table.append(row)

        return table

    def renderer_salones(self):
        """
        Displays a table with classroom information.

        Returns:
            TABLE: HTML table containing the classroom information.
        """
        # Puedes acceder a los atributos de tu modelo
        salones = self.db(self.db.salones.id > 0).select()

        # makes an instance of classroom
        factory = SalonesFactory()

        # Create the HTML table structure
        table = TABLE(
            THEAD(
                TR(
                    TH("ID", _style="width: 10%;"),
                    TH("Nombre", _style="width: 45%;"),
                    TH("Edificio", _style="width: 45%;"),
                )
            ),
            _class="table table-bordered",
        )

        # Adds rows to the table for each classroom
        for i, sal in enumerate(salones):
            salon = factory.modelo_salones(sal.id, sal.nombre, sal.edificio)

            row = TR(
                TD(i+1),
                TD(salon['nombre']),
                TD(salon['edificio']),
            )
            table.append(row)

        return table
